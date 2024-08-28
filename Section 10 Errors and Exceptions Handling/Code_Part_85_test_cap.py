import unittest
import Code_Part_85_cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text='python'
		result=Code_Part_85_cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multiple_words(self):
		text='monty python'
		result=Code_Part_85_cap.cap_text(text)
		self.assertEqual(result,'Monty Python')

if __name__=='__main__':
	unittest.main()
			

