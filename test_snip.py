import unittest
import snip

class TestSnip(unittest.TestCase):

	def test_openInput(self):

		file_name = 'example_input.txt'
		lines = snip.openInput(file_name)

		#-> unit test, first line should be integer > 0
		self.assertGreater(int(lines[0]), 0)

		#-> second line should be length > 1 AND first digit equal the number of digits after AND number of digits after all >0 AND <= 4
		self.assertGreater(len(lines[1]), 1)
		self.assertEqual(int(lines[1].split()[0]), len(lines[1].split()[1:]))

		#-> for each line if len(lines[i])==1 then next lines[i+1] should be length > 1 AND first digit equal the number of digits after AND number of digits after all >0 AND <= 4
		for i in range(len(lines)-1):
			if len(lines[i]) == 1:
				self.assertGreater(len(lines[i+1]), 1)
				self.assertEqual(int(lines[i+1].split()[0]), len(lines[i+1].split()[1:]))

				for j in lines[i+1].split()[1:]:
					self.assertGreater(int(j), 0)
					self.assertLessEqual(int(j), 4)

		#-> last line lines[-1] should be 0
		self.assertEqual(int(lines[-1]), 0)

	def test_maxProfit(self):

		self.assertEqual(snip.maxProfit([2, 3, 1]), 3)
		self.assertEqual(snip.maxProfit([1, 2, 1]), 1)
		self.assertEqual(snip.maxProfit([1, 2]), 2)
		self.assertEqual(snip.maxProfit([1, 4]), -1)

	def test_printOrder(self):

		self.assertEqual(snip.printOrder([2, 3, 1]), [[2, 3, 1], [3, 1, 2], [1, 2, 3]])
		self.assertEqual(snip.printOrder([1, 2, 1]), [[1, 2, 1], [2, 1, 1], [1, 1, 2]])
		self.assertEqual(snip.printOrder([1, 2]), [[1, 2], [2, 1]])
		self.assertEqual(snip.printOrder([1, 4]), [[1, 4], [4, 1]])

if __name__ == '__main__':
	unittest.main()