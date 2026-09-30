"""Pruebas de la lógica pura de la app de exploración de LLMs."""

from pathlib import Path

from main_app import cosine_similarity, tokenize_text


def test_main_app_module_is_present() -> None:
    """La aplicación Streamlit se entrega como un módulo ejecutable."""
    assert Path(__file__).with_name("main_app.py").is_file()


def test_tokenize_text_includes_token_id_and_hex_color() -> None:
    tokens = tokenize_text("Hola mundo", "cl100k_base")

    assert tokens
    assert all(isinstance(item["id"], int) for item in tokens)
    assert all(item["color"].startswith("#") for item in tokens)


def test_cosine_similarity_is_one_for_identical_vectors() -> None:
    assert cosine_similarity([1.0, 2.0], [1.0, 2.0]) == 1.0


def test_cosine_similarity_is_zero_when_one_vector_is_empty() -> None:
    assert cosine_similarity([], [1.0, 2.0]) == 0.0
