import unittest
import arithmetic as file

class TestArithmetic(unittest.TestCase):
    def test_add(self):
        sum = file.add(5,5)
        self.assertEqual(sum,10)
    
    def test_sub(self):
        diff = file.minus(5,5)
        self.assertEqual(diff,0)

    def test_mul(self):
        product = file.multiply(5,5)
        self.assertEqual(product,25)

    def test_div(self):
        quotient = file.divide(5,5)
        self.assertEqual(quotient,1)
        #test exception 
        with self.assertRaises(ValueError):
            file.divide(5,0)

if __name__ == '__main__':
    unittest.main()