# -*- coding: utf-8 -*-
# pylint: disable= E0012, fixme, invalid-name, no-member, W1401

''' Assignment 5 (random numbers; compulsory)

Assignment Tasks: 3

Restrictions:
    Do not change anything outside TODO blocks.
    Do not use import, pi.
    Do not add pylint directives.

Guidance:
    Use np.random.rand().
    Do not use for or other loops.
    Use np.count_nonzero() to count how many values in an array are True.

Author of template:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
'''

import numpy as np

def xy_array(n):
    """ Generate an array with uniform PDF random number (x,y) pairs.

    Parameters
    ----------
    n : integer
        number of (x,y) pairs to include in the array

    Returns
    -------
    xy : array of floats
        The array has shape xy.shape = (n, 2).
        All elements are between -1 and 1.
    """
    # TODO: Assignment Task 1: write function body
    # transform range of random values from 0 to 1 to range between -1 and 1
    xy = (np.random.rand(n, 2)-0.5)*2  #create 2D array of these values
    return xy
    # End of Task 1; proceed to Task 2


def number_of_xy_in_circle(xy):
    """ Calculates the number of (x,y) pairs in the unit circle

    Parameters
    ----------
    xy : array
        numpy array of shape (n, 2)

    Returns
    -------
    nr_inside : integer
        The number of (x,y) pairs inside the circle.
    """
    # TODO: Assignment Task 2: write function body
    # count all values in xy that satisfy (x^2) + (y^2) < 1
    nr_inside = np.count_nonzero(xy[:, 0]**2+xy[:, 1]**2 < 1)
    return nr_inside
    # End of Task 2; proceed to Task 3


def estimate_pi(n):
    """ Estimate pi

    Parameters
    ----------
    n : integer
        number of (x,y) pairs to use for the estimate

    Returns
    -------
    pi_est : float
        Estimated value based on n (x,y) pairs.
    """
    # TODO: Assignment Task 3: write function body
    # find the proportion of total area (4) that is in the circle
    pi_est = 4*(number_of_xy_in_circle(xy_array(n))/n)
    return pi_est
    # End of Task 3; no further tasks.


if __name__ == '__main__':
    # pylint: disable=E0012, C0112, C0111, C0304, C0325, C0413, C0411, C0301
    import unittest

    print(estimate_pi(10))
    print(estimate_pi(100))
    print(estimate_pi(1000))
    print(estimate_pi(10000))


    class Xy_arrayTests(unittest.TestCase):
        ''' tests for Xy_array '''

        def test_1(self):
            ''' test correct shape '''
            self.assertEqual(xy_array(4).shape, (4, 2))

        def test_2(self):
            ''' test values in correct range (upper limit) '''
            self.assertLessEqual(np.max(xy_array(1000)), 1.0)

        def test_3(self):
            ''' test values in correct range (lower limit) '''
            self.assertGreaterEqual(np.min(xy_array(1000)), -1.0)

        def test_4(self):
            ''' test mean of probability distribution function '''
            self.assertAlmostEqual(np.mean(xy_array(100000)), 0.0, delta=0.01)

        def test_5(self):
            ''' test std of probability distribution function '''
            self.assertAlmostEqual(np.std(xy_array(100000)), 0.5773, delta=0.01)

        def test_6(self):
            ''' test lack of correlation between x and y values '''
            p = xy_array(100000)
            x = p[:, 0]
            y = p[:, 1]
            self.assertLess(np.corrcoef(x, y)[0, 1], 0.01)

    class Number_of_xy_in_circleTests(unittest.TestCase):
        ''' tests for number_of_xy_in_circle '''

        def test_1(self):
            ''' test that x=0.59, y=-0.8 is identified as inside the circle '''
            self.assertEqual(number_of_xy_in_circle(np.array([[0.59, -0.8]])), 1)

        def test_2(self):
            ''' test that x=0.62, y=0.8 is identified as outside the circle '''
            self.assertEqual(number_of_xy_in_circle(np.array([[-0.62, 0.8]])), 0)

        def test_3(self):
            ''' test that all below are inside the circle '''
            self.assertEqual(number_of_xy_in_circle(np.array([[-0.9, 0.3], [0.9, -0.3], [0.9, 0.3]])), 3)

    class Estimate_piTests(unittest.TestCase):
        ''' tests for estimate_pi '''

        def test_1(self):
            ''' test that pi is within expected accuracy (10 sigma)'''
            self.assertAlmostEqual(estimate_pi(100000), np.pi, delta=0.05)

        def test_2(self):
            ''' test that output is <= 4'''
            self.assertLessEqual(estimate_pi(1), 4)


    unittest.main(exit=False)
