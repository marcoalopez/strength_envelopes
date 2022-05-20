# ============================================================================ #
#                                                                              #
#    Strenght envelopes                                                        #
#    A Python script for plotting lithosphere and crust strength envelopes     #
#                                                                              #
#    Copyright (c) 2020-present   Marco A. Lopez-Sanchez                       #
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
#        Python version 3.6 or higher                                          #
#                                                                              #
# ============================================================================ #

import numpy as np
from types import SimpleNamespace


def quartz(flow_law=None):
    """Curated list of experimentally derived values defining quartz flow laws.

    flow_law : string or None
        the flow law parameters to use, either...

    Returns
    -------
    A SimpleNamespace object containing the stress exponent (n),
    the activation energy (Q) [J mol**-1], the material
    constant (A) [MPa**-n s**-1], and the reference.
    """

    if flow_law is None:
        print('Available flow laws:')
        print("'HTD' from Hirth et al. (2004)")
        print("'LP_wet' from Luan and Paterson (1992)")
        print("'GT_wet' from Gleason and Tullis (1995)")
        print("'HK_wet' from Holyoke and Kronenberg (2010)")
        print("'RB_wet' from Rutter and Brodie (2004)")
        return None

    elif flow_law == 'HTD':  # from Hirth et al. (2001)
        n = 4.0          # stress exponent
        E = 135000       # activation energy [J mol**-1]
        A = 10**(-11.2)  # material parameter [MPa**-n s**-1]
        ref = 'Hirth et al. (2004)'

    elif flow_law == 'LP_wet':  # from Luan and Paterson (1992)
        n = 4.0
        E = 152000
        A = 10**(-7.2)
        ref = 'Luan and Paterson (1992)'

    elif flow_law == 'GT_wet':  # from Gleason and Tullis (1995). Wet quartzite.
        n = 4.0
        E = 223000
        A = 1.1e-4
        ref = 'Gleason and Tullis (1995)'

    elif flow_law == 'HK_wet':  # Holyoke and Kronenberg (2010), based on Gleason and Tullis (1995) data
        n = 4.0
        E = 223000
        A = 5.1e-4
        ref = 'Holyoke and Kronenberg (2010)'

    elif flow_law == 'RB_wet':  # from Rutter and Brodie (2004). Wet quartzite, minor grain boundary sliding inferred.
        n = 2.97
        E = 242000
        A = 10**(-4.93)
        ref = 'Rutter and Brodie (2004)'

    else:
        raise ValueError("Quartz flow law name misspelled. Use 'HTD', 'LP_wet', 'GT_wet', 'HK_wet' or 'RB_wet'")

    return SimpleNamespace(n=n, E=E, A=A, ref=ref)


def olivine(flow_law=None):
    """Curated list of experimentally derived values defining olivine flow laws.

    flow_law : string or None
        the flow law default parameters

    Returns
    -------
    A SimpleNamespace object containing the stress exponent (n),
    the activation energy (Q) [J mol**-1], the material constant (A)
    [MPa**-n s**-1], the activation volume per mol (V) [m**3 mol**-1],
    the water fugacity exponent (r), and the reference.
    """

    if flow_law is None:
        print('Available flow laws:')
        print("'HK_wet' from Hirth and Kohlstedt (2003)")
        print("'HK_dry' # from Hirth and Kohlstedt (2003)")
        print("'KJ_wet' from Karato and Jung (2003)")
        print("'KJ_dry' from Karato and Jung (2003)")
        print("'ZK_dry' (dry peridotite) from Zimmerman and Kohlstedt (2004)")
        print("'Faul_dry' from Faul et al. (2011)")
        print("'Ohuchi' from Ohuchi et al. (2015)")
        return None

    elif flow_law == 'HK_wet':  # from Hirth and Kohlstedt (2003). Wet Olivine
        n = 3.5        # stress exponent
        E = 520000     # activation energy [J mol**-1]
        A = 10**(3.2)  # material parameter [MPa**-n s**-1]
        V = 2.2e-05    # activation volume per mol [m**3 mol**-1]
        r = np.nan     # water fugacity exponent
        ref = 'Hirth and Kohlstedt (2003)'

    elif flow_law == 'HK_dry':  # from Hirth and Kohlstedt (2003). Dry Olivine
        n = 3.5
        E = 530000
        A = 10**(5.0)
        V = 1.8e-05
        r = np.nan  # not provided
        ref = 'Hirth and Kohlstedt (2003)'

    elif flow_law == 'KJ_wet':  # from Karato and Jung (2003). Wet olivine
        n = 3.0
        E = 470000
        A = 10**(2.9)
        V = 2.4e-05
        r = np.nan  # not provided
        ref = 'Karato and Jung (2003)'

    elif flow_law == 'KJ_dry':  # from Karato and Jung (2003). Dry olivine
        n = 3.0
        E = 510000
        A = 10**(6.1)
        V = 1.4e-05
        r = np.nan  # not provided
        ref = 'Karato and Jung (2003)'

    elif flow_law == 'ZK_dry':  # from Zimmerman and Kohlstedt (2004). Dry peridotite
        n = 4.3
        E = 550000
        A = 10**(4.8)
        V = np.nan  # activation volume per mol not provided!
        r = np.nan  # not provided
        ref = 'Zimmerman and Kohlstedt (2004)'

    elif flow_law == 'Faul_dry':  # from Faul et al. (2011). Dry olivine
        n = 8.2
        E = 682000
        A = 0.3
        V = np.nan  # activation volume per mol not provided!
        r = np.nan  # not provided
        ref = 'Faul et al. (2011)'

    elif flow_law == 'Ohuchi':  # from Ohuchi et al. (2015)
        n = 3.0
        E = 423000
        A = 10**(-4.89)
        V = 17.6e-06
        r = 1.25
        ref = 'Ohuchi et al. (2015)'

    else:
        raise ValueError("Olivine flow law name misspelled. Use 'HK_wet', 'HK_dry', 'KJ_wet', 'KJ_dry', 'ZK_dry', 'Faul_dry', or 'Ohuchi'")

    return SimpleNamespace(n=n, E=E, A=A, V=V, r=r, ref=ref)


def olivine_Idrissi(R, T, stress):
    """Semi-empirical olivine flow law for the uppermost mantle based on Idrissi
    et al. (2016). It solves the equation:

    ss = 1e6 * exp{(-566e3 / (R * T)) * [1 - sqrt(stress / 3.8)]**2}

    Parameters
    ----------
    R : scalar
        universal gas constant

    geotherm : scalar
        the temperature in K

    stress : scalar or numpy array_like
        the stress in MPa

    Returns
    -------
    the strain rate in s**-1
    """
    # convert from MPa to GPa
    stress = stress / 1000

    return 1e6 * np.exp((-556e3 / (R * T)) * (1 - np.sqrt(stress / 3.8))**2)


if __name__ == '__main__':
    print("functions loaded from 'flow_laws_params.py': \n quartz,\n olivine, \n olivine_Idrissi \n")
else:
    print('module flow_laws imported')
