import unittest
from testing import get_formatted_name

class GetNameTestCase(unittest.TestCase):

	def test_first_last_name(self):
		combined_name = get_formatted_name('marwan', 'bit')
		self.assertEqual(combined_name, 'Marwan Bit')


unittest.main()