#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutOperators(Koan):

    def test_assignments(self):
        """
        Sometimes we will ask you to fill in the values
        """
        my_var = 5
        self.assertEqual(__, my_var)

    def test_arithmetics_operators(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(__, 1 * 5)
        self.assertEqual(__, 2 ** 2)
        self.assertEqual(__, 4 / 2)
        self.assertEqual(__, 13 % 4)

    def test_comparaison_operators(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertTrue(4 == 3)
        self.assertTrue(4 <= 3)
        self.assertTrue(2 >= 3)
        self.assertTrue(3 != 3)

    def test_membership_operators(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertTrue('hello' in 'world')
        self.assertTrue('hello' not in 'hello world')

    def test_identiy_operators(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertTrue(False is False is True)
