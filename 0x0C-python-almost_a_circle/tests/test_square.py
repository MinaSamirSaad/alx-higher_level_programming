#!/usr/bin/python3
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def tearDown(self):
        Base._Base__nb_objects = 0

    def test_no_docstring(self):
        self.assertIsNotNone(Square.__doc__)

    def test_structure(self):
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "size"))
        self.assertIsNotNone(Square.size.__doc__)
        self.assertTrue(hasattr(Square, "width"))
        self.assertIsNotNone(Square.width.__doc__)
        self.assertTrue(hasattr(Square, "height"))
        self.assertIsNotNone(Square.height.__doc__)
        self.assertTrue(hasattr(Square, "x"))
        self.assertIsNotNone(Square.x.__doc__)
        self.assertTrue(hasattr(Square, "y"))
        self.assertIsNotNone(Square.y.__doc__)
        self.assertTrue(hasattr(Square, "update"))
        self.assertIsNotNone(Square.update.__doc__)
        self.assertTrue(hasattr(Square, "area"))
        self.assertIsNotNone(Square.area.__doc__)
        self.assertTrue(hasattr(Square, "display"))
        self.assertIsNotNone(Square.display.__doc__)
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_square_initialize(self):
        self.assertIsNotNone(Square(2))

    def test_square_missing_arguments(self):
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 5)

    def test_square_init(self):
        r1 = Square(2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Square(1, 2, 3)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 1)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 2)

        r3 = Square(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 1)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, 3)
        self.assertEqual(r3.id, 4)

        r4 = Square(10, 20)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 10)
        self.assertEqual(r4.x, 20)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r4.id, 3)

    def test_square_size_width(self):
        r1 = Square(1)
        self.assertEqual(r1.size, 1)
        self.assertGreater(r1.size, 0)
        self.assertIs(type(r1.size), int)
        self.assertRaises(TypeError, Square, 1.1)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)

    def test_square_size_height(self):
        r1 = Square(2)
        self.assertEqual(r1.height, 2)
        self.assertGreater(r1.height, 0)
        self.assertIs(type(r1.height), int)
        self.assertRaises(TypeError, Square, 1.1)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)

    def test_square_x(self):
        self.assertEqual(Square(1).x, 0)
        self.assertEqual(Square(1, 3).x, 3)
        self.assertGreaterEqual(Square(1, 3).x, 0)
        self.assertGreaterEqual(Square(1, 0).x, 0)
        self.assertIs(type(Square(1, 3).x), int)
        self.assertRaises(TypeError, Square, 2, 1.1)
        self.assertRaises(ValueError, Square, 2, -1)

    def test_square_y(self):
        self.assertEqual(Square(1, 2).y, 0)
        self.assertEqual(Square(1, 2, 3).y, 3)
        self.assertGreaterEqual(Square(1, 2, 3).y, 0)
        self.assertGreaterEqual(Square(1, 2, 0).y, 0)
        self.assertIs(type(Square(1, 2, 3).y), int)
        self.assertRaises(TypeError, Square, 2, 1, 2.2)
        self.assertRaises(ValueError, Square, 2, 1, -1)

    def test_square_update(self):
        r1 = Square(1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.id, 1)
        r1.update()
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r1.update(10)
        self.assertEqual(r1.id, 10)
        r1.update(20, 30)
        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.size, 30)
        r1.update(30, 40, 50)
        self.assertEqual(r1.id, 30)
        self.assertEqual(r1.width, 40)
        self.assertEqual(r1.height, 40)
        self.assertEqual(r1.size, 40)
        self.assertEqual(r1.x, 50)
        r1.update(40, 50, 60, 70)
        self.assertEqual(r1.id, 40)
        self.assertEqual(r1.width, 50)
        self.assertEqual(r1.height, 50)
        self.assertEqual(r1.size, 50)
        self.assertEqual(r1.x, 60)
        self.assertEqual(r1.y, 70)
        r1.update(60, 70, 80, 90, 100, id=10, width=20)
        self.assertEqual(r1.id, 60)
        self.assertEqual(r1.width, 70)
        self.assertEqual(r1.height, 70)
        self.assertEqual(r1.size, 70)
        self.assertEqual(r1.x, 80)
        self.assertEqual(r1.y, 90)
        r1.update(70, id=10, width=20)
        self.assertNotEqual(r1.id, 10)
        self.assertEqual(r1.id, 70)
        self.assertNotEqual(r1.width, 20)

        r1.update(id=10, width=20)
        self.assertEqual(r1.id, 10)
        self.assertNotEqual(r1.id, 70)
        self.assertEqual(r1.width, 20)
        self.assertNotEqual(r1.width, 70)

        r1.update(hight=30)
        self.assertEqual(r1.height, 70)
        self.assertNotEqual(r1.height, 30)

        r1.update(x=5, y=6, id=100, size=200)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 200)
        self.assertEqual(r1.height, 200)
        self.assertEqual(r1.size, 200)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)

        r1.update(x=5, xx=8, y=6, id=100, width=200, height=3, size=50)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 50)
        self.assertEqual(r1.height, 50)
        self.assertEqual(r1.size, 50)
        self.assertEqual(r1.x, 5)
        self.assertNotEqual(r1.x, 8)
        self.assertEqual(r1.y, 6)

    def test_rectangle_area(self):
        r1 = Square(10)
        self.assertEqual(r1.area(), 100)
        r1.update(1, 100, 20, 5)
        self.assertEqual(r1.area(), 10000)
        r1.size = 5
        self.assertEqual(r1.area(), 25)

    @staticmethod
    def capture_our_buffer(obj, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        buffer = io.StringIO()
        sys.stdout = buffer
        if method == "print":
            print(obj)
        elif method == "display":
            obj.display()
        sys.stdout = sys.__stdout__
        return buffer

    def test_square_display_width_height(self):
        r1 = Square(2)
        buffer = TestSquare.capture_our_buffer(r1, "display")
        self.assertEqual("##\n##\n", buffer.getvalue())

    def test_square_display_width_height_x(self):
        r1 = Square(2, 2)
        buffer = TestSquare.capture_our_buffer(r1, "display")
        self.assertEqual("  ##\n  ##\n", buffer.getvalue())

    def test_square_display_width_height_x_y(self):
        r1 = Square(2, 2, 4)
        buffer = TestSquare.capture_our_buffer(r1, "display")
        self.assertEqual("\n\n\n\n  ##\n  ##\n", buffer.getvalue())

    def test_square__str__(self):
        r1 = Square(20)
        self.assertEqual("[Square] (1) 0/0 - 20", r1.__str__())
        r1 = Square(30, 3)
        self.assertEqual("[Square] (2) 3/0 - 30", r1.__str__())
        r1 = Square(40, 3, 4)
        self.assertEqual("[Square] (3) 3/4 - 40", r1.__str__())
        r1 = Square(22, 33, 44, 55)
        self.assertEqual("[Square] (55) 33/44 - 22", r1.__str__())

    def test_square_print(self):
        r1 = Square(2, 4, 5)
        buffer = TestSquare.capture_our_buffer(r1, "print")
        self.assertEqual("[Square] (1) 4/5 - 2\n", buffer.getvalue())

        r1 = Square(22)
        buffer = TestSquare.capture_our_buffer(r1, "print")
        self.assertEqual("[Square] (2) 0/0 - 22\n", buffer.getvalue())

    def test_square_to_dictionary(self):
        r1_dict = Square(1, 3, 4, 5).to_dictionary()
        test_dict = {'id': 5, 'size': 1, 'x': 3, 'y': 4}
        self.assertEqual(test_dict, r1_dict)

        r1_dict = Square(10, 30, 44).to_dictionary()
        test_dict = {'id': 1, 'size': 10, 'x': 30, 'y': 44}
        self.assertEqual(test_dict, r1_dict)

        r1_dict = Square(10, 22).to_dictionary()
        test_dict = {'id': 2, 'size': 10, 'x': 22, 'y': 0}
        self.assertEqual(test_dict, r1_dict)
