"""
    For consistency with problem statement, the first prop var is 1, not 0.
"""

from pdb import set_trace
from random import *

from pycryptosat import Solver

def main(): 
    s = Solver()
    print(experiment_once(s, 3, 150, 10))

def experiment_once(s, k, n, r):
    for i in range(r * n):
        s.add_clause(generate_clause(n,k))
    sat,_ = s.solve()
    return sat

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