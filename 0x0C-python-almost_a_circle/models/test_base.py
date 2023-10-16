#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(inittest.TestCase):

    def test_id(self):
        o = Base(12)
        self.assertAlmostEqual(Base.id, 12)
        o2 = base()
        self.assertAlmostEqual(Base.id, 2)
