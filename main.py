"""
    For consistency with problem statement, the first prop var is 1, not 0.
"""

from pdb import set_trace
from random import *

from pycryptosat import Solver

def main():
    s = Solver()

    # give_formula

    sat, soln = s.solve()
    print(f'SAT: {sat}')
    print(f'SOLN: {soln}')

def give_formula(s, k, n, r):
    for i in range(r * n):
        s.add_clause(generate_clause(n,k))

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