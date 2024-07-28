# -*- coding: utf-8 -*-
# pylint: disable=E0012, fixme, invalid-name, no-member, R0913, R1716, W0613, W0622, E0611, W0603, R0902, R0903, C0301
"""  Semester 2, Assignment 4

Assignment Tasks: 8

Aim:
    GUI to visualise electric field lines for a collection of point charges.

    To remove a charge:
        Left-click on it and release.

    To add a charge:
        Left-click and hold, move mouse left or right reading charge in status
        message and release. Adds the charge of displayed magnitude at the initial
        mouse press position.

    Drag a charge:
        Left-click on a charge and drag it

Restrictions:
    Do not change anything outside TODO blocks.
    Do not use import.
    Do not add pylint directives.

Guidance:
    Please read the introduction page to this assignment on Canvas.

Author of the template:
    Wolfgang Theis
    School of Physics and Astronomy
    University of Birmingham
"""

import sys
import numpy as np
from scipy.integrate import odeint
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas



class Charges:
    ''' A collection of point charges in the xy-plane

    distances, charges, electric fields, and potentials are treated as unitless

    The electric field due to a charge q at distance d is taken to be
    E = q/d**2

    The potential V is given by dV/dr = -E

    '''

    def __init__(self):
        # private attributes
        # self._q is a 1d array holding the value of the charge for the different charges
        # charege n has a charge of self._q[n]
        self._q = np.zeros((0, ))
        # self._pos is a 2d array with xy coordinates of the charges
        # x position of charge n is self._pos[n, 0]
        # y position of charge n is self._pos[n, 1]
        self._pos = np.zeros((0, 2))

    def add_charge(self, q, xy):
        ''' add charge of magnitude q at locations x,y = xy '''
        self._q = np.hstack([self._q, q])
        self._pos = np.vstack([self._pos, np.array([xy])])

    def delete_charge(self, k):
        ''' delete charge k '''
        if 0 <= k < self._q.shape[0]:
            self._q = np.delete(self._q, k)
            self._pos = np.delete(self._pos, k, 0)

    def set_position(self, k, xy):
        ''' set position of charge k to xy '''
        if 0 <= k < self._q.shape[0]:
            self._pos[k, :] = xy

    def get_charges(self):
        ''' provide list of (charge, position) tuples '''
        p = self._pos
        return [(q, p[k, :]) for k, q in enumerate(self._q)]

    def get_closest(self, xy, limit=0.2):
        ''' determine the index of the closest charge

        Parameters
        ----------
        xy: array-like
            x,y pair of position to find the closest charge to.

        limit:
            maximum distance to find a charge in.

        Returns
        -------
        index: int
            index of the closest charge
            If no charge is within the limit then None is returned.
        '''
        # TODO: Assignment Task 1: write function body
        vector_s = xy - self._pos #gets the vector displacement from each charge
        mag_s = np.sqrt(vector_s[:, 0]**2 + vector_s[:, 1]**2) #gets the magnitude of those vectors
        if min(mag_s) <= limit: #checks there is a charge within the limit
            index = np.argmin(mag_s)     # finds the index of the charge with the smallest distance
        else:
            index = None
        return index

    def scaled_electric_field(self, xy, _):
        ''' calculate suitably scaled electric field vector at position xy.

        The scaling is such that integrating this scaled field along field lines
        Es(lambda) dlambda from lamda=0 to lamda_max transverses roughly a
        modulus of the potential energy difference of lambda_max.

        To avoid numerical instabilities it should be ensured that the return value
        is not divergent by ensuring that the scaling factor remains finite.
        If you had a pure scaling factor of 1/x where x could be zero,
        you would use 1/(x+0.0001) instead]

        Parameters
        ----------
        xy: array-like
            x,y pair of position at which the scaled electric field is requested

        _:
            not used but required place holder for ode integrator

        Returns
        -------
        ef: array-like
            scaled electric field Es = (s*Ex, s*Ey) at position xy

        '''
        # TODO: Assignment Task 2: write function body
        vector_s = (xy - self._pos).T  #gets the vector displacement from each charge
        mag_s = np.array(np.sqrt(vector_s[0]**2 + vector_s[1]**2)) #gets the magnitudes
        mag_E = (self._q)/(mag_s)**2
        vector_E = (mag_E*vector_s)/mag_s #gets the vector fields from each charge
        ef = np.zeros(2)
        ef[0] = np.sum(vector_E[0])
        ef[1] = np.sum(vector_E[1])
        mod = ef[0]**2 + ef[1]**2 #gets the scaling constant
        return ef/(mod+0.0001) #returns total scaled E field
        # End of Task 2; proceed to task 3.

    def field_lines(self, nr_of_fieldlines=32, start_radius=0.2, lambda_max=10, points=801):
        ''' calculate the field lines which should include one at pi/4, rather than 0

            Parameters
            ----------

            nr_of_fieldlines: int
                number of field lines originating from each positive charge

            start_radius: float
                radius around each positive charge at which the field lines start

            lambda_max: float
                the maximum value of the parameter for the parametric representation
                of the fieldlines x(lambda), y(lambda), lambda =[0,..., lambda_max]

            points: int
                the number of points in each fieldline

            Returns
            -------

            fieldlines: list of 2-d numpy arrays
                each element of the list is an array of shape (points, 2) with
                fieldlines[k][:, 0] and fieldlines[k][:, 1] providing
                the x and y values, respectively of the k-th fieldline
        '''
        # TODO: Assignment Task 3: write function body
        angles = np.linspace(np.pi/nr_of_fieldlines, 2*np.pi, nr_of_fieldlines) #angles which the field lines come out from
        lamda = np.linspace(0, lambda_max, points) #integration variable
        fieldlines = []
        xy = np.zeros(2)
        for n, charge in enumerate(self._q): #loops through charges
            if charge > 0: #checks the charge is not neutral
                for pos in angles:
                    xy[0] = self._pos[n, 0] + np.cos(pos)*start_radius #starting x positions for each field line
                    xy[1] = self._pos[n, 1] + np.sin(pos)*start_radius #starting y positions for each field line
                    fieldlines.append(odeint(self.scaled_electric_field, xy, lamda)) #creates field lines by integrating along lamda
        return fieldlines
        # End of Task 3; proceed to task 4.


class MyMainWindow(QMainWindow):
    ''' the main window potentially with menus, statusbar, ... '''

    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.move(400, 300)
        central_widget = MyCentralWidget(self)
        self.setCentralWidget(central_widget)
        self.setWindowTitle('PyQt widget with matplotlib figure')
        self.statusBar().showMessage('Waiting for mouse move or mouse click')


class MyCentralWidget(QWidget):
    ''' everything in the main area of the main window '''

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        # define figure canvas
        self.mpl_widget = MyMplWidget(self.main_window)
        # place MplWidget into a vertical box layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_widget)  # add the figure
        # use the box layout to fill the window
        self.setLayout(vbox)


class MyMplWidget(FigureCanvas):
    ''' both a QWidget and a matplotlib figure '''

    def __init__(self, main_window, parent=None, figsize=(4, 4), dpi=100):
        self.main_window = main_window
        self.fig = plt.figure(figsize=figsize, dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        self.mouse_pressed_pos = None
        self.closest_k = None
        self.dragging = False
        self.qadd = 0
        self.lines = []
        self.points = []
        self.field_lines_args = None            # used to save the parameters for use in drag_replt
        self.charges = Charges()
        # add some charges to start with an example
        self.charges.add_charge(1, (1, 0))
        self.charges.add_charge(1, (-1, 0))
        self.charges.add_charge(-1, (0, 1))
        self.charges.add_charge(-1, (0, -1))
        self.plot_fieldlines()
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.cid_press = self.fig.canvas.mpl_connect('button_press_event', self.on_mouse_press)
        self.cid_release = self.fig.canvas.mpl_connect('button_release_event', self.on_mouse_release)
        self.cid_move = self.fig.canvas.mpl_connect('motion_notify_event', self.on_mouse_move)

    def plot_fieldlines(self, nr_of_fieldlines=32, start_radius=0.2, lambda_max=10, points=801):
        ''' clear figure and plot fieldlines and charges '''
        self.fig.clf()
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.lines = []         # list of matplotlib lines in the plot showing the fieldlines (for drag_replot)
        self.points = []        # list of matplotlib lines in the plot showing the charges (for drag_replot)
        self.field_lines_args = (nr_of_fieldlines, start_radius, lambda_max, points)
        # TODO: Assignment Task 4: calculate and plot field lines; plot charges; collect lines and points
        for line in self.charges.field_lines(*self.field_lines_args):
            a, = self.ax.plot(line[:, 0], line[:, 1], 'k', label='Field Lines')
            self.lines.append(a)  #stores the plotting details for each line
        for charge, position in self.charges.get_charges():
            if charge > 0:
                shape = 'bo' #blue circle for positive charge
            else:
                shape = 'ro' #red circle for negative charge (neutral charges aren't added)
            point, = self.ax.plot(*position, shape, markersize=15*np.sqrt(abs(charge)))
            self.points.append(point) #stores the plotting details for each point
        # End of Task 4; proceed to task 5.
        self.ax.set_xlabel('$x$')
        self.ax.set_ylabel('$y$')
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 5)
        self.ax.set_aspect('equal')
        self.draw()

    def drag_replot(self):
        ''' replot elements in self.lines and self.point
            after adjusting their xdata and ydata arrays
            to reflect the new position of the dragged charge.
        '''
        self.ax.draw_artist(self.ax.patch)                              # <-- redraw the plotting area of the axis
        # TODO: Assignment Task 5: redraw updated field lines and charges
        for i, j in enumerate(self.charges.field_lines(8)): #calculates 8 field lines for efficiency
            self.lines[i].set_xdata(j[:, 0])
            self.lines[i].set_ydata(j[:, 1])
            self.ax.draw_artist(self.lines[i]) #only the lines that have been updated will be drawn
        self.points[self.closest_k].set_xdata = self.current_mouse_pos[0] #change only the point being dragged
        self.points[self.closest_k].set_ydata = self.current_mouse_pos[1]
        for point in self.points:
            self.ax.draw_artist(point) #all points will be drawn
        # End of Task 5; proceed to task 6.
        self.fig.canvas.update()                                        # <-- update the figure
        self.fig.canvas.flush_events()                                  # <-- ensure all draw requests are sent out

    def on_mouse_move(self, event):
        ''' add charge or drag

            self.dragging determines whether a charge is being dragged and is
            updated accordingly.

            If a charge is being added then self.qadd, the value of the charge
            is updated and the current value displayed in the statusbar.

            If a charge is being dragged then its position is updated in the
            self.charges object and the charges and fieldlines are displayed using
            drag_replot().

        '''
        # TODO: Assignment Task 6: write function body
        if event.xdata is not None and event.ydata is not None and self.mouse_pressed_pos is not None: #only exectues if mouse is being held down and is in the display window
            self.current_mouse_pos = np.array([event.xdata, event.ydata]) #new class attribute defined for the current mouse position so that the information can be accessed from other functions 
            if self.closest_k is None: #if no charge has been clicked on
                self.qadd = np.round(self.current_mouse_pos[0]-self.mouse_pressed_pos[0]) #record the round(dx) for when charge is added
                msg = f'qadd={self.qadd}'
                self.main_window.statusBar().showMessage(msg)
            else:
                self.dragging = True
                self.charges.set_position(self.closest_k, self.current_mouse_pos)
                self.drag_replot() #replot lines for new position of charge being dragged
        # End of Task 6; proceed to task 7.

    def on_mouse_press(self, event):
        ''' set self.mouse_pressed_pos and self.closest_k, the
            xy pair for the position the mouse was clicked at
            and the index of of the charge closest to that position, respectively.
        '''
        # TODO: Assignment Task 7: write function body
        if event.xdata is not None and event.ydata is not None: #makes sure mouse is in the display window
            self.mouse_pressed_pos = np.array([event.xdata, event.ydata]) #stores (x,y) position of mouse click
            self.closest_k = self.charges.get_closest(self.mouse_pressed_pos) #gets the nearest charge to that position
        # End of Task 7; proceed to task 8.

    def on_mouse_release(self, event):
        ''' perform required actions when the mouse button is released

        If a charge should be deleted, delete the charge.
        If a charge should be added, add the charge.

        In all cases, redraw the figure with 32 fieldlines per charge
        and reset attributes as appropriate.
        '''
        # TODO: Assignment Task 8: write function body
        if event.xdata is not None and event.ydata is not None and self.mouse_pressed_pos is not None: #if mouse is released in the display window after having being clicked originally in the display window
            if not self.closest_k is None:
                if self.dragging is False:
                    self.charges.delete_charge(self.closest_k) #deletes if charge is clicked on but not dragged
            else:
                if not self.qadd == 0:
                    self.charges.add_charge(self.qadd, self.mouse_pressed_pos) #adds charge if no charge was clicked on and mouse was moved far enough
        self.dragging = False #resets attributes for the next click
        self.closest_k = None
        self.qadd = 0
        self.mouse_pressed_pos = None
        self.plot_fieldlines() #plots the new field lines and points
        # End of Task 8; no further tasks


app = None


# pylint: disable=C0111
def main():
    global app
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec()


if __name__ == '__main__':
    main()
