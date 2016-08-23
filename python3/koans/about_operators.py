#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutOperators(Koan):

    def test_assignment_operator(self):
        """
        Assume this variable holds a value
        """
        my_var = 5
        self.assertEqual(5, my_var)

    def test_multiple_assignments(self):
        """
        multiple assignments
        """
        a, b, c = 5, 6, 8
        self.assertEqual(6, b)

    def test_arithmetics_operators(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(5, 1 * 5)
        self.assertEqual(4, 2 ** 2)

        self.assertEqual(2, 4 / 2)
        self.assertEqual(1, 7 // 4)

        self.assertEqual(3.25, 13 / 4)
        self.assertEqual(1, 13 % 4)

    def test_increment_operator(self):
        """
        those are operator assignments also

        It adds right operand to the left operand
        and assign the result to left operand.
        """
        a = 5
        self.assertEqual(5, a)

        a += 1
        self.assertEqual(6, a)

        a = 5
        a -= 1
        self.assertEqual(4, a)

        a = 5
        a *= 2
        self.assertEqual(10, a)

        a = 8
        a /= 2
        self.assertEqual(4, a)

        a = 7
        a %= 2
        self.assertEqual(1, a)


    def test_comparaison_operators(self):
        """
        These operators compare the values on either sides
        of them and decide the relation among them.

        Comparaison operator always return a Boolean (True/False)
        """
        self.assertTrue(3 == 3)

        #change the value of the variable 'number'
        number = 2
        self.assertTrue(number < 3)

        #change the value of the variable 'number'
        number = 3
        self.assertTrue(number <= 3)

        #change the value of the variable 'number'
        number = 3
        self.assertTrue(number >= 3)

        #change the value of the variable 'number'
        number = 7
        self.assertTrue(number > 3)

        #change the value of the variable 'number'
        number = 2
        self.assertTrue(number != 3)

    def test_membership_operators(self):
        """
        Python’s membership operators test for membership
         in a sequence, such as strings, lists, or tuples.

        Membership operators always return a Boolean (True/False)
        """
        #change the value of the variable 'university'
        university = 'Morisset library'
        self.assertTrue('library' in university )

        #change the value of the variable 'countries'
        countries = ['USA', 'Nepal', 'Albany', 'Canada']
        self.assertTrue('Canada' in countries)

        #change the value of the variable 'greeting'
        greeting = 'hell world'
        self.assertTrue('hello' not in greeting)

    def test_identity_operators(self):
        """
        Identity operators compare the memory locations of two objects

        Identity operators always return a Boolean (True/False)
        """

        #change the value of the variable 'director'
        director = True
        self.assertTrue(director is True)

        #change the value of the variable 'my_program'
        course = "Geography"
        my_program = 'Geography'
        self.assertTrue(my_program is course)

    def test_priority_of_operators(self):
        """
        Test operator precedence
        """

        self.assertTrue(False is False)


        statement = False is False is False
        #replace 0 by the value of the variable 'statement'
        self.assertTrue(statement)

        statement_2 = (False is False) is False
        #replace 1 by the value of the variable 'statement'
        self.assertFalse(False)
