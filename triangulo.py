from __future__ import annotations

EQUILATERO = "EL TRIANGULO ES EQUILATERO"
ISOSCELES = "EL TRIANGULO ES ISOSCELES"
ESCALENO = "EL TRIANGULO ES ESCALENO"
TRIANGULO_INVALIDO = "LOS VALORES INGRESADOS NO FORMAN UN TRIANGULO"

MENSAJE_LADO_NO_POSITIVO = "El lado debe ser un numero positivo y finito."
MENSAJE_VALOR_INVALIDO = "Valor invalido. Ingrese un numero."


def es_triangulo_valido(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a


def clasificar_triangulo(a: float, b: float, c: float) -> str:
    if not es_triangulo_valido(a, b, c):
        return TRIANGULO_INVALIDO

    if a == b == c:
        return EQUILATERO
    if a == b or b == c or a == c:
        return ISOSCELES
    return ESCALENO


def pedir_lado(nombre: str) -> float:
    while True:
        try:
            valor = float(input(f"INGRESE EL LADO {nombre} DEL TRIANGULO: "))
        except ValueError:
            print(MENSAJE_VALOR_INVALIDO)
            continue

        if valor <= 0 or valor == float("inf"):
            print(MENSAJE_LADO_NO_POSITIVO)
            continue

        return valor


def main() -> None:
    a = pedir_lado("A")
    b = pedir_lado("B")
    c = pedir_lado("C")

    print(clasificar_triangulo(a, b, c))


if __name__ == "__main__":
    main()
