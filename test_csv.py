import unittest
from state_count import *
from highest_in_state import *
from closest_university import *


class TestCSV(unittest.TestCase):
    def test(self):
        tests = []
        tests.append(['AK', 9])
        tests.append(['TX', 446])
        tests.append(['AL', 94])
        tests.append(['OK', 129])
        tests.append(['CA', 716])
        tests.append(['FL', 412])
        tests.append(['NY', 452])

        for test in tests:
            exp = test[1]
            act = state_count(test[0])
            self.assertEqual(
                exp, act, "state_count('" + test[0] + "') incorrect")

    def test_highest_in_state(self):
        tests = []
        tests.append(['AK', 20760, 'Alaska Pacific University'])
        tests.append(['TX', 52498, 'Southern Methodist University'])
        tests.append(['NJ', 50554, 'Stevens Institute of Technology'])
        tests.append(['OR', 54200, 'Reed College'])
        tests.append(['NV', 32639, 'Sierra Nevada College'])

        for test in tests:
            expValue = test[1]
            expName = test[2]
            self.assertEqual((expValue, expName), highest_in_state(test[0]))

    def test_closest(self):
        tests = []
        # Seven Lakes HS
        tests.append([(15.885002, 'Fortis College'), (29.707459, -95.8101941)])

        # Statue of Liberty
        tests.append([(3.3121172, 'Mildred Elley-New York Campus'),
                      (40.6892534, -74.0466891)])

        # Golden Gate Bridge
        tests.append([(2.233386, 'Presidio Graduate School'),
                      (37.8199286, -122.4804438)])

        for test in tests:
            closest = closest_university(test[1])
            self.assertEqual(test[0][1], closest[1])
            self.assertAlmostEqual(test[0][0], closest[0], 4)
