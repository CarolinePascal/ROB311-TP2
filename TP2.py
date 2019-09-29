import numpy as np
import matplotlib.pyplot as plt
import copy as copy

def rmse(U,V):
    """
    @brief Computes the root mean square error between two utility vectors
    
    @param U : np array (n), the first utility vector
    @param V : np array (n), the second utility vector
    
    @return double : Returns the computed error
    """
    return np.sqrt(np.dot(U-V,(U-V).T)/len(U))

def value_iteration(R,g,x,y):
    """
    @brief Implements the value iteration method to compute the optima utility and policy
    
    @param R : np array (4), the static rewerd vector 
    @param x : double, problem parameter x
    @param y : double, problem parameter y
    @param y : double, the discount factor gamma 
    
    @return void : Displays the optima utility and policy results
    """

    #Initializing arrays and error value
    V = copy.deepcopy(R)
    P = [] 
    error = 1e5

    #Main loop
    while(error >= 1e-5):

        #Utility iteration
        U = copy.deepcopy(V)

        #Utility computation
        V[0] = R[0] + g*np.max([U[1],U[2]])
        V[1] = R[1] + g*((1-x)*U[1] + x*U[3])
        V[2] = R[2] + g*((1-y)*U[0] + y*U[3])
        V[3] = R[3] + g*U[0]

        #Policy monitoring
        if(U[1] == U[2]):
            P.append('both')
        elif(U[1] > U[2]):
            P.append('a1')
        else:
            P.append('a2')

        #Error computation
        error = rmse(U,V)
    
    #Display the results !
    print("The optimal utility is : \n V*0 = " + str(V[0]) + "\n V*1 = " + str(V[1]) + "\n V*2 = " + str(V[2]) + "\n V*3 = " + str(V[3]))
    print("The optimal policy for the choice in state S0 is P*0 = " + P[-1])

    return
        
#Reward vector
R = np.array([0.,0.,1.,10.])

#Parameters
x = 0.25
y = 0.25
g = 0.9

value_iteration(R,g,x,y)











