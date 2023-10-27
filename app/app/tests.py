from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        result = calc.add(2,3)
        self.assertEquals(result, 5)
    
    def test_substract_numbers(self):
        res = calc.substract(10, 15)
        self.assertEquals(res, 5)
