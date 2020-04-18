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

# n: number of propositional variables that we can use
# k: number of literals in clause
def generate_clause(n, k):
    return list(
        map(
            lambda x: x * choice([1,-1]),
            sample(range(1,n+1), k)
        )
    )

main()