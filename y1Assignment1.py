# -*- coding: utf-8 -*-
# pylint: disable=E0012, invalid-name, no-member, C0301, C0411, C1801, W0622

''' Assignment 1

Assignment Tasks: 1

Restrictions:
    Do not change anything outside TODO blocks.
    Do not use import, mean(), or std().
    Do not add pylint directives.

Guidance:
    Use numpy arrays and np.sum() for your calculation.

Author of template:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
'''

import numpy as np

def mean_with_error(data):
    """ Calculate the mean and error of the mean.

    Parameters
    ----------
    data : array-like
        numpy array or list of numbers

    Returns
    -------
    (data_mean, error_of_mean) : tuple of numbers
        data_mean is the mean and error_of_mean is the error of the mean.
        These are the full machine precision results, not the rounded values.
        If either is not well-defined None is returned in its respective
        place, as in (data_mean, None) or (None, None)
    """
    # TODO: Assignment Task 1: write function body  # pylint: disable=fixme
    data = np.array(data)
    if len(data) == 1:
        return (data, None)
    if len(data) == 0:
        return (None, None)
    data_mean = np.sum(data) / len(data)
    variance = np.sum((data-data_mean)**2/(len(data)-1))
    std_dev = np.sqrt(variance)
    error_of_mean = std_dev/np.sqrt(len(data))
    return (data_mean, error_of_mean)
    # End of Task 1; no further tasks.


if __name__ == '__main__':
    # pylint: disable=E0012, C0112, C0111, C0304, C0325, C0413, C0411, C0301
    import unittest

    class Mean_with_errorTests(unittest.TestCase):
        ''' tests for mean_with_error(data) '''

        def test_list1(self):
            ''' test list input, identical values '''
            self.assertEqual(mean_with_error([1, 1, 1, 1]), (1, 0))

        def test_list2(self):
            ''' test list input, different values '''
            self.assertEqual(mean_with_error([1, 2]), (1.5, 0.5))

        def test_ndarray(self):
            ''' test length one input (single value) '''
            self.assertEqual(mean_with_error(np.ones(1)), (1, None))

        def test_ndarray1(self):
            ''' test calculated mean '''
            self.assertEqual(mean_with_error(np.arange(5))[0], 2.0)

        def test_ndarray2(self):
            ''' test calculated error of the mean value '''
            self.assertAlmostEqual(mean_with_error(np.arange(5))[1], 0.70710678)


    unittest.main(exit=False)
