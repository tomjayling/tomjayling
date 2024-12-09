# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, no-member, C0301, C0411, W0511

''' Semester 2, Assignment 1

Assignment Tasks: 4

Restrictions:
    Do not change anything outside TODO blocks.
    Do not add pylint directives.

Guidance:
    Define a function to generate random numbers with a PDF reflecting
    the angular intensity distribution behind a single slit and generate
    a plot comparing the histogram of a drawn sample with the PDF. The angular
    range is -pi/2 to pi/2.

    Ensure that your program correctly evaluates sin(x)/x at x=0, which should
    yield 1.

    Task 2:
    Ensure that the PDF is normalized.

Author of template:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
'''


import numpy as np
import scipy.interpolate as interpolate
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Fixed wavelength and slit_width in metres
wavelength = 500e-9
slit_width = 1500e-9 

# TODO: Assignment Task 1: define any additional functions you might need
def intensity(alpha):
    x = (np.pi*slit_width*np.sin(alpha))/wavelength
    return (np.sin(x)/x)**2
# End of Task 1; proceed to task 2.

def slit_pdf(alpha):
    """ Calculate the value of the pdf at angles alpha

    Parameters
    ----------
    alpha : float or numpy array of float
        angle(s) to evaluate the pdf at.
        angles are in radians.

    Returns
    -------
    pdf_values: float or numpy array of float
        resulting value(s) of the pdf
    """
    integral, error = integrate.quad(intensity, -np.pi/2, np.pi/2) 
    return intensity(alpha)/integral
    # TODO: Assignment Task 2: write function body
    # End of Task 2; proceed to task 3.

def rv_from_pdf(pdf_function, pdf_range, n):
    """ Calculate random values with given pdf

    Parameters
    ----------
    pdf_function : function
        The PDF function

    pdf_range : array-like
        pdf_range[0] is the allowed minimum value for the random values
        pdf_range[1] is the allowed maximum value for the random values

    n : integer
        number of random values to draw

    Returns
    -------
    rv: numpy array of float
        resulting random values
    """
    # TODO: Assignment Task 3: write function body
    angles = np.linspace(pdf_range[0],pdf_range[1],n)
    pdf_angles = pdf_function(angles)
    cdf = integrate.cumtrapz(pdf_angles,angles,initial=0)
    f = interpolate.interp1d(cdf, angles, kind='linear')
    x = np.random.rand(n)
    return f(x)
    
    # End of Task 3; proceed to task 4.

def generate_plot(fig, n, bins):
    """ Create a fully labelled plot

    Modify the provided figure object to show a histogram with error bars
    overlayed by the PDF and return the figure.

    Parameters
    ----------

    fig: matplotlib figure
        object to draw on

    n: integer
        number of samples to use to generate the histogram

    bins: integer
        number of bins to use to generate the histogram

    Returns
    -------
    fig: matplotlib figure
        figure object with fully labelled plot
    """
    # TODO: Assignment Task 4: write function body                    # number of random values to draw
    x_rand = rv_from_pdf(slit_pdf,[-np.pi/2,np.pi/2],n)
    nr_in_bin, bin_edges = np.histogram(x_rand, bins, range=(-np.pi/2, np.pi/2))
    width = bin_edges[1:] - bin_edges[:-1]              # widths of the individual bins
    center = (bin_edges[:-1] + bin_edges[1:]) / 2       # centre positions of the individual bins
    yerr = np.sqrt(nr_in_bin)                           # statistical error for counts in bins
    
    s = 1/np.sum(width*nr_in_bin)
    ax = fig.add_subplot(1, 1, 1)
    # draw histogram with error bars
    ax.bar(center, nr_in_bin*s, align='center', width=width*0.9, yerr=yerr*s,
           color='g', error_kw={'elinewidth':2, 'capsize':4, 'capthick':2},
           label='histogram of ')
    # draw PDF//
    ax.plot(x_rand,slit_pdf(x_rand),'r-', linewidth=2, label='PDF')
    ax.set_xlabel('angle')
    ax.set_ylabel('probability density')
    ax.set_title('Title')
    ax.legend()
    return fig
    # End of Task 4; no further tasks.

def main():
    ''' do everything '''
    fig = plt.figure()
    fig = generate_plot(fig, 100, 51)
    plt.show()


if __name__ == '__main__':
    main()
