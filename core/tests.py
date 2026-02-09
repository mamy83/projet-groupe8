from django.test import TestCase
from .models import Appliance
from . import utils

class AlgorithmTests(TestCase):
    def test_calculate_energy(self):
        # 100Ah * 12V * 50% = 600Wh
        self.assertEqual(utils.calculate_energy(100, 12, 50), 600)
        # 200Ah * 24V * 100% = 4800Wh
        self.assertEqual(utils.calculate_energy(200, 24, 100), 4800)

    def test_estimate_autonomy(self):
        # 1000Wh / 100W = 10h
        self.assertEqual(utils.estimate_autonomy(1000, 100), 10)
        # Zero load
        self.assertEqual(utils.estimate_autonomy(1000, 0), 99.9)

    def test_get_recommendations_optimal(self):
        appliances = [
            Appliance(name="TV", power_w=60, is_essential=True),
            Appliance(name="Clim", power_w=1500, is_essential=False),
        ]
        recs = utils.get_recommendations(80, appliances)
        self.assertEqual(recs['status'], "OPTIMAL")
        self.assertIn(appliances[0], recs['recommended'])
        self.assertIn(appliances[1], recs['acceptable'])

    def test_get_recommendations_critical(self):
        appliances = [
            Appliance(name="Lampe", power_w=10, is_essential=True),
            Appliance(name="Radio", power_w=100, is_essential=True),
            Appliance(name="TV", power_w=60, is_essential=False),
        ]
        recs = utils.get_recommendations(15, appliances)
        self.assertEqual(recs['status'], "CRITIQUE")
        self.assertIn(appliances[0], recs['recommended']) # Essential and < 50W
        self.assertIn(appliances[1], recs['acceptable'])  # Essential and > 50W
        self.assertIn(appliances[2], recs['avoid'])       # Not essential
