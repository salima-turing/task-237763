import unittest
from unittest.mock import patch, Mock
import io
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class DecisionMaker:
	def __init__(self, model, threshold=0.5):
		self.model = model
		self.threshold = threshold

	def make_decision(self, input_data):
		probability = self.model.predict_proba(input_data)[:, 1]
		output = "Accept" if probability >= self.threshold else "Reject"
		print(f"Decision: {output}")
		return output

class TestDecisionMaker(unittest.TestCase):

	def setUp(self):
		# Load pre-trained or train a model for testing
		self.model = RandomForestClassifier(random_state=0)
		# Sample data for testing
		self.test_data = pd.DataFrame({
			'feature1': [1, 2, 3, 4, 5],
			'feature2': [10, 20, 30, 40, 50]
		})
		self.test_labels = pd.Series([0, 1, 0, 1, 0])
		self.model.fit(self.test_data, self.test_labels)
		self.decision_maker = DecisionMaker(self.model, threshold=0.6)

	@patch('sys.stdout', new_callable=io.StringIO)
	def test_make_decision_accept(self, mock_stdout):
		input_data = self.test_data.iloc[[3]]  # Data point with high probability of acceptance
		result = self.decision_maker.make_decision(input_data)
		self.assertEqual(result, "Accept")
		self.assertIn("Decision: Accept", mock_stdout.getvalue())

	@patch('sys.stdout', new_callable=io.StringIO)
	def test_make_decision_reject(self, mock_stdout):
		input_data = self.test_data.iloc[[0]]  # Data point with low probability of acceptance
		result = self.decision_maker.make_decision(input_data)
		self.assertEqual(result, "Reject")
		self.assertIn("Decision: Reject", mock_stdout.getvalue())

if __name__ == '__main__':
	unittest.main()
