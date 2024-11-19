import sympy as sm

rho = sm.Symbol('rho')
mu = sm.Symbol('mu')
lamda = sm.Symbol('lamda')
a = sm.Matrix([[0,0,0,-1/rho,0,0,0,0,0],
               [0,0,0,0,-1/rho,0,0,0,0],
               [0,0,0,0,0,-1/rho,0,0,0],
               [-(lamda+2*mu),0,0,0,0,0,0,0,0],
               [0,-mu,0,0,0,0,0,0,0],
               [0,0,-mu,0,0,0,0,0,0],
               [-lamda,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [-lamda,0,0,0,0,0,0,0,0]])

print(a.eigenvals())
#print(a)