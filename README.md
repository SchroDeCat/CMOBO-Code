# CMOBO
CMOBO_code

## peni.py
contains a function that simulates the biological process of penicillin reaction, which has been used as a test function for MOBO in *Scalable Bayesian Optimization Accelerates Process Optimization of Penicillin Production, 2021*(https://openreview.net/forum?id=UVdSYXMNdOe). It was first released in *A modular simulation package for fed-batch fermentation: penicillin production, 2002*(https://www.sciencedirect.com/science/article/abs/pii/S0098135402001278)

it takes a 7-D input and its output is 3-D.

## CMOBO.ipynb

I've written a simple botorch work flow for CMOBO in discrete case. And I have some troubles in the continuous case, which is mainly from non-linear constraints generated from UCB, where I defined the `create_ucb_constraints` function. Errors arise when I passed the constraints into `optimize_acqf`.
