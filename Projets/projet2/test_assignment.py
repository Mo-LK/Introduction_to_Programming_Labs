import Molecule as molec
import Reservoir as res


import unittest
import os
import sys
import random

class TestMolecule(unittest.TestCase):
    x, y, dx, dy, rayon = 5, 2, -3, 4, 5
    mol_1 = molec.creerMolecule(x, y, dx, dy, rayon)
    random.seed(10)

    def test11_creerMolecule(self):
        mol = molec.creerMolecule(self.x, self.y, self.dx, self.dy, self.rayon)
        result = {'x': 5, 'y': 2, 'dx': -3, 'dy': 4, 'rayon': 5}
        self.assertDictEqual(mol, result)


    # Test moleculesSeTouche
    def test12_moleculeSeTouche1(self):
        mol_2 = self.mol_1
        result = molec.moleculesSeTouche(self.mol_1, mol_2)
        self.assertTrue(result)

    def test12_moleculeSeTouche2(self):
        mol_2 = molec.creerMolecule(self.x, self.y + self.rayon, self.dx, self.dy, self.rayon)
        result = molec.moleculesSeTouche(self.mol_1, mol_2)
        self.assertTrue(result)

    def test12_moleculeSeTouche3(self):
        mol_2 = molec.creerMolecule(self.x + self.rayon, self.y + self.rayon, self.dx, self.dy, self.rayon)
        result = molec.moleculesSeTouche(self.mol_1, mol_2)
        self.assertTrue(result)

    def test12_moleculeSeTouche4(self):
        mol_2 = molec.creerMolecule(self.x + self.rayon, self.y + self.rayon, self.dx, self.dy, self.rayon / 4)
        result = molec.moleculesSeTouche(self.mol_1, mol_2)
        self.assertFalse(result)

    def test12_moleculeSeTouche5(self):
        mol_2 = molec.creerMolecule(self.x + self.rayon, self.y + 2 * self.rayon, self.dx, self.dy, self.rayon)
        result = molec.moleculesSeTouche(self.mol_1, mol_2)
        self.assertFalse(result)

    # Test deplacerMolecule
    def test13_deplacerMolecule(self):
        mol_1 = self.mol_1.copy()
        mol_1 = molec.deplacerMolecule(mol_1)
        mol_2 = {'x': 2, 'y': 6, 'dx': -3, 'dy': 4, 'rayon': 5}
        self.assertDictEqual(mol_1, mol_2)

    # Test creerListMolecules
    def test15_creerListMolecules(self):
        hauteur, xmin, xmax, nbMolecules = 500, 0, 1000, 20
        lm = molec.creerListMolecules(hauteur, xmin, xmax, nbMolecules)
        self.assertEqual(len(lm), nbMolecules)
        for mol in lm:
            self.assertTrue(xmin + mol['rayon'] <= mol['x'] <= xmax - mol['rayon'])
            self.assertTrue(mol['rayon'] <= mol['y'] <= hauteur - mol['rayon'])
            self.assertTrue(10 <= mol['rayon'] <= 30)

    # Test inverseDirMolecule
    def test16_inverseDirMolecule1(self):
        mol = {'x': 2, 'y': 6, 'dx': -3, 'dy': 4, 'rayon': 5}
        mol = molec.inverseDirMolecule(mol, 0, 1000, 1000)
        result = {'x': 5, 'y': 6, 'dx': 3, 'dy': 4, 'rayon': 5}
        self.assertDictEqual(mol, result)

    def test16_inverseDirMolecule2(self):
        mol = {'x': 1100, 'y': 6, 'dx': -3, 'dy': 4, 'rayon': 5}
        mol = molec.inverseDirMolecule(mol, 0, 1000, 1000)
        result = {'x': 995, 'y': 6, 'dx': 3, 'dy': 4, 'rayon': 5}
        self.assertDictEqual(mol, result)

    def test16_inverseDirMolecule3(self):
        mol = {'x': 10, 'y': 1100, 'dx': -3, 'dy': 4, 'rayon': 5}
        mol = molec.inverseDirMolecule(mol, 0, 1000, 1000)
        result = {'x': 10, 'y': 995, 'dx': -3, 'dy': -4, 'rayon': 5}
        self.assertDictEqual(mol, result)

    def test16_inverseDirMolecule4(self):
        mol = {'x': 10, 'y': 0, 'dx': -3, 'dy': 4, 'rayon': 5}
        mol = molec.inverseDirMolecule(mol, 0, 1000, 1000)
        result = {'x': 10, 'y': 5, 'dx': -3, 'dy': -4, 'rayon': 5}
        self.assertDictEqual(mol, result)

    def test16_inverseDirMolecule5(self):
        mol = {'x': 0, 'y': 0, 'dx': -3, 'dy': 4, 'rayon': 5}
        mol = molec.inverseDirMolecule(mol, 0, 1000, 1000)
        result = {'x': 5, 'y': 5, 'dx': 3, 'dy': -4, 'rayon': 5}
        self.assertDictEqual(mol, result)

    def test16_inverseDirMolecule6(self):
        mol = {'x': 20, 'y': 20, 'dx': -3, 'dy': 4, 'rayon': 5}
        mol = molec.inverseDirMolecule(mol, 0, 1000, 1000)
        result = {'x': 20, 'y': 20, 'dx': -3, 'dy': 4, 'rayon': 5}
        self.assertDictEqual(mol, result)


class TestReservoir(unittest.TestCase):
    random.seed(10)

    def test21_creerReservoir(self):
        hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD = 500, 1500, 1000, 20, 10
        reservoir = res.creerReservoir(hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD)
        self.assertEqual(reservoir['h'], hauteur)
        self.assertEqual(reservoir['l'], largeur)
        self.assertEqual(reservoir['posPar'], posParoi)
        self.assertEqual(len(reservoir['mG']), nbMoleculesG)
        self.assertEqual(len(reservoir['mD']), nbMoleculesD)
        self.assertEqual(len(reservoir["lCG"]), nbMoleculesG * (nbMoleculesG - 1) / 2)
        self.assertEqual(len(reservoir["lCD"]), nbMoleculesD * (nbMoleculesD - 1) / 2)

    def test22_colision(self):
        reservoir = {'h': 500, 'l': 1500, 'posPar': 1000, 'mG': [{'x': 755, 'y': 48, 'dx': -5, 'dy': -14, 'rayon': 12}, {'x': 572, 'y': 57, 'dx': 2, 'dy': 21, 'rayon': 14}, {'x': 355, 'y': 242, 'dx': -12, 'dy': -40, 'rayon': 20}, {'x': 755, 'y': 48, 'dx': -10, 'dy': -12, 'rayon': 26}, {'x': 742, 'y': 108, 'dx': 25, 'dy': 19, 'rayon': 16}, {'x': 190, 'y': 395, 'dx': 55, 'dy': 7, 'rayon': 28}, {'x': 769, 'y': 284, 'dx': 2, 'dy': 29, 'rayon': 16}, {'x': 539, 'y': 60, 'dx': -35, 'dy': 6, 'rayon': 28}, {'x': 943, 'y': 229, 'dx': -31, 'dy': 5, 'rayon': 24}, {'x': 624, 'y': 204, 'dx': 16, 'dy': -3, 'rayon': 26}, {'x': 742, 'y': 108, 'dx': 23, 'dy': 8, 'rayon': 24}, {'x': 437, 'y': 436, 'dx': -22, 'dy': -24, 'rayon': 12}, {'x': 572, 'y': 57, 'dx': -42, 'dy': -4, 'rayon': 24}, {'x': 167, 'y': 67, 'dx': 14, 'dy': 5, 'rayon': 12}, {'x': 166, 'y': 258, 'dx': 7, 'dy': 16, 'rayon': 24}, {'x': 375, 'y': 395, 'dx': -15, 'dy': 41, 'rayon': 24}, {'x': 457, 'y': 192, 'dx': 35, 'dy': 18, 'rayon': 24}, {'x': 183, 'y': 404, 'dx': -22, 'dy': -11, 'rayon': 26}, {'x': 61, 'y': 379, 'dx': -31, 'dy': 26, 'rayon': 28}, {'x': 617, 'y': 452, 'dx': 24, 'dy': 5, 'rayon': 28}], 'mD': [{'x': 1423, 'y': 69, 'dx': -2, 'dy': 7, 'rayon': 10}, {'x': 1423, 'y': 69, 'dx': -21, 'dy': -27, 'rayon': 16}, {'x': 1423, 'y': 69, 'dx': -43, 'dy': 48, 'rayon': 28}, {'x': 1101, 'y': 361, 'dx': 25, 'dy': -18, 'rayon': 18}, {'x': 1324, 'y': 225, 'dx': -16, 'dy': 4, 'rayon': 20}, {'x': 1054, 'y': 316, 'dx': -16, 'dy': -1, 'rayon': 14}, {'x': 1065, 'y': 366, 'dx': 7, 'dy': 27, 'rayon': 16}, {'x': 1395, 'y': 242, 'dx': 5, 'dy': 33, 'rayon': 26}, {'x': 1333, 'y': 412, 'dx': 24, 'dy': -6, 'rayon': 26}, {'x': 1333, 'y': 412, 'dx': 16, 'dy': -24, 'rayon': 12}], 'lCG': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'lCD': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        result = {'h': 500, 'l': 1500, 'posPar': 1000, 'mG': [{'x': 755, 'y': 48, 'dx': -5, 'dy': -14, 'rayon': 12}, {'x': 572, 'y': 57, 'dx': -33.34426229508197, 'dy': 24.21311475409836, 'rayon': 14}, {'x': 355, 'y': 242, 'dx': -12, 'dy': -40, 'rayon': 20}, {'x': 755, 'y': 48, 'dx': -10, 'dy': -12, 'rayon': 26}, {'x': 742, 'y': 108, 'dx': 25, 'dy': 19, 'rayon': 16}, {'x': 190, 'y': 395, 'dx': 34.7, 'dy': 33.099999999999994, 'rayon': 28}, {'x': 769, 'y': 284, 'dx': 2, 'dy': 29, 'rayon': 16}, {'x': 539, 'y': 60, 'dx': -41.040983606557376, 'dy': 6.549180327868853, 'rayon': 28}, {'x': 943, 'y': 229, 'dx': -31, 'dy': 5, 'rayon': 24}, {'x': 624, 'y': 204, 'dx': 16, 'dy': -3, 'rayon': 26}, {'x': 742, 'y': 108, 'dx': 23, 'dy': 8, 'rayon': 24}, {'x': 437, 'y': 436, 'dx': -22, 'dy': -24, 'rayon': 12}, {'x': 572, 'y': 57, 'dx': -0.6147540983606561, 'dy': -7.762295081967213, 'rayon': 24}, {'x': 167, 'y': 67, 'dx': 14, 'dy': 5, 'rayon': 12}, {'x': 166, 'y': 258, 'dx': 7, 'dy': 16, 'rayon': 24}, {'x': 375, 'y': 395, 'dx': -15, 'dy': 41, 'rayon': 24}, {'x': 457, 'y': 192, 'dx': 35, 'dy': 18, 'rayon': 24}, {'x': 183, 'y': 404, 'dx': -1.7000000000000028, 'dy': -37.099999999999994, 'rayon': 26}, {'x': 61, 'y': 379, 'dx': -31, 'dy': 26, 'rayon': 28}, {'x': 617, 'y': 452, 'dx': 24, 'dy': 5, 'rayon': 28}], 'mD': [{'x': 1423, 'y': 69, 'dx': -2, 'dy': 7, 'rayon': 10}, {'x': 1423, 'y': 69, 'dx': -21, 'dy': -27, 'rayon': 16}, {'x': 1423, 'y': 69, 'dx': -43, 'dy': 48, 'rayon': 28}, {'x': 1101, 'y': 361, 'dx': 25, 'dy': -18, 'rayon': 18}, {'x': 1324, 'y': 225, 'dx': -16, 'dy': 4, 'rayon': 20}, {'x': 1054, 'y': 316, 'dx': -16, 'dy': -1, 'rayon': 14}, {'x': 1065, 'y': 366, 'dx': 7, 'dy': 27, 'rayon': 16}, {'x': 1395, 'y': 242, 'dx': 5, 'dy': 33, 'rayon': 26}, {'x': 1333, 'y': 412, 'dx': 24, 'dy': -6, 'rayon': 26}, {'x': 1333, 'y': 412, 'dx': 16, 'dy': -24, 'rayon': 12}], 'lCG': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'lCD': [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}
        reservoir = res.colision(reservoir)
        self.assertDictEqual(reservoir, result)

    def test23_inverseDirMolecules(self):
        reservoir = {'h': 200, 'l': 800, 'posPar': 500, 'mG': [{'x': -10, 'y': 172, 'dx': 20, 'dy': 16, 'rayon': 16}, {'x': 550, 'y': 124, 'dx': -21, 'dy': -25, 'rayon': 16}, {'x': 150, 'y': -10, 'dx': 18, 'dy': 14, 'rayon': 20}, {'x': 337, 'y': 220, 'dx': 27, 'dy': 5, 'rayon': 16}, {'x': -10, 'y': -20, 'dx': -19, 'dy': -1, 'rayon': 26}, {'x': 351, 'y': 111, 'dx': -4, 'dy': 44, 'rayon': 24}, {'x': 265, 'y': 132, 'dx': 25, 'dy': 25, 'rayon': 18}, {'x': 365, 'y': 150, 'dx': 22, 'dy': -1, 'rayon': 12}, {'x': 428, 'y': 65, 'dx': 33, 'dy': 9, 'rayon': 22}, {'x': 61, 'y': 106, 'dx': -54, 'dy': 19, 'rayon': 28}], 'mD': [{'x': 684, 'y': 38, 'dx': 10, 'dy': 38, 'rayon': 20}, {'x': 450, 'y': 250, 'dx': -17, 'dy': -10, 'rayon': 20}, {'x': 1020, 'y': 38, 'dx': 7, 'dy': 22, 'rayon': 14}, {'x': 622, 'y': -10, 'dx': -16, 'dy': 6, 'rayon': 10}, {'x': 450, 'y': 167, 'dx': -30, 'dy': 18, 'rayon': 16}], 'lCG': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'lCD': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        result =  {'h': 200, 'l': 800, 'posPar': 500, 'mG': [{'x': 16, 'y': 172, 'dx': -20, 'dy': 16, 'rayon': 16}, {'x': 484, 'y': 124, 'dx': 21, 'dy': -25, 'rayon': 16}, {'x': 150, 'y': 20, 'dx': 18, 'dy': -14, 'rayon': 20}, {'x': 337, 'y': 184, 'dx': 27, 'dy': -5, 'rayon': 16}, {'x': 26, 'y': 26, 'dx': 19, 'dy': 1, 'rayon': 26}, {'x': 351, 'y': 111, 'dx': -4, 'dy': 44, 'rayon': 24}, {'x': 265, 'y': 132, 'dx': 25, 'dy': 25, 'rayon': 18}, {'x': 365, 'y': 150, 'dx': 22, 'dy': -1, 'rayon': 12}, {'x': 428, 'y': 65, 'dx': 33, 'dy': 9, 'rayon': 22}, {'x': 61, 'y': 106, 'dx': -54, 'dy': 19, 'rayon': 28}], 'mD': [{'x': 684, 'y': 38, 'dx': 10, 'dy': 38, 'rayon': 20}, {'x': 520, 'y': 180, 'dx': 17, 'dy': 10, 'rayon': 20}, {'x': 786, 'y': 38, 'dx': -7, 'dy': 22, 'rayon': 14}, {'x': 622, 'y': 10, 'dx': -16, 'dy': -6, 'rayon': 10}, {'x': 516, 'y': 167, 'dx': 30, 'dy': 18, 'rayon': 16}], 'lCG': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'lCD': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        reservoir =  res.inverseDirMolecules(reservoir)
        self.assertDictEqual(reservoir, result)


    def test24_getTemperature(self):
        reservoir = {'h': 200, 'l': 800, 'posPar': 500, 'mG': [{'x': 16, 'y': 172, 'dx': -20, 'dy': 16, 'rayon': 16}, {'x': 484, 'y': 124, 'dx': 21, 'dy': -25, 'rayon': 16}, {'x': 150, 'y': 20, 'dx': 18, 'dy': -14, 'rayon': 20}, {'x': 337, 'y': 184, 'dx': 27, 'dy': -5, 'rayon': 16}, {'x': 26, 'y': 26, 'dx': 19, 'dy': 1, 'rayon': 26}, {'x': 351, 'y': 111, 'dx': -4, 'dy': 44, 'rayon': 24}, {'x': 265, 'y': 132, 'dx': 25, 'dy': 25, 'rayon': 18}, {'x': 365, 'y': 150, 'dx': 22, 'dy': -1, 'rayon': 12}, {'x': 428, 'y': 65, 'dx': 33, 'dy': 9, 'rayon': 22}, {'x': 61, 'y': 106, 'dx': -54, 'dy': 19, 'rayon': 28}], 'mD': [{'x': 684, 'y': 38, 'dx': 10, 'dy': 38, 'rayon': 20}, {'x': 520, 'y': 180, 'dx': 17, 'dy': 10, 'rayon': 20}, {'x': 786, 'y': 38, 'dx': -7, 'dy': 22, 'rayon': 14}, {'x': 622, 'y': 10, 'dx': -16, 'dy': -6, 'rayon': 10}, {'x': 516, 'y': 167, 'dx': 30, 'dy': 18, 'rayon': 16}], 'lCG': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'lCD': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        result_g = 574.6
        temperature_g = res.getTemperature(reservoir, "Gauche")
        self.assertEqual(result_g, temperature_g)
        result_d = 398.2
        temperature_d = res.getTemperature(reservoir, "Droite")
        self.assertEqual(result_d, temperature_d)

    def test26_deplacerMolecules(self):
        reservoir = {'h': 200, 'l': 800, 'posPar': 500, 'mG': [{'x': 16, 'y': 172, 'dx': -20, 'dy': 16, 'rayon': 16}, {'x': 484, 'y': 124, 'dx': 21, 'dy': -25, 'rayon': 16}, {'x': 150, 'y': 20, 'dx': 18, 'dy': -14, 'rayon': 20}, {'x': 337, 'y': 184, 'dx': 27, 'dy': -5, 'rayon': 16}, {'x': 26, 'y': 26, 'dx': 19, 'dy': 1, 'rayon': 26}, {'x': 351, 'y': 111, 'dx': -4, 'dy': 44, 'rayon': 24}, {'x': 265, 'y': 132, 'dx': 25, 'dy': 25, 'rayon': 18}, {'x': 365, 'y': 150, 'dx': 22, 'dy': -1, 'rayon': 12}, {'x': 428, 'y': 65, 'dx': 33, 'dy': 9, 'rayon': 22}, {'x': 61, 'y': 106, 'dx': -54, 'dy': 19, 'rayon': 28}], 'mD': [{'x': 684, 'y': 38, 'dx': 10, 'dy': 38, 'rayon': 20}, {'x': 520, 'y': 180, 'dx': 17, 'dy': 10, 'rayon': 20}, {'x': 786, 'y': 38, 'dx': -7, 'dy': 22, 'rayon': 14}, {'x': 622, 'y': 10, 'dx': -16, 'dy': -6, 'rayon': 10}, {'x': 516, 'y': 167, 'dx': 30, 'dy': 18, 'rayon': 16}], 'lCG': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'lCD': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
        result = {'h': 200, 'l': 800, 'posPar': 500, 'mG': [{'x': 36, 'y': 188, 'dx': 20, 'dy': 16, 'rayon': 16}, {'x': 463, 'y': 99, 'dx': -17.95389507154213, 'dy': 13.076311605723376, 'rayon': 16}, {'x': 168, 'y': 34, 'dx': 18, 'dy': 14, 'rayon': 20}, {'x': 364, 'y': 189, 'dx': 36.4, 'dy': 23.8, 'rayon': 16}, {'x': 7, 'y': 25, 'dx': -19, 'dy': -1, 'rayon': 26}, {'x': 347, 'y': 155, 'dx': -13.4, 'dy': 25.2, 'rayon': 24}, {'x': 290, 'y': 157, 'dx': 25, 'dy': 25, 'rayon': 18}, {'x': 387, 'y': 149, 'dx': 22, 'dy': -1, 'rayon': 12}, {'x': 461, 'y': 74, 'dx': 29.95389507154213, 'dy': -29.076311605723376, 'rayon': 22}, {'x': 7, 'y': 125, 'dx': -54, 'dy': 19, 'rayon': 28}], 'mD': [{'x': 694, 'y': 76, 'dx': 10, 'dy': 38, 'rayon': 20}, {'x': 503, 'y': 170, 'dx': -38.20038910505836, 'dy': 8.706225680933851, 'rayon': 20}, {'x': 793, 'y': 60, 'dx': 7, 'dy': 22, 'rayon': 14}, {'x': 606, 'y': 16, 'dx': -16, 'dy': 6, 'rayon': 10}, {'x': 486, 'y': 185, 'dx': -8.799610894941633, 'dy': -0.7062256809338514, 'rayon': 16}], 'lCG': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'lCD': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]}
        reservoir = res.deplacerMolecules(reservoir)
        self.assertEqual(reservoir, result)

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)