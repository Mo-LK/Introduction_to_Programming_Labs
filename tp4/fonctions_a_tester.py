import math
from typing import Tuple, Union


def fizz_buzz(nombre: int) -> str:
    result = str(nombre)

    if nombre % 3 == 0 and nombre % 5 == 0:
        result = "fizzbuzz"
    elif nombre % 3 == 0:
        result = "fizz"
    elif nombre % 5 == 0:
        result = "buzz"

    return result


def resoudre_equation(a: int, b: int, c: int) -> Union[None, float, Tuple[float, float]]:
    delta = b ** 2 - 4 * a * c

    na_pas_de_solution = delta < 0

    if na_pas_de_solution:
        return None

    a_une_seule_solution = delta == 0

    if a_une_seule_solution:
        racine_1 = (-b + math.sqrt(delta)) / (2 * a)
        return racine_1

    a_deux_solutions = delta > 0

    if a_deux_solutions:
        racine_1 = (-b + math.sqrt(delta)) / (2 * a)
        racine_2 = (-b - math.sqrt(delta)) / (2 * a)
        return racine_1, racine_2
