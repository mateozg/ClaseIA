"""Funciones reutilizables para el ejercicio 4 de Clase 12."""

from collections.abc import Sequence

from sklearn.feature_extraction.text import TfidfVectorizer


def embed_texts(texts: Sequence[str]):
    """Convierte textos en vectores TF-IDF y devuelve también el vectorizador."""
    vectorizer = TfidfVectorizer(stop_words=None)
    return vectorizer.fit_transform(texts), vectorizer
