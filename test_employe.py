import unittest
from unittest.mock import patch
from employe import Employe

class testemploye(unittest.TestCase):

    # def setUP(self):
    #     self.emp1 = Employe('john', 'lenon', 50)
    #     self.emp2 = Employe('wick', 'onion', 54)

    def setUp(self):
        self.emp1 = Employe('john', 'lenon', 50)
        self.emp2 = Employe('wick', 'onion', 54)    
          
    def tearDown(self):
        print('teardownnnn')

    def test_email(self):

        self.assertEqual(self.emp1.email, 'john.lenon@gmail.com')
        self.assertEqual(self.emp2.email, 'wick.onion@gmail.com')

        self.emp1.first = 'lenon'
        self.emp2.first = 'onion'

        self.assertEqual(self.emp1.email, 'lenon.lenon@gmail.com')
        self.assertEqual(self.emp2.email, 'onion.onion@gmail.com')



    def test_fullname(self):

        self.assertEqual(self.emp1.full_name, 'john lenon')
        self.assertEqual(self.emp2.full_name, 'wick onion')

        self.emp1.first = 'lenon'
        self.emp2.first = 'onion'

        self.assertEqual(self.emp1.full_name, 'lenon lenon')
        self.assertEqual(self.emp2.full_name, 'onion onion')


    def test_payraise(self):

        self.emp1.pay_raise() 
        self.emp2.pay_raise()

        self.assertAlmostEqual(self.emp1.pay, 55)
        self.assertAlmostEqual (self.emp2.pay, 59.4) 


    def test_monthly(self):
        with patch('employe.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            month = self.emp1.monthly_schedule('April')
            mocked_get.assert_called_with('http://company.com/lenon/April')
            self.assertEqual(month, 'Success')

            mocked_get.return_value.ok = False


            month = self.emp2.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/onion/May')
            self.assertEqual(month, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()