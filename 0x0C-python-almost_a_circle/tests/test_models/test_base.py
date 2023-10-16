#!/usr/bin/python3
"""
This modual contains methods to test Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_method(self):
        """
        method to test the id method
        """
        o = Base(12)
        self.assertAlmostEqual(o.id, 12)
        o2 = Base()
        self.assertAlmostEqual(o2.id, 1)

    def test_inst(self):
        """
        Tests Base() instantiation
        """
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 2})
        self.assertEqual(b.id, 2)

    def test_to_json_string_method(self):
        """
        Tests to_json_string() method
        """
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        self.assertEqual(str(e.exception), "to_json_string() missing 1 \
required positional argument: 'list_dictionaries'")
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 10, 'y': 23, 'width': 31, 'id': 52,
             'height': 40}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{"foo": 9}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foo": 9}]')
        d = [{"foo": 8}, {"abc": 123}, {"hi": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foo": 8}, {"abc": 123}, {"hi": 0}]')
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 11, 'y': 2, 'width': 31, 'id': 5,
             'height': 30}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d), '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d), '[{}, {}]')
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)


if __name__ == "__main__":
    unittest.main()
