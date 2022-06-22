from projeto4_sols import *

import unittest


class TestProj4(unittest.TestCase):

#T1

    def test_t1_1_teamDuels(self):
        d2021 = {'Alfa Romeo Racing': {'GIO': 15, 'RAI': 7, 'KUB': 0}, 'AlphaTauri': {'GAS': 21, 'TSU': 1}, 'Alpine': {'ALO': 11, 'OCO': 11}, 'Aston Martin': {'STR': 8, 'VET': 14}, 'Ferrari': {'LEC': 13, 'SAI': 9}, 'Haas F1 Team': {'MAZ': 2, 'MSC': 20}, 'McLaren': {'NOR': 15, 'RIC': 7}, 'Mercedes': {'BOT': 5, 'HAM': 17}, 'Red Bull Racing': {'PER': 2, 'VER': 20}, 'Williams': {'LAT': 2, 'RUS': 20}}
        self.assertEqual(teamDuels(2021),d2021)

    def test_t1_2_teamDuels(self):
        d2020 = {'Alfa Romeo Racing': {'GIO': 9, 'RAI': 8}, 'AlphaTauri': {'GAS': 13, 'KVY': 4}, 'Ferrari': {'LEC': 13, 'VET': 4}, 'Haas F1 Team': {'GRO': 7, 'MAG': 10, 'FIT': 0}, 'McLaren': {'NOR': 9, 'SAI': 8}, 'Mercedes': {'BOT': 5, 'HAM': 12, 'RUS': 0}, 'Racing Point': {'PER': 11, 'STR': 5, 'HUL': 1}, 'Red Bull Racing': {'ALB': 0, 'VER': 17}, 'Renault': {'OCO': 2, 'RIC': 15}, 'Williams': {'LAT': 1, 'RUS': 16, 'AIT': 0}}
        self.assertEqual(teamDuels(2020),d2020)

if __name__ == '__main__':
    unittest.main(exit=False)

#T2

drawFastestLaps(2021,'Austrian Grand Prix')


