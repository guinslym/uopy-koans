#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        self.assertTrue(False) # This should be True

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(__, 1 + 1)

    def test_assert_not_equal_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertNotEqual(__, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = __
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = __
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)


    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        self.assertEqual(__, "navel".__class__) # It's str, not <type 'str'>

        # Need an illustration? More reading can be found here:
        #
        #   http://bit.ly/__class__

    def test_this_variable_is_a_integer(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:
        my_number = 4

        self.assertEqual(__, my_number.__class__) # It's int, not <type 'int'>

        # Need an illustration? More reading can be found here:
        #
        #   http://bit.ly/__class__

    def test_this_variable_is_a_string(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        self.assertEqual(__, "hello world".__class__) # It's str, not <type 'str'>

        # Need an illustration? More reading can be found here:
        #
        #   http://bit.ly/__class__

    def test_this_variable_is_a_boolean(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:
        student = True

        self.assertEqual(__, student.__class__) # It's bool, not <type 'bool'>

        # Need an illustration? More reading can be found here:
        #
        #   http://bit.ly/__class__

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
