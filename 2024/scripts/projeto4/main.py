# -*- coding: utf-8 -*-

from projeto4 import *

import unittest

class TestProj4(unittest.TestCase):

# T1

    def test_t1_dueloEquipas(self):
        self.assertEqual(dueloEquipas("Hungary","Germany"),('Group Stage', ['Stuttgart']))
        self.assertEqual(dueloEquipas("Spain","Germany"),('Round of 16', ['Cologne', 'Berlin']))
        self.assertEqual(dueloEquipas("Spain","England"),('Quarter finals', ['Stuttgart', 'Düsseldorf']))


# T2


if __name__ == '__main__':
    unittest.main(exit=False)


