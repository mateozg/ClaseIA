"""Prueba del ejercicio 4: representación vectorial de textos."""

from embedding_utils import embed_texts


def test_embed_texts_creates_one_non_empty_vector_per_text() -> None:
    vectors, _ = embed_texts(["gato negro", "perro negro"])

    assert vectors.shape[0] == 2
    assert vectors.shape[1] > 0
    assert vectors.nnz > 0
