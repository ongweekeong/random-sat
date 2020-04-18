"""
    For consistency with problem statement, the first prop var is 1, not 0.
"""

from pdb import set_trace
from random import *

from pycryptosat import Solver

def main():
    s = Solver()

    s.add_clause([-1,2,3])
    s.add_clause([1,3,4])
    s.add_clause([1,3,-4])
    s.add_clause([1,-3,4])
    s.add_clause([1,-3,-4])
    s.add_clause([-2,-3,4])
    s.add_clause([-1,2,-3])
    s.add_clause([-1,-2,3])
    s.add_clause([-1])

    sat, soln = s.solve()
    print(f'SAT: {sat}')
    print(f'SOLN: {soln}')

main()