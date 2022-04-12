#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:22:51 2022

@author: sampasmann
"""

import numpy as np
"""
Analytic solution to reeds problem. Returns array and plot.
"""
def reeds_sol(Nx=1000):

    y1 = lambda x: (1 - 5.96168047527760*10**(-47)*np.cosh(52.06761235859028*x) -
    6.78355315350872*10**(-56)*np.cosh(62.76152118553390*x) -
    7.20274049646598*10**(-84)*np.cosh(95.14161078659372*x) -
    6.34541150517664*10**(-238)*np.cosh(272.5766481169758*x))

    y2 = lambda x: (1.685808767651539*10**3*np.exp(-5.206761235859028*x) + 3.143867366942945*10**4*np.exp(-6.276152118553390*x) +
    2.879977113018352*10**7*np.exp(-9.514161078659372*x) + 8.594190506002560*10**22*np.exp(-27.25766481169758*x) +
    1.298426035202193*10**(-36)*np.exp(27.25766481169758*x) + 1.432344656303454*10**(-13)*np.exp(9.514161078659372*x) +
    1.514562265056083*10**(-9)*np.exp(6.276152118553390*x) + 1.594431209450755*10**(-8)*np.exp(5.206761235859028*x))

    y3 = lambda x: 1.105109108062394

    y4 = lambda x: (10 - 0.1983746883968300*np.exp(0.5254295183311557*x) - 7.824765332896027*10**(-5)*np.exp(1.108937229227813*x) -
    9.746660212187006*10**(-6)*np.exp(1.615640334315550*x) - 2.895098351422132*10**(-13)*np.exp(4.554850586269065*x) -
    75.34793864805979*np.exp(-0.5254295183311557*x ) - 20.42874998426011*np.exp(-1.108937229227813*x) -
    7.129175418204712*10**(2)*np.exp(-1.615640334315550*x) - 2.716409367577795*10**(9)*np.exp(-4.554850586269065*x))

    y5 = lambda x: (31.53212162577067*np.exp(-0.5254295183311557*x) + 26.25911060454856*np.exp(-1.108937229227813*x) +
    1.841223066417334*10**(3)*np.exp(-1.615640334315550*x) + 1.555593549394869*10**(11)*np.exp(-4.554850586269065*x) -
    3.119310353653182*10**(-3)*np.exp(0.5254295183311557*x) - 6.336401143340483*10**(-7)*np.exp(1.108937229227813*x) -
    3.528757679361232*10**(-8)*np.exp(1.615640334315550*x) - 4.405514335746888*10**(-18)*np.exp(4.554850586269065*x))

    xspan = np.linspace(-8.0,8.0,num=Nx)
    y = np.zeros(Nx)
    count = 0
    
    for x in xspan:
        x = np.abs(x)
        if (x < -6.0):
            y[count] = y5(x)
        elif (-6.0 <= x < -5.0):
            y[count] = y4(x)
        elif (-5.0 <= x < -3.0):
            y[count] = y3(x)
        elif (-3.0 <= x < -2.0):
            y[count] = y2(x)
        elif (-2.0 <= x < 2.0):
            y[count] = y1(x)
        elif (2.0 <= x < 3.0):
            y[count] = y2(x)
        elif (3.0<= x < 5.0):
            y[count] = y3(x)
        elif (5.0<= x < 6.0):
            y[count] = y4(x)
        elif (6.0<= x):
            y[count] = y5(x)
        count += 1
    y = np.reshape(y, (Nx,1))
    return y