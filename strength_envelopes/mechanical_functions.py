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


def Anderson_fault(fault_type, depths, densities, mu, C0, lamb, g):
    """ Returns the corresponding differential stress in MPa for a specific depth
    based on the Anderson theory of faulting (Anderson, 1905) and the Coulomb–
    Navier’s law of friction.

    Parameters
    ----------
    fault_type : string
        the type of fault, either 'inverse', 'normal' or 'strike-slip'
    depths : array-like
        an array-like with the depths [km]
    densities : array-like
        the corresponding average density [kg/m**3]
    mu : positive scalar
        coefficient of friction
    C0 : positive scalar
        internal cohesion of the rock [MPa]
    lamb : positive scalar
        coefficient of fluid pressure
    g : scalar
        average gravitational acceleration [m/s**2]
    """

    depths = 1000 * depths  # convert km to m

    if fault_type == 'thrust':
        diff_stress = (2 * (C0 + mu * densities * g * depths * (1 - lamb))) / (np.sqrt(mu**2 + 1) - mu)

    elif fault_type == 'strike-slip':
        diff_stress = (2 * (C0 + mu * densities * g * depths * (1 - lamb))) / (np.sqrt(mu**2 + 1))

    elif fault_type == 'extension':
        diff_stress = (- 2 * (C0 - mu * densities * g * depths * (1 - lamb))) / (np.sqrt(mu**2 + 1) + mu)

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


def calc_average_density(depths, moho, Lab, crust_densities, crust_layers, mantle_density):
    """ Return the corresponding average density at specific depths.

    Parameters
    ----------
    depths : array-like
        a list with the depths
    moho : positive scalar
        the depth of the moho discontinuity
    Lab : positive scalar
        the depth of the lithosphere-asthenosphere boundary
    crust_densities : tuple with three values
        the average density of the different crust layers
    crust_layers : tuple with two values
        depth of the base with respect to the depth of the moho
    mantle_density : positive scalar
        the average density of the lithospheric mantle

    Assumptions
    -----------
    - Assumes a three-layer crust and a single-layer lithospheric mantle
    - The uppermost layer start at depth 0
    """

    # preallocate
    densities = np.zeros(len(depths))
    step = depths[1] - depths[0]

    for index, depth in enumerate(depths):

        if depth <= crust_layers[0] * moho:  # upper crust
            avg_density = crust_densities[0]
        elif depth <= crust_layers[1] * moho:  # middle crust
            avg_density = densities[index - 1] * ((depth - step) / depth) + crust_densities[1] * (step / depth)
        elif depth <= moho:  # lower crust
            avg_density = densities[index - 1] * ((depth - step) / depth) + crust_densities[2] * (step / depth)
        elif depth <= Lab:  # lithospheric mantle
            avg_density = densities[index - 1] * ((depth - step) / depth) + mantle_density * (step / depth)

        densities[index] = avg_density

    return densities
