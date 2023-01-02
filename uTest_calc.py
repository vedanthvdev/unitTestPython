import unittest
import calc


class testCalc(unittest.TestCase):
    def test_add(self):
        self.assertEquals(calc.add(10,4), 14)
        self.assertEquals(calc.add(1,-4), -3)
        self.assertEquals(calc.add(-1,1), 0)
    def test_sub(self):
        self.assertEquals(calc.sub(10,4), 6)
        self.assertEquals(calc.sub(1,-4), 5)
        self.assertEquals(calc.sub(-1,1), -2)
    def test_mul(self):
        self.assertEquals(calc.mul(10,4), 40)
        self.assertEquals(calc.mul(1,-4), -4)
        self.assertEquals(calc.mul(-1,-1), 1)
    def test_div(self):
        self.assertEquals(calc.div(12,4), 3)
        self.assertEquals(calc.div(5,-2), -2.5)
        self.assertEquals(calc.div(-1,-1), 1)
        with self.assertRaises(ValueError):
            calc.div(-1,0)
    

if __name__ == '__main__':
    unittest.main()