import unittest
from my_app.main_v1_1 import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(1,4),5)

if __name__=='__main__':
    unittest.main()