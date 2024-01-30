import unittest

def foo(x,y):
    return x/y

class TestFoo(unittest.TestCase):

    def testWorks1(self):
        result = foo(10,2)
        self.assertEqual(result,5)

    def testDivideByZero(self):
        with self.assertRaises(ValueError):
            foo(5,0)



if __name__ == '__main__':
    unittest.main()
