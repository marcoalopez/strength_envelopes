# ============================================================================ #
#                                                                              #
#    This is part of the strenght_envelopes script                             #
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


def turcotte_schubert_eq(z0, z, T0, Jq, A, K):
    """ Apply the equation (model) of Turcotte and Schubert (1982) (ts) to estimate
    a steady-state geotherm (i.e. the T at a given depth)

    Parameters (all positive scalars)
    ----------
    z0 : surface elevation [km]
    z : max. depth in the model [km]
    T0 : temperature at Earth surface [K]
    Jq : average heat flux [mW m**-2]
    A : average heat productivity [microW m**-3]
    K : coefficient of thermal conductivity [W m**-1 K**-1]

    Assumptions
    -----------
    TODO

    Returns
    -------
    The temperature in K, a floating point number
    """

    return T0 + ((Jq / K) * (z - z0)) - ((A / (2 * K)) * (z - z0)**2)


def thermal_conductivity(T, K_0):
    """ Estimate the temperature-dependent thermal conductivity based on
    the model of Druham et al. (1987)

    Parameters
    ----------
    T : absolute temperature at Earth surface [K]
    K_0 : conductivity at the surface [mW m**-2] (for T=273 K)

    Assumptions
    -----------
    TODO

    - only reliable for temperatures below 1000 K (at higher values
    the radioactive component must be included)

    Returns
    -------
    The thermal conductivity in W m**-1 K**-1, a floating point number
    """

    second_term = 618.241 / T
    third_term = K_0 * ((255.576 / T) - 0.30247)

    return 2.26 - second_term + third_term
