#!/usr/bin/python3
"""
Unit test for the Square class
"""

import unittest
import json
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Sqare class
    """

    def tearDown(self):
        """
        Reset the nb_sects
        """
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(Square.__doc__)

    def test_documentation(self):
        """
        Test to see if documentation is correct and created
        """
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "create"))
        self.assertTrue(Square.create.__doc__)
        self.assertTrue(hasattr(Square, "to_json_string"))
        self.assertTrue(Square.to_json_string.__doc__)
        self.assertTrue(hasattr(Square, "from_json_string"))
        self.assertTrue(Square.from_json_string.__doc__)
        self.assertTrue(hasattr(Square, "save_to_file"))
        self.assertTrue(Square.save_to_file.__doc__)
        self.assertTrue(hasattr(Square, "load_from_file"))
        self.assertTrue(Square.load_from_file.__doc__)

    def test_rectangle_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/square.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_empty(self):
        """
        Test for an empty instantiation
        """
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_more_arguments(self):
        """
        Test for an instantiation with 1 more argument
        """
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, 1, 1, 1)

    def test_correct_inst(self):
        """
        Test for a correct instantiation
        """
        s1 = Square(3, 1, 2, 45)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 45)

    def test_default_square(self):
        """
        Test for a default square
        """
        s = Square(1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_str_rep(self):
        """
        Test for string representation of a square.
        """
        s1 = Square(3, 1, 2, 45)
        self.assertEqual(s1.__str__(), "[Square] (45) 1/2 - 3")

    def test_size_setter(self):
        """
        Test for size setter of square class
        """
        s1 = Square(3, 1, 2, 45)
        s1.size = 27
        self.assertEqual(s1.size, 27)

    def test_update(self):
        """
        Test for update method of square
        """
        s1 = Square(3, 1, 2, 45)
        s1.update(12, 5, 5, 8)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 8)
        self.assertEqual(s1.id, 12)
        s1.update(23)
        self.assertEqual(s1.id, 23)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 8)
        s1.update(y=4, x=12, size=8, id=6)
        self.assertEqual(s1.size, 8)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 6)
        s1.update(x=1)
        self.assertEqual(s1.x, 1)
        s1.update(6, x=23)
        self.assertEqual(s1.id, 6)
        self.assertEqual(s1.x, 1)

    def test_update_error(self):
        """
        Testing the update with invalid arguments
        """
        s = Square(1)
        s.update()
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size='3')

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x={'a': 1})

        with self.assertRaises(TypeError) as context:
            s.update(y=[31])
        self.assertIn('y must be an integer', str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.update(size=0)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.update(size=-20)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.update(x=-30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.update(y=-80)
        self.assertIn('y must be >= 0', str(context.exception))

    def test_to_dict(self):
        """
        Test for to dictionary function.
        """
        s1 = Square(3, 1, 2, 45)
        s1_d = s1.to_dictionary()
        self.assertDictEqual(s1_d, {'x': 1, 'size': 3, 'id': 45, 'y': 2})
