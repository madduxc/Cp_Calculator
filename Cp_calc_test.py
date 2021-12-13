#Author:        Charles D. Maddux
#Date:          12/10/2021
#Description:   Test module for verifying function of specific modules in Cp_Calculator.py file

import unittest
from Cp_Calculator import *

class TestRocketClass(unittest.TestCase):
    """
    verify methods in Rocket class
    """
    def test_initialize_rocket(self):
        """
        verify values entered int initializer are stored and returned properly
        """
        rocket = Rocket("Test Rocket", 6)
        rocket.add_component("nose", 2.5)
        rocket.add_component("boattail", 0.75)
        rocket.add_x_bar(12.3)
        rocket.add_x_bar(15)
        rocket.add_Cn_alpha(0.955)
        rocket.add_Cn_alpha(1.1)
        self.assertEqual(rocket.get_name(), "Test Rocket")
        self.assertEqual(rocket.get_num_fins(), 6)
        self.assertEqual(rocket.get_components(), {"nose": 2.5, "boattail": 0.75})
        self.assertEqual(rocket.get_x_bar(), [12.3, 15])
        self.assertEqual(rocket.get_Cn_alpha(), [0.955, 1.1])
