#  FUNCTION File: Rosenbrock Function
#  Author: Arshad Afzal, IIT Kanpur, India
#  For Questions/ Comments, please email to arshad.afzal@gmail.com


from math import *


def myfun(x):
    f = 100 * pow((x[1][0] - pow(x[0][0], 2)), 2) + pow((1 - x[0][0]), 2)
    return f
