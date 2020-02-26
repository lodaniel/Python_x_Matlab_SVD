# Author: Luciano de Oliveira Daniel
# https://sites.google.com/site/professorlucianodaniel

from scipy.io import savemat
from numpy import random
from numpy import linalg
import time
import numpy as np

def pause():
    input("Press the <ENTER> key to continue...")


dim = int(input('Dimension of the square random matrix:'))
A = random.rand(dim, dim)
print(A, '\n')
print()
savemat('calc_svd_01.mat', {'A': A})
t = time.time()
u_P, s_P, vh_P = np.linalg.svd(A, full_matrices=True)
elapsed = time.time() - t
print(u_P, '\n')
print(s_P, '\n')
print(vh_P, '\n')
print('SVD elapsed time in PYTHON (executable) is:', elapsed, 'seconds', '\n')
savemat('calc_svd_02.mat', {'u_P': u_P})
savemat('calc_svd_03.mat', {'s_P': s_P})
savemat('calc_svd_04.mat', {'vh_P': vh_P})
print('"I have a paper afloat which I hold to be great guns" (Maxwell, J.C.)', '\n')
pause()
