import numpy as np
import unittest
from risk_mitigation.risk_model import RiskModel

class TestRiskModel(unittest.TestCase):
    def setUp(self):
        self.data = np.array([100, 110, 105, 115, 120])
        self.risk_free_rate = 0.02

    def test_analyze_risk(self):
        risk_model = RiskModel(self.data, self.risk_free_rate)
        result = risk_model.analyze_risk()

        self.assertIsInstance(result, dict)
        self.assertIn("returns", result)
        self.assertIn("volatility", result)
        self.assertIn("sharpe_ratio", result)
        self.assertIn("optimized_weights", result)

        returns = result["returns"]
        volatility = result["volatility"]
        sharpe_ratio = result["sharpe_ratio"]
        optimized_weights = result["optimized_weights"]

        self.assertEqual(len(returns), len(self.data) - 1)
        self.assertIsInstance(volatility, float)
        self.assertIsInstance(sharpe_ratio, float)
        self.assertIsInstance(optimized_weights, np.ndarray)
        self.assertEqual(len(optimized_weights), len(self.data) - 1)

    def test_mitigate_risk(self):
        risk_model = RiskModel(self.data, self.risk_free_rate)
        risk_analysis = risk_model.analyze_risk()
        mitigation_plan = risk_model.mitigate_risk(risk_analysis)

        self.assertIsInstance(mitigation_plan, dict)
        self.assertIn("optimized_weights", mitigation_plan)

        optimized_weights = mitigation_plan["optimized_weights"]

        self.assertIsInstance(optimized_weights, np.ndarray)
        self.assertEqual(len(optimized_weights), len(self.data) - 1)

if __name__ == '__main__':
    unittest.main()
