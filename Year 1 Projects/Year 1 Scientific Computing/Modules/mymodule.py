# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:47:07 2020

@author: princ
"""

def input_integer(query_string):
    ''' Print query_string and return an integer entered by the user.

    Repeats prompting the user until an integer is provided.

    Parameters
    ----------
    query_string : string
        Text that is displayed to prompt the user to enter the integer

    Returns
    -------
    n : integer
        The integer value provided by the user

    Note
    ----
    The user continues to be prompted for input until an integer is provided.

    See Also
    --------
    input, input_float
    '''

    while True:
        r = input(query_string)
        try:
            n = int(r)
            return n
        except:
            print(f"'{r}' is not an integer")

if __name__ == '__main__':
    n = input_integer('\nPlease enter an integer\n')
    print(f'You entered a valid integer: {n}')