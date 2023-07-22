import unittest
from add import add

class TestCaseAdd(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(50,50),100)



    # def test_subtract(result):
    #     result = modulecheck.subtract(5,2)
    #     assert result == 3