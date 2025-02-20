import numpy as np
def peni(variable):
    '''
    input:
    V: culture medium volume L [60, 20]
    X: biomass concentration g/L [0.05, 18]
    T: temperature K [293, 303]
    S: glucose substrate concentration g/L [0.05, 18]
    F: substrate feed rate L/hr [0.01, 0.50]
    S_f: substrate feed concentration g /L [500, 700]
    pH: pH [5, 6.5]

    return:
    P: concentration of penicillin (>=0)
    t: reaction time (>=0)
    CO2: CO2 concentration (>=0)
    '''
    #initialize
    V, X, T, S, F, S_f, pH = variable[0], variable[1], variable[2], variable[3], variable[4], variable[5], variable[6]
    P = 0
    t= 0
    CO2 = 0
    dt = 0.5
    process_end = False
    iter = 0

    H = 10**(-pH)
    lamb = 2.5* 10**(-4)
    T0 = 273.1
    Tv = 373.1
    alpha1 = 0.143
    alpha2 = 4* 10**(-7)
    alpha3 = 10**(-4)
    mx = 0.014
    mux = 0.092
    K1 = 10**(-10)
    K2 = 7* 10**(-5)
    Kx = 0.15
    kg = 7*10**3
    Eg = 5100 
    R = R = 1.9872
    kd = 10**33
    Ed = 50000
    mup = 0.005
    Kp = 0.0002
    K_I = 0.1 
    K = 0.04
    Yxs = 0.45
    Yps = 0.90


    while not process_end:
        iter +=1
        #dV
        dV = F - V*lamb*(np.exp(5* ((T- T0)/(Tv-T0)))-1)

        #dX
        mu = (mux/(1+K1/H+H/K2))*(S/(Kx*X+S))*(kg*np.exp(-Eg/(R*T))-kd*np.exp(-Ed/(R*T)))
        dX = mu* X - (X/V)*dV

        #dP
        mupp = mup * (S/(Kp+S+(S**2/K_I)))
        dP = mupp *X - K*P - (P/V)*dV

        #dS
        dS = - (mu/Yxs)*X -  (mupp/Yps)*X -mx*X + (F*S_f/V) -(S/V)*dV

        #dCO2
        dCO2 = alpha1*dX + alpha2*X + alpha3

        #update
        V += dV*dt
        X += dX*dt
        P += dP*dt
        S += dS*dt
        CO2 += dCO2*dt
        t +=dt

        #whether to stop process
        if V > 180: #exceed maximum volume
            process_end = True
        elif dP < 10**(-12): # P converges
            process_end = True
        elif iter > 1000: #max iteration
            process_end = True
    return P, t, CO2

