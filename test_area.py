from unittest import TestCase
import area

class TestShapeAreas(TestCase):

    def test_triangle_area(self):
        result = area.triangle_area(4,5)
        self.assertEqual(10, result)

    def test_triangle_area_floating_point(self):
        self.assertAlmostEqual(17.79875, area.triangle_area(7.25, 4.91))

    def test_triangle_negative_height_base_raises_value_exception(self):
        with self.assertRaises(ValueError):
            area.triangle_area(9, -10)
        
        with self.assertRaises(ValueError):
            area.triangle_area(-9, 10)
        
        with self.assertRaises(ValueError):
            area.triangle_area(-9, -10)

    def test_triangle_base_or_height_of_zero(self):
        self.assertEqual(0, area.triangle_area(0, 8))
        self.assertEqual(0, area.triangle_area(8, 0))
        self.assertEqual(0, area.triangle_area(0, 0))

        

