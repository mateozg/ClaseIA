"""Laboratorio Streamlit para generación, tokenización y embeddings con Groq."""

from __future__ import annotations

import html
import math
from collections.abc import Sequence


GROQ_MODELS = {
    "GPT-OSS 20B (Groq)": "openai/gpt-oss-20b",
    "GPT-OSS 120B (Groq)": "openai/gpt-oss-120b",
    "Llama 3.1 8B Instant": "llama-3.1-8b-instant",
    "Llama 3.3 70B Versatile": "llama-3.3-70b-versatile",
}

TOKENIZERS = {
    "GPT-4o (o200k_base)": "o200k_base",
    "GPT-4 / GPT-3.5 (cl100k_base)": "cl100k_base",
    "Codex (p50k_base)": "p50k_base",
}

EMBEDDING_MODELS = {
    "TF-IDF (rápido, local)": "tfidf",
    "all-MiniLM-L6-v2 (inglés)": "sentence-transformers/all-MiniLM-L6-v2",
    "paraphrase-multilingual-MiniLM-L12-v2 (multilingüe)": (
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    ),
}

PALETTE = ("#2563eb", "#7c3aed", "#db2777", "#ea580c", "#16a34a", "#0891b2")


def token_color(token_id: int) -> str:
    """Devuelve un color determinista para un ID de token."""
    return PALETTE[token_id % len(PALETTE)]


def tokenize_text(text: str, encoding_name: str) -> list[dict[str, int | str]]:
    """Tokeniza y conserva ID, fragmento decodificado y color por token.

    Si tiktoken todavía no está instalado, muestra una representación UTF-8 que
    permite abrir la interfaz; al instalar dependencias se usa el tokenizer real.
    """
    try:
        import tiktoken

        encoding = tiktoken.get_encoding(encoding_name)
        ids = encoding.encode(text, disallowed_special=())
        pieces = [encoding.decode([token_id]) for token_id in ids]
    except ImportError:
        ids = list(text.encode("utf-8"))
        pieces = [bytes([item]).decode("utf-8", errors="replace") for item in ids]

    return [
        {"id": token_id, "text": piece, "color": token_color(token_id)}
        for token_id, piece in zip(ids, pieces, strict=True)
    ]


def cosine_similarity(first: Sequence[float], second: Sequence[float]) -> float:
    """Calcula similitud coseno sin depender de NumPy."""
    if not first or not second or len(first) != len(second):
        return 0.0
    if first == second:
        return 1.0
    numerator = sum(left * right for left, right in zip(first, second, strict=True))
    first_norm = math.sqrt(sum(value * value for value in first))
    second_norm = math.sqrt(sum(value * value for value in second))
    if first_norm == 0 or second_norm == 0:
        return 0.0
    return numerator / (first_norm * second_norm)


def embed_texts(texts: list[str], model_name: str) -> list[list[float]]:
    """Genera embeddings locales, evitando enviar los textos a Groq."""
    if model_name == "tfidf":
        from sklearn.feature_extraction.text import TfidfVectorizer

        return TfidfVectorizer().fit_transform(texts).toarray().tolist()

    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(model_name).encode(texts, normalize_embeddings=True).tolist()


def render_token_html(tokens: list[dict[str, int | str]]) -> str:
    """Crea etiquetas HTML seguras para visualizar tokens con ID y color."""
    spans = []
    for token in tokens:
        fragment = html.escape(str(token["text"])).replace("\n", "↵<br>")
        spans.append(
            '<span title="ID: {id}" style="background:{color}; color:white; '
            'padding:3px 5px; margin:2px; border-radius:4px; display:inline-block; '
            'font-family:monospace">{text}<small> · {id}</small></span>'.format(
                id=token["id"], color=token["color"], text=fragment
            )
        )
    return "".join(spans) or "<em>No hay tokens para mostrar.</em>"


def generate_with_groq(
    api_key: str, model: str, system_prompt: str, user_prompt: str, temperature: float,
    max_tokens: int, top_p: float,
) -> str:
    """Solicita una respuesta de chat a Groq mediante su SDK oficial."""
    from groq import Groq

    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_completion_tokens=max_tokens,
        top_p=top_p,
    )
    return completion.choices[0].message.content or ""


def run_app() -> None:
    import streamlit as st

    st.set_page_config(page_title="Laboratorio Groq", page_icon="🧪", layout="wide")
    st.title("🧪 Laboratorio de modelos: Groq, tokens y embeddings")
    st.caption("La clave se usa solo durante la sesión y no se guarda en el proyecto.")

    with st.sidebar:
        st.header("Conexión y generación")
        saved_key = st.secrets.get("GROQ_API_KEY", "")
        api_key = st.text_input("Groq API key", value=saved_key, type="password")
        model_label = st.selectbox("Modelo de generación", list(GROQ_MODELS))
        temperature = st.slider("Temperatura", 0.0, 2.0, 0.7, 0.1)
        max_tokens = st.slider("Máximo de tokens", 32, 4096, 512, 32)
        top_p = st.slider("Top-p", 0.0, 1.0, 1.0, 0.05)

    tab_generate, tab_tokens, tab_similarity = st.tabs(
        ["Generar texto", "Tokenización", "Embeddings y fases"]
    )
    with tab_generate:
        system_prompt = st.text_area("Instrucción de sistema", "Responde de forma clara y útil.")
        user_prompt = st.text_area("Prompt", "Explica qué es la similitud coseno.", height=150)
        if st.button("Generar con Groq", type="primary"):
            if not api_key:
                st.warning("Ingresa una Groq API key para generar texto.")
            elif not user_prompt.strip():
                st.warning("Escribe un prompt antes de generar.")
            else:
                with st.spinner("Generando respuesta..."):
                    try:
                        response = generate_with_groq(
                            api_key, GROQ_MODELS[model_label], system_prompt, user_prompt,
                            temperature, max_tokens, top_p,
                        )
                        st.subheader("Respuesta")
                        st.write(response)
                    except Exception as error:  # SDK / red / validación remota
                        st.error(f"Groq no pudo completar la solicitud: {error}")

    with tab_tokens:
        tokenizer_label = st.selectbox("Esquema de tokenización", list(TOKENIZERS))
        token_text = st.text_area("Texto a tokenizar", "La IA aprende representaciones del texto.")
        tokens = tokenize_text(token_text, TOKENIZERS[tokenizer_label])
        st.metric("Cantidad de tokens", len(tokens))
        st.markdown(render_token_html(tokens), unsafe_allow_html=True)
        st.dataframe(
            [{"ID": item["id"], "Token": item["text"], "Color": item["color"]} for item in tokens],
            use_container_width=True,
            hide_index=True,
        )

    with tab_similarity:
        st.write("Compara la cercanía semántica entre dos fases o fragmentos de texto.")
        first = st.text_area("Fase A", "Definir el problema y los datos.")
        second = st.text_area("Fase B", "Preparar y analizar los datos disponibles.")
        embedding_label = st.selectbox("Modelo de embeddings", list(EMBEDDING_MODELS))
        if st.button("Calcular similitud"):
            if not first.strip() or not second.strip():
                st.warning("Ambas fases deben contener texto.")
            else:
                with st.spinner("Creando embeddings..."):
                    try:
                        vectors = embed_texts([first, second], EMBEDDING_MODELS[embedding_label])
                        score = cosine_similarity(vectors[0], vectors[1])
                        st.metric("Similitud coseno", f"{score:.3f}")
                        st.progress(max(0, min(100, round((score + 1) * 50))))
                    except Exception as error:
                        st.error(f"No se pudieron generar embeddings: {error}")


if __name__ == "__main__":
    run_app()
