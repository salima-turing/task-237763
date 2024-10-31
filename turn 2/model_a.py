import unittest
from unittest.mock import patch, Mock
import io
import pandas as pd
from sklearn.linear_model import LogisticRegression

class DecisionMaker:
	def __init__(self, model, threshold=0.5):
		self.model = model
		self.threshold = threshold

	def make_decision(self, input_data):
		prediction = self.model.predict_proba(input_data)[:, 1]
		output = "Accept" if prediction >= self.threshold else "Reject"
		print(f"Decision: {output}")
		return output

class TestDecisionMaker(unittest.TestCase):

	def setUp(self):
		# Create a mock machine learning model
		self.mock_model = Mock()
		self.mock_model.predict_proba.return_value = [[0.8], [0.3]]

		self.decision_maker = DecisionMaker(model=self.mock_model, threshold=0.6)

	@patch('sys.stdout', new_callable=io.StringIO)
	def test_make_decision_accept(self, mock_stdout):
		input_data = pd.DataFrame({'feature1': [1], 'feature2': [2]})
		result = self.decision_maker.make_decision(input_data)

		self.mock_model.predict_proba.assert_called_once_with(input_data)
		self.assertEqual(result, "Accept")
		self.assertIn("Decision: Accept", mock_stdout.getvalue())

	@patch('sys.stdout', new_callable=io.StringIO)
	def test_make_decision_reject(self, mock_stdout):
		# Update mock model prediction to below threshold
		self.mock_model.predict_proba.return_value = [[0.4]]
		input_data = pd.DataFrame({'feature1': [3], 'feature2': [4]})
		result = self.decision_maker.make_decision(input_data)

		self.mock_model.predict_proba.assert_called_once_with(input_data)
		self.assertEqual(result, "Reject")
		self.assertIn("Decision: Reject", mock_stdout.getvalue())

if __name__ == '__main__':
	unittest.main()
