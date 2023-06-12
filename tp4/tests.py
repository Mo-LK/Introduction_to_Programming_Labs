import unittest
from unittest import TestCase
import fonctions_a_tester as fcts


class TestFizzBuzz(TestCase):
    def test_fizz_buzz_3(self):
        # Teste avec un multiple de 3
        number = 3
        result = fcts.fizz_buzz(number)
        expected = 'fizz'
        self.assertEqual(result, expected)

    def test_fizz_buzz_5(self):
        # Teste avec un multiple de 5
        number = 5
        result = fcts.fizz_buzz(number)
        expected = 'buzz'
        self.assertEqual(result, expected)

    def test_fizz_buzz_3_5(self):
        # Teste avec un multiple de 3 et 5
        number = 15
        result = fcts.fizz_buzz(number)
        expected = 'fizzbuzz'
        self.assertEqual(result, expected)

    def test_fizz_buzz_non_facteur(self):
        # Teste avec un number qui n'a pas 3 et 5 comme facteur
        #  et assurez-vous que la valeur en sortie soit une string
        number = 13
        result = fcts.fizz_buzz(number)
        self.assertEqual(result, str(number))

class TestResoudreEquation(TestCase):
    def test_resoudre_equation_sans_racine(self):
        # Teste avec un polynome sans racines réelles
        #  et assurez-vous que la valeur en sortie est None
        a = 4
        b = 1
        c = 4
        result = fcts.resoudre_equation(a, b, c)
        self.assertIsNone(result)

    def test_resoudre_equation_une_racine(self):
        # Teste avec un polynome avec une seule solution
        a = 9
        b = 6
        c = 1
        result = fcts.resoudre_equation(a, b, c)
        expected = -1 / 3
        self.assertEqual(result, expected)

    def test_resoudre_equation_deux_racine(self):
        # Teste avec un polynome avec deux solutions
        a = 1
        b = 7
        c = 6
        result = fcts.resoudre_equation(a, b, c)
        expected = (-1, -6)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
