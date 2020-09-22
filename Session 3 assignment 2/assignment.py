
###### Ignore this
import pytest
import hashlib
_ = 123456789  # just a wrong number, please ignore
###### Stop ignoring

import numpy as np

# Metabolic Flux Analysis

# 1. Write down the stoichiometry matrix S for the model as a numpy array.
# The order of the rows should correspond to A, B and C.
# The order of the columns should correspond to v1-v6


# replace [[]] with the stoichiometric matrix.
S = np.array([[-1,-1,0,0,0,1],
              [1,0,0,0,-1,0],
              [0,1,-1,-1,0,0]])

###### Don't touch
def test_stoichiometry_matrix():
    assert hashlib.md5(S).digest() == b'\xe2Q(\xd6\xf1\x8f.7F\xfbB(\xabY\xf8\xcc'
###### this


# 2. Calculate how many fluxes need to be measured (degrees of freedom).

from numpy.linalg import matrix_rank

# Degrees of freedom: Number of columns (n) minus the rank of the matrix
n = S.shape[1]

# Assign your solution to the following variable (replace _ with your solution;
# cannot be just a number; should be a computation based on S)
degrees_of_freedom = n - matrix_rank(S)

###### Don't touch
def test_degrees_of_freedom():
    assert degrees_of_freedom == 3
###### this


# 3. Based on measured fluxes v4 = 2.5, v5 = 2, and v6 = 10, calculate v1-v3.

v4 = 2.5
v5 = 2
v6 = 10

S_c = S[:, 0:3]
S_m = S[:, 3:]
v_m = np.array([v4,v5,v6])

Sc_inv = np.linalg.inv(S_c)
Sdot = Sc_inv.dot(S_m)

# Assign the final solution here (replace _ with your final step)
# v_c needs to be a numpy.array containing the three calculated fluxes v1-v3
# Ideally you should get to v_c through a computation involving S and the
# measured fluxes v4-v6 as covered in the lecture.

v_c = (-1)*Sdot.dot(v_m)

###### Don't touch
def test_mfa_calculation():
    assert v_c.sum() == 15.5
###### this
