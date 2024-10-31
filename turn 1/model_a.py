import unittest
from unittest.mock import patch, Mock
import io

class DecisionMaker:
	def __init__(self, threshold=0.5):
		self.threshold = threshold

	def make_decision(self, input_data):
		probability = input_data.get('probability', 0)
		output = "Accept" if probability >= self.threshold else "Reject"
		print(f"Decision: {output}")
		return output

class TestDecisionMaker(unittest.TestCase):

	def setUp(self):
		self.decision_maker = DecisionMaker(threshold=0.6)

	@patch('sys.stdout', new_callable=io.StringIO)
	def test_make_decision_accept(self, mock_stdout):
		input_data = {'probability': 0.7}
		result = self.decision_maker.make_decision(input_data)
		self.assertEqual(result, "Accept")
		self.assertIn("Decision: Accept", mock_stdout.getvalue())

	@patch('sys.stdout', new_callable=io.StringIO)
	def test_make_decision_reject(self, mock_stdout):
		input_data = {'probability': 0.5}
		result = self.decision_maker.make_decision(input_data)
		self.assertEqual(result, "Reject")
		self.assertIn("Decision: Reject", mock_stdout.getvalue())

if __name__ == '__main__':
	unittest.main()
