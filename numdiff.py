#  Program to calculate Gradient using Numerical Differentiation
#  INPUT:
#  x: Column Vector, shape n - by -  1
#  eps: Perturbation
#  OUTPUT:
#  Gradient Vector, shape n - by -  1
#  =================================================================================
#  Version 1.0
#  Author: Arshad Afzal, IIT Kanpur, India
#  https://www.researchgate.net/profile/Arshad_Afzal
#  For Questions/ Comments, please email to arshad.afzal@gmail.com
#  =================================================================================
import numpy as np
from myfun import *


def numdiff(x, eps):
    n = (np.shape(x))[0]
    f = np.zeros([n, 1])
    for i in range(n):
        y = x.copy()
        z = x.copy()
        y[i][0] = x[i][0] + eps
        z[i][0] = x[i][0] - eps
        f[i][0] = (myfun(y) - myfun(z))/(2 * eps)
    return f

