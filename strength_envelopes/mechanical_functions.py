# ============================================================================ #
#                                                                              #
#    Strenght envelopes                                                        #
#    A Python script for plotting lithosphere and crust strength envelopes     #
#                                                                              #
#    Copyright (c) 2017-present   Marco A. Lopez-Sanchez                       #
#                                                                              #
#    This Source Code Form is subject to the terms of the Mozilla Public       #
#    License, v. 2.0. If a copy of the MPL was not distributed with this       #
#    file, You can obtain one at http://mozilla.org/MPL/2.0/.                  #
#                                                                              #
#    Covered Software is provided under this License on an “AS IS” BASIS,      #
#    WITHOUT WARRANTY OF ANY KIND, either expressed, implied, or statutory,    #
#    including, without limitation, warranties that the Covered Software is    #
#    FREE OF DEFECTS, merchantable, fit for a particular purpose or            #
#    non-infringing. The entire risk as to the quality and performance         #
#    of the Covered Software is with You. Should any Covered Software prove    #
#    defective in any respect, You (not any Contributor) assume the cost of    #
#    any necessary servicing, repair, or correction. This disclaimer of        #
#    warranty constitutes an essential part of this License. No use of any     #
#    Covered Software is authorized under this License except under this       #
#    disclaimer.                                                               #
#                                                                              #
#    Version alpha                                                             #
#    For details see: https://github.com/marcoalopez/Strength_envelopes        #
#    download at https://github.com/marcoalopez/Strength_envelopes/releases    #
#                                                                              #
#    Requirements:                                                             #
#        Python version 3.5 or higher                                          #
#        Numpy version 1.11 or higher                                          #
#        Matplotlib version 2.0 or higher                                      #
#                                                                              #
# ============================================================================ #

import numpy as np

g = 9.80665  # average gravitational acceleration [m/s**2]
R = 8.3144598  # universal gas constant [J mol**-1 K**-1]

def Anderson_fault(fault_type, depth, mu, C0, lamb, ro_crust):
    """ Returns the corresponding differential stress in MPa for a specific depth
    in thrust faults using the Anderson theory of faulting (Anderson, 1905).

    Parameters
    ----------
    depth : positive scalar
        the depth [km]
    mu : positive scalar
        coefficient of friction
    C0 : positive scalar
        internal cohesion of the rock [MPa]
    lamb : positive scalar
        coefficient of fluid pressure
    """

    depth = 1000 * depth  # convert km to m

    if fault_type == 'thrust':
        diff_stress = (2 * (C0 + mu * ro_crust * g * depth * (1 - lamb))) / (np.sqrt(mu**2 + 1) - mu)

    elif fault_type == 'strike':
        diff_stress = (2 * (C0 + mu * ro_crust * g * depth * (1 - lamb))) / (np.sqrt(mu**2 + 1))

    elif fault_type == 'extension':
        diff_stress = (- 2 * (C0 - mu * ro_crust * g * depth * (1 - lamb))) / (np.sqrt(mu**2 + 1) + mu)

    return diff_stress / 10**6


    def power_law_creep(ss, A, n, Q, R, T, P, V, d, m, f, r):
        """ Return the neccesary differential stress (Tresca criterion) in MPa
        for permanently deforming a polycrystalline material at a given environmental
        conditions.

        Parameters (all positive scalars)
        ----------
        ss : strain rate [s**-1]
        A : material constant [MPa**-n s**-1]
        n : stress exponent
        Q : activation energy [J mol**-1]
        R : universal gas constant [J mol**-1 K**-1]
        T : absolute temperature [K]
        P : pressure [MPa]
        V : activation volume per mol [m**3 mol**-1]
        d : average grain size [microns]
        m : grain size exponent
        f : fugacity of water [water molecules per 1e6 Si atoms]
        r : water fugacity exponent

        Assumptions
        -----------
        - Steady-state creep
        - Moderate stress regime (roughly between 20 - 200 MPa)
        - Effect of partial melt ignored
        """

        return (ss * (d**m) * (f**r) * np.exp((Q + P * V) / (R * T)) / A)**(1 / n)
