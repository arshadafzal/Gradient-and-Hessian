#  Program to calculate Hessian using Numerical Differentiation
#  INPUT:
#  x: Column Vector, shape n - by -  1
#  eps: Perturbation
#  OUTPUT:
#  Hessian Matrix, shape n - by -  n
#  =================================================================================
#  Version 1.0
#  Author: Arshad Afzal, GIST, South Korea
#  https://www.researchgate.net/profile/Arshad_Afzal
#  For Questions/ Comments, please email to arshad.afzal@gmail.com
#  =================================================================================
import numpy as np
from myfun import *


def hessian(x, eps):
    n = (np.shape(x))[0]
    h = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            y = x.copy()
            z = x.copy()
            y[i][0] = x[i][0] + eps
            z[i][0] = x[i][0] - eps
            u = y.copy()
            v = z.copy()
            if j == i:
                h[i][j] = (myfun(y) - 2 * myfun(x) + myfun(z))/(pow(eps, 2))
            else:
                u[j][0] = u[j][0] + eps
                z[j][0] = z[j][0] + eps
                y[j][0] = y[j][0] - eps
                v[j][0] = v[j][0] - eps
                h[i][j] = (myfun(u) - myfun(y) - myfun(z) + myfun(v)) / (4 * pow(eps, 2))
    return h

