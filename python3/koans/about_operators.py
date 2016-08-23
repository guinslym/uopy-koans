#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutOperators(Koan):

    def test_assignment_operator(self):
        """
        Assume this variable holds a value
        """
        my_var = 5
        self.assertEqual(__, my_var)

    def test_multiple_assignments(self):
        """
        multiple assignments
        """
        a, b, c = 5, 6, 8
        self.assertEqual(__, b)

    def test_arithmetics_operators(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(__, 1 * 5)
        self.assertEqual(__, 2 ** 2)
        self.assertEqual(__, 4 / 2)
        self.assertEqual(__, 13 % 4)
        self.assertEqual(__, 7 // 4)

    def test_increment_operator(self):
        """
        those are operator assignments also

        It adds right operand to the left operand
        and assign the result to left operand.
        """
        a = 5
        self.assertEqual(__, a)

        a += 1
        self.assertEqual(__, a)

        a = 5
        a -= 1
        self.assertEqual(__, a)

        a = 5
        a *= 2
        self.assertEqual(__, a)

        a = 8
        a /= 2
        self.assertEqual(__, a)

        a = 7
        a %= 2
        self.assertEqual(__, a)


    def test_comparaison_operators(self):
        """
        These operators compare the values on either sides
        of them and decide the relation among them.
        They are also called Relational operators.
        """
        self.assertTrue(__ == 3)
        self.assertTrue(__ < 3)
        self.assertTrue(__ <= 3)
        self.assertTrue(__ >= 3)
        self.assertTrue(__ > 3)
        self.assertTrue(__ != 3)
        self.assertTrue(__ <> 3)

    def test_membership_operators(self):
        """
        Python’s membership operators test for membership
         in a sequence, such as strings, lists, or tuples.
        """
        university = 'Morisset'
        self.assertTrue('library' in university )

        countries = ['USA', 'Nepal', 'Albany']
        self.assertTrue('hello' in countries)

        greeting = 'hello world'
        self.assertTrue('hello' not in greeting)

    def test_identity_operators(self):
        """
        Identity operators compare the memory locations of two objects
        """

        director = False
        self.assertTrue(director is True)

        course = "Geography"
        my_program = __
        self.assertTrue(__ is course)

    def test_priority_of_operators(self):
        """
        Test operator precedence
        """

        self.assertTrue(False is True)

        statement = False is False is False
        self.assertTrue(__)

        statement_2 = (False is False) is False
        self.assertTrue(__)
