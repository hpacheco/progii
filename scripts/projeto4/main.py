from projeto4 import *

import unittest


class TestProj4(unittest.TestCase):

#T1

    def test_t1_0_teamDuels(self):
        d2020 = {'Alfa Romeo Racing': {'GIO': 9, 'RAI': 8}, 'AlphaTauri': {'GAS': 13, 'KVY': 4},
             'Ferrari': {'LEC': 13, 'VET': 4}, 'Haas F1 Team': {'GRO': 7, 'MAG': 10, 'FIT': 0},
             'McLaren': {'NOR': 9, 'SAI': 8}, 'Mercedes': {'BOT': 5, 'HAM': 12, 'RUS': 0},
             'Racing Point': {'PER': 11, 'STR': 5, 'HUL': 1}, 'Red Bull Racing': {'ALB': 0, 'VER': 17},
             'Renault': {'OCO': 2, 'RIC': 15}, 'Williams': {'LAT': 1, 'RUS': 16, 'AIT': 0}}
        self.assertEqual(teamDuels(2020), d2020)

    def test_t1_1_teamDuels(self):
        d2021 = {'Alfa Romeo Racing': {'GIO': 15, 'RAI': 7, 'KUB': 0}, 'AlphaTauri': {'GAS': 21, 'TSU': 1}, 'Alpine': {'ALO': 11, 'OCO': 11}, 'Aston Martin': {'STR': 8, 'VET': 14}, 'Ferrari': {'LEC': 13, 'SAI': 9}, 'Haas F1 Team': {'MAZ': 2, 'MSC': 20}, 'McLaren': {'NOR': 15, 'RIC': 7}, 'Mercedes': {'BOT': 5, 'HAM': 17}, 'Red Bull Racing': {'PER': 2, 'VER': 20}, 'Williams': {'LAT': 2, 'RUS': 20}}
        self.assertEqual(teamDuels(2021),d2021)

    def test_t1_2_teamDuels(self):
        d2022 = {'Alfa Romeo': {'BOT': 14, 'ZHO': 8}, 'AlphaTauri': {'GAS': 13, 'TSU': 9}, 'Alpine': {'ALO': 12, 'OCO': 10},
 'Aston Martin': {'HUL': 1, 'STR': 8, 'VET': 13}, 'Ferrari': {'LEC': 15, 'SAI': 7},
 'Haas F1 Team': {'MAG': 16, 'MSC': 6}, 'McLaren': {'NOR': 20, 'RIC': 2}, 'Mercedes': {'HAM': 13, 'RUS': 9},
 'Red Bull Racing': {'PER': 4, 'VER': 18}, 'Williams': {'ALB': 19, 'LAT': 2, 'DEV': 1}}
        self.assertEqual(teamDuels(2022),d2022)




# uncomment for testing T1
#if __name__ == '__main__':
#    unittest.main(exit=False)

#T2

# uncomment for running T2
#drawFastestLaps(2021,'Austrian Grand Prix')

