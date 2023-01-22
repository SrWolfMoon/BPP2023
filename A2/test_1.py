import unittest
import functions

class pruebasUnitarias(unittest.TestCase):
    def test_getArea(self):
        self.assertEqual(functions.getArea(10),100)
        
    def test_getAreaRect(self):
        self.assertEqual(functions.getArea(10,5), 50)
        
    def test_getPerim(self):
        self.assertEqual(functions.getPerimeter(10), 40)
        
    def test_getPerimRect(self):
        self.assertEqual(functions.getPerimeter(10,1,1,1), 13)
        
    def test_getPerim_With_Negative_Param(self):
        self.assertEqual(functions.getPerimeter(10,-1,10,10), "No puede haber una figura con un lado negativo")
        

if __name__ == '__main__':
    unittest.main()