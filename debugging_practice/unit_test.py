import unittest
from get_name import get_name

class GetNameTestCase(unittest.TestCase):

	def test_first_last_name(self):
		combined_name = get_name('marwan', 'bit')
		self.assertEqual(combined_name, 'Marwan Bit')


get_name('marwan', 'bit')
unittest.main()