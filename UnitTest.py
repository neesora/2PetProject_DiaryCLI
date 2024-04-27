import unittest
from diaryMain import Diary

#You always create  a child class derived from unittest.TestCase
class testDiary(unittest.TestCase):
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.diary = Diary()
     #Each test method starts with the keyword test_
    def test_append(self):
        self.assertEqual(self.diary.append("Jojo", "Jojo"), "LMAO")
# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()