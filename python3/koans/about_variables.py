#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutVariables(Koan):

    def test_that_sometimes_we_need_to_know_the_data_type(self):
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

        self.assertEqual(__, type("navel")) # It's str, not <type 'str'>

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
        nb_of_cars = 4

        self.assertEqual(__, type(nb_of_cars)) # It's int, not <type 'int'>

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

        self.assertEqual(__, type("hello world")) # It's str, not <type 'str'>

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

        self.assertEqual(__, type(student)) # It's bool, not <type 'bool'>

        # Need an illustration? More reading can be found here:
        #
        #   http://bit.ly/__class__
