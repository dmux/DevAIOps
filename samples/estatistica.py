from typing import List, Optional


def calcular_media(valores: List[float]) -> Optional[float]:
    """Calcula a média aritmética de uma lista de números. Retorna None se a lista estiver vazia."""
    if not valores:
        return None
    return sum(valores) / len(valores)


def encontrar_maior_menor(valores: List[float]) -> Optional[tuple]:
    """Retorna uma tupla (maior, menor) da lista. Retorna None se a lista estiver vazia."""
    if not valores:
        return None
    return max(valores), min(valores)


def normalizar_lista(valores: List[float]) -> List[float]:
    """Normaliza a lista de números para o intervalo [0, 1]. Se todos os valores forem iguais, retorna lista de zeros."""
    if not valores:
        return []
    maior = max(valores)
    menor = min(valores)
    if maior == menor:
        return [0.0 for _ in valores]
    return [(v - menor) / (maior - menor) for v in valores]
