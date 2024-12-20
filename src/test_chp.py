import chp

import unittest


class Tests(unittest.TestCase):
    def test_chp(self):
        self.assertEqual(chp.calculate_hidden_power("h31a34d35s35sa34sd38"), "Electric")
        self.assertEqual(chp.calculate_hidden_power("h35a35d41s41sa41sd35.88"), "Steel")
        self.assertEqual(chp.calculate_hidden_power("123"), "Error")
