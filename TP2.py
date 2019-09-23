import numpy as np
import matplotlib.pyplot as plt
import copy as copy

def rms(U,V):
    return(np.sqrt(np.dot(U-V,(U-V).T)))

def value_iteration(R,g,x,y):
    V = copy.deepcopy(R)
    P = []  #For policies (a1 or a2) monitoring

    error = 1e5
    print(V)

    while(error >= 1e-5):

        U = copy.deepcopy(V)

        V[0] = R[0] + g*np.max([U[1],U[2]])

        #Policies monitoring
        if(U[1] == U[2]):
            P.append(0)
        elif(U[1] > U[2]):
            P.append(1)
        else:
            P.append(2)

        V[1] = R[1] + g*((1-x)*U[1] + x*U[2])
        V[2] = R[2] + g*((1-y)*U[0] + y*U[3])
        V[3] = R[3] + g*U[0]

        error = rms(U,V)

        print(V)

    return(V,P)
        
R = np.array([0.,0.,1.,10.])
V,P = value_iteration(R,0.5,0.5,0.5)
print(P)









