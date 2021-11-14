import unittest
import itertools

from Matrix import SubMatrices

class TestUser(unittest.TestCase):

    def setUp(self) -> None:
        self.m1 = [[ 5, 6, 7, 8],
                   [10,11,12,13],
                   [21,22,23,24],
                   ]
    
    def test_size(self):
        m = self.m1
        k = 2
        sm = SubMatrices(m, k)
        self.assertEqual((4,3),sm.get_size())
    
    def test_get_sub_01(self):
        m = self.m1
        k = 2
        subm = [[ 5, 6],
                [10,11],
                ]
        origin = (0,0)
        sm = SubMatrices(m, k)
        self.assertEqual(subm, sm.get_sub(origin))

    def test_get_sub_02(self):
        m = self.m1
        k = 2
        subm = [[11,12],
                [22,23],
                ]
        origin = (1,1)
        sm = SubMatrices(m, k)
        self.assertEqual(subm, sm.get_sub(origin))

    def test_all_subs_01(self):
        m = self.m1
        k = 3
        #m = 4
        #n = 3
        subm1 = [[ 5, 6, 7],
                 [10,11,12],
                 [
                     
                     21,22,23],
                ]

        subm2 = [[ 6, 7, 8],
                 [11,12,13],
                 [22,23,24],
                ]
        sm = SubMatrices(m, k)
        sm.update_all_subs()
        sm1 = sm.get_all_subs()[0]
        sm2 = sm.get_all_subs()[1]
        self.assertEqual(subm1, sm1)
        self.assertEqual(subm2, sm2)
     
if __name__ == '__main__':
    unittest.main()
