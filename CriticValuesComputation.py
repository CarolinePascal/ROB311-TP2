import sympy as sp

#Initializing symbols
u0,u1,u2,u3 = sp.symbols('u0,u1,u2,u3')
x,y,g = sp.symbols('x,y,g')

#Case where the optimal policy is pi(s0) = a2
result1 = sp.solve([u0-g*u2,u1-g*(1-x)*u1-g*x*u3,u2-1-g*(1-y)*u0-y*g*u3,u3-10-g*u0],(u0,u1,u2,u3))
#Case where the optimal policy is pi(s0) = a1
#result2 = sp.solve([u0-g*u1,u1-g*(1-x)*u1-g*x*u3,u2-1-g*(1-y)*u0-y*g*u3,u3-10-g*u0],(u0,u1,u2,u3))

#Compute the critic value for y - It's the same in both cases !
resulty = sp.solve(result1[u2]-result1[u1],y)
#Compute the critic value for x - It's the same in both cases !
resultx = sp.solve(result1[u2]-result1[u1],x)

#Display the computed expressions
print("The expression for the critic value of y is " + str(resulty))
print("The expression for the critic value of x is " + str(resultx))