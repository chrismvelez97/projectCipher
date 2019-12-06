#unit tests for ceaser cipher go here
import unittest

import cipherFunctions as cipher

class TestCipher(unittest.TestCase):

	def test_convertToNum(self):
		self.assertEqual(cipher.messageToNumber("a"),[0],"This should return a list containing numbers.")

	def test_shiftNum(self):
		self.assertEqual(cipher.shiftNumbers([0],2),[2],"This should create a new list with shifted numbers")

	def test_negativeShift(self):
		self.assertEqual(cipher.shiftNumbers([1],-1),[0],"this should shift left")

	def test_Out_Of_Bounds_R(self):
		self.assertEqual(cipher.checkOutOfBounds([27]),[1],"This should subtract the shift by 26")

	def test_Out_Of_Bounds_L(self):
		self.assertEqual(cipher.checkOutOfBounds([-5]),[21],"This should add 26")

if __name__ == "__main__":
	unittest.main()
