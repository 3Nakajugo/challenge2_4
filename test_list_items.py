import unittest

from add_list_items import add_items


class test_items(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add_items([1,2,3,4]),10)

    def test_list(self):
        self.assertRaises(TypeError,add_items,True)
    
    # def test_int(self):
    #     self.assertRaises(ValueError,add_items,[])
