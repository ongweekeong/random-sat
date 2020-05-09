"""
    For consistency with problem statement, the first prop var is 1, not 0.
"""
import time
from pdb import set_trace
from random import *

from pysat.solvers import Solver

NUM_EXP = 50 # number of experiments to run per set of random params

def main():
    results = []
    n = 150
    for num in range(NUM_EXP):
        for k in range(4,6): # for k from 3 to 5
            results.append([])
            for r5 in range(0, 51):
                r = r5/5 # in steps of 0.2
                start_time = time.time()
                count = experiment_many(k, n, r, 1)
                duration = time.time() - start_time
                results[-1].append(count)
                print(f'k:{k} r:{r} -- {count}', 'time taken: ', duration)
        
        print(results)

def experiment_many(k, n, r, times):
    sat_count = 0
    for i in range(times): # initially used when running 50 experiments before giving output
        if experiment_once(Solver(), k, n, r):
            sat_count += 1
    return sat_count

def experiment_once(s, k, n, r):
    for i in range(round(r*n)): # generate r*n clauses
        clause = generate_clause(n,k)
        s.add_clause(clause)
    return s.solve()

# n: number of propositional variables that we can use
# k: number of literals in clause
def generate_clause(n, k):
    return list(
        map(
            lambda x: x * choice([1,-1]), #choose literal or its negation
            sample(range(1,n+1), k) # choose k literals randomly from 1 to 150
        )
    )

main()