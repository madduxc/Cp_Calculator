#Author:        Charles D. Maddux
#Date:          12/10/2021
#Description:   Test module for verifying function of specific modules in Cp_Calculator.py file

from unittest import TestCase
from unittest import mock
import Cp_Calculator

class TestRocketClass(TestCase):
    """
    verify methods in Rocket class
    """
    def test_rocket_class(self):
        """
        verify values entered int initializer are stored and returned properly
        """
        rocket = Cp_Calculator.Rocket("Test Rocket 1")
        rocket.add_fins(6)
        rocket.add_diameter(2.5)
        rocket.add_component("nose", 2.5)
        rocket.add_component("boattail", 0.75)
        rocket.add_x_bar(12.3)
        rocket.add_x_bar(15)
        rocket.add_Cn_alpha(0.955)
        rocket.add_Cn_alpha(1.1)
        rocket.add_length(2.5)
        rocket.add_length(12.5)
        rocket.add_length(10.1)
        rocket.set_Cna(2.555)
        rocket.set_xBar(12.503)
        self.assertEqual(rocket.get_name(), "Test Rocket 1")
        self.assertEqual(rocket.get_diameter(), 2.5)
        self.assertEqual(rocket.get_num_fins(), 6)
        self.assertEqual(rocket.get_components(), {"nose": 2.5, "boattail": 0.75})
        self.assertEqual(rocket.get_x_bar(), [12.3, 15])
        self.assertEqual(rocket.get_Cn_alpha(), [0.955, 1.1])
        self.assertEqual(rocket.get_length(), 25.1)
        self.assertEqual(rocket.get_Cna(), 2.555)
        self.assertEqual(rocket.get_xBar(), 12.503)

    @mock.patch('Cp_Calculator.input', create=True)
    def test_find_nose_cone(self, mocked_input):
        """
        tests find_nose method for calculating x_bar of conical nose
        :param mocked_input: (patch)
        :return: none
        """
        mocked_input.side_effect = ["Falcon Heavy", '3', '1']
        rocket = Cp_Calculator.initialize_rocket()
        Cp_Calculator.find_nose(rocket)
        self.assertEqual(rocket.get_name(), "Falcon Heavy")
        self.assertEqual(rocket.get_length(), 3)
        self.assertEqual(rocket.get_Cn_alpha(), [2])
        self.assertAlmostEqual(rocket.get_x_bar(), [2.0], 3)

