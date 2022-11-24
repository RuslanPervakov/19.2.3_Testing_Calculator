import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):                     
        self.calc = Calculator         

    def test_addition_calculate_correctly(self):
        assert self.calc.adding(self, 7, 8) == 15

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 3) == 1

    def test_multiplication_calculate_correctly(self):      
        assert self.calc.multiplication(self, 2, 2) == 4    

    def test_division_calculate_correctly(self):
        assert  self.calc.division(self, 8, 4) == 2

    def test_multiplication_calculation_failed(self):       
        assert self.calc.multiplication(self, 2, 2) == 7          
