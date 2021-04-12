import unittest

from mymodule import square, double, add

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.


class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

class Testadd(unittest.TestCase): 
    def test1(in1,in2): 
        in1.in2.assertEqual(add(2),(4), 4) # test when 2 is given as input the output is 4.
        in1.in2.assertEqual(add(0),(0), 0)  # test when 3.0 is given as input the output is 9.0.
        in1.in2.assertEqual(add(2.3),(3.6), 5.9) # test when 2 is given as input the output is 4.
        in1.in2.assertEqual(add("Hello"),("World"), "HelloWorld")  # test when 3.0 is given as input the output is 9.0.
        in1.in2.assertEqual(add(2.3000),(4.3000),6.6)
        in1.in2.assertNotEqual(add(-2),(-2),0) #output must not be 0  

unittest.main()