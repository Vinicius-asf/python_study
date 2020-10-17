import numpy as np
from docplex.mp.model import Model

rmd = np.random
rmd.seed(0)

n = 10
Q = 15
N = [i for i in range(1,n+1)]
V = [0] + N
q = {i:rmd.randint(1,10) for i in N}


loc_x = rmd.rand(len(V))*200
loc_y = rmd.rand(len(V))*100

import matplotlib.pyplot as plt

A = [(i,j) for i in V for j in V if i != j]
c = {(i,j):np.hypot(loc_x[i]-loc_x[j],loc_y[i]-loc_y[j]) for i,j in A}

mdl = Model('CVRP')
x = mdl.binary_var_dict(A,name='x')
u = mdl.continuous_var_dict(N,ub=Q,name='u')

mdl.minimize(mdl.sum(c[i,j]*x[i,j] for i,j in A))
mdl.add_constraints(mdl.sum(x[i,j] for j in V if j!=i)== 1 for i in N)
mdl.add_constraints(mdl.sum(x[i,j] for i in V if j!=i)== 1 for j in N)
mdl.add_indicator_constraints(mdl.indicator_constraint(x[i,j], u[i]+q[j]==u[j]) for i,j in A if i!=0 and j!=0)
mdl.add_constraints(u[i]>=q[i] for i in N)
solution = mdl.solve(log_output=True)


