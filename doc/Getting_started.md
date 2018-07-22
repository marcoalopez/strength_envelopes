## Getting started

To operate with the script, open the  Spyder (Anaconda) or the Canopy IDE and then open the script using ``File>Open`` in the menu bar. The script will appear in the editor as shown in Figure 1.

![Figure 1]()

#### Defining the general starting parameters

Between lines 40 and 58 you will see the following text block showing some general default values that are required for generate strength envelope models.

```python
# ==============================================================================#
# DEFAULT INPUT PARAMETERS

# Miscellanea
g = 9.80665  # average gravitational acceleration [m/s**2]
R = 8.3144598  # universal gas constant [J mol**-1 K**-1]

# Mechanical constants (CAUTION! these are global variables and thus changing their values will affect the different functions)
ro_crust = 2750  # average rock density in the crust [kg/m**3]
ro_mantle = 3330  # average rock density in the mantle [kg/m**3]
ref_sr = 1.0e-14  # Reference average shear strain rate in the ductile lithosphere [s**-1]; see Twiss and Moores (2007, p.488)
moho = 34.4  # Average continental crust thickness [km] (Huang et al. 2013)
LAB = 81  # Average lithosphere-asthenosphere boundary (LAB) [km] beneath tectonically altered regions (Rychert and Shearer, 2009)

# set plot style
plot_style = 'ggplot'
mpl.style.use(plot_style)
# you can use other styles as well, see the following gallery:
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html
# ==============================================================================#
```



>  👉 The reference average shear strain rate value is used as a default value by some functions in the script, for example those that involve deformation due to dislocation creep. Later, you will see that such functions allows you to "override" this value and set any other strain rate when required. So, do not modify this value to see how different strain rates affect the strength of the lithosphere, this will be done using a specific method to do this.

### Running the script

To interact with the script and create lithospheric strength envelopes it is necessary to run the script. For this, click on the green "play" icon in the tool bar or go to `Run>Run file` in the menu bar.  The followin text will appear in the Python shell or console:

```
======================================================================================
Welcome to Strength envelopes script v1.0
======================================================================================

Strength envelopes is a free open-source cross-platform script to generate strength
envelopes.

METHODS AVAILABLE
====================  ================================================================
Main Functions        Description
====================  ================================================================
fric_strength         Plot frictional slopes
stable_geotherm       Estimate and plot a steady-state geothermal gradient
qtz_disloc_creep      Plot dislocation creep flow laws for quartz
ol_disloc_creep       Plot dislocation creep flow laws for olivine

======================  ==============================================================
Other functions
====================  ================================================================
triple_point          Plot the Al2SiO5 triple point (Holdoway or Pattison)
goetze_line           Plot the Goetze criterion
granite_solidus       Plot granite solidus (wet and dry)
peridotite_solidus    Plot peridotite solidus NOT YET IMPLEMENTED!
borehole_data         Plot temperature gradients from superdeep boreholes
====================  ================================================================

You can get information on the different methods by:
    (1) Typing the command help in the console as follows: help(name of the function)
        e.g. >>> help(stable_geotherm)
    (2) In the Spyder IDE by writing the name of the function and clicking Ctrl+I
    (3) Visit script documentation at https://github.com/marcoalopez/Strength_envelopes


EXAMPLES
--------
Initialize a doble plot (diff. stress vs depth and tempretaure vs depth)
fig, (ax1, ax2) = init_plot()

Initialize a single plot (diff. stress vs depth)
fig, ax1 = init_plot(True)

For more examples see documentation or use help(function_name)
```

To initialize



Also a new window with an empty figure will appear. Specifically, a plot with a differential stress vs depth and another with a temperature vs depth (Fig. 2).

![Figure 2]()

### Estimate the strength in the brittle crust: the Anderson model

Lithosphere breakage and tectonic earthquakes seldom occur, if ever, by the appearance and propagation of a new fault but by sudden slippage along a pre-existing fault or plate interface (Scholz, 1998)

The... Byerlee's law establish that frictional strength is independent of rock type (leaving aside slates), temperature and strain rate. Anderson... normal faults are favoured by gravitational acceleration, thrust faults have to counteract gravitational acceleration, and strike-slip faults are more or less independent of gravitational acceleration. This means that

To generate frictional slopes with the script...:

```python
fric_strength(z=15, fault_type='strike-slip')
```

This function requires to enter at least the parameter ``z``, which is the maximum depth in km. Optional parameters include the fault type ``fault_type`` that can be defined as ``'inverse'``, ``'normal'`` or ``'strike-slip'``, the coefficient of friction ``mu``, the Hubbert-Rubbey coefficient of fluid pressure ``lamb``, and the internal cohesion of rock ``C0``. Default values are shown in Table X below. You can also define the aesthetics of the elements in the plot by using matplotlib standard commands such as ``color``, ``linewidth``, ``linestyle``, ``alpha``, etc., or make some annotations using ``annot``, see later for examples. For additional information use ```help(fric_strength)``` in the console. If the fault type is not declared ``strike`` is used by default. For example, the following random combinations are possible:

```python
# all values by default ()
fric_strength(z=10)

# defining fault type and coefficient of friction
fric_strength(z=15, fault_type='thrust', mu=0.5)

# defining fault type and coefficient of fluid pressure
fric_strength(z=15, fault_type='normal', lamb=0.1)

# defining different coefficients and setting the color of the line to plot
fric_strength(z=15, mu=0.6, lamb=0.4, C0=40, color='red', linewidth=2)

# or just any other combination
```

Goetze criterion

### Estimate the geothermal gradient

The equation that relate stress and permanent deformation (strickly speaking strain rate) due to dislocation creep depend strongly on the temperature. Hence, to estimate rock strength envelopes using dislocation creep flow laws, we need first to estimate the geothermal gradient. The script contains a function named ```stable_geotherm``` that calculates and plot a stable geotherm for the continental lithosphere based on the two-layer model of Turcotte and Schubert (1982). This model separate the thermal behaviour of the crust and the lithospheric mantle.

In the ```stable_geotherm``` function, all the parameters to enter are optional and a geotherm can be obtained by calling the function and saving the results in a variable to use later as follows:

```python
my_model = stable_geotherm()

# the following information will appear in the console (results can be change depending on your starting constrains such as the location of the moho, etc.)
ACCORDING TO THE MODEL:
The T at the base of the moho is 669.7 [deg C]
The T at the lithosphere-asthenosphere boundary is 1139.4 [deg C]
The average temperature gradient in the crust is 25.9 [K km-1]
The average temperature gradient in the lithospheric mantle is 10.15 [K km-1]
```
>  👉 Variable names in Python can contain upper and lowercase letters (the language is case-sensitive), digits and the special character *_*, but cannot start with a digit. In addition, there are some special keywords reserved for the language (e.g. True, False, if, else, lambda, etc.). Do not worry about this when choosing variable names, the shell will highlight the word if you are using one of these. 

After pressing the enter key you will see the geotherm estimated in the *T* vs depth plot (Fig. X) and some information according to the model including the temperatures at the base of the moho and the LAB, and the average temperature gradients for the crust and the lithospheric mantle.

[Figure]()

The variable ```my_model``` contains two lists/arrays of values, one with the temperature variation with depth in *K* degrees and other with the corresponding depths in meters.

The script has several functions to test whether the geotherm estimated is feasible for your study case (i.e. compatible or not with field data) (Fig. X). These include:

- a projection of the Al~2~SiO~4~ triple point (Holdoway or Pattison)
- a projection of the granite solidus for wet (saturated) and dry conditions
- a projection of the peridotite solidus for wet (saturated) and dry conditions
- a projection of superdeep borehole data including the Kola, KTB, and Gravberg boreholes

Some examples below:

```python
triple_point('Holdoway')  # can be 'Pattison' instead 
granite_solidus()
peridotite_solidus()  # not yet implemented
borehole_data('KTB')  # can be 'Kola' or 'Gravberg' instead
```

[Figure]()

Figure X above show that according to the geotherm calculated there will be no magma generation in a dry crust nor andalusite or sillimanite in equilibrium within the whole crust. The temperature at the LAB is also close to the peridotite melting point at GPa (81 km) according to the models that predict...TODO

The default values used by the ```stable_geotherm``` function can be modified to generate different geotherms. First by defining different depths for the moho and the lithosphere-asthenosphere boundary, and second by defining different thermal parameters. Specifically, the following parameters can be modified:

- the temperature at surface [in K]. The default is set to 280.65 (7.5 °C) taken from the KTB borehole.
- the average thermal parameters for the crust and the lithospheric mantle that includes:
    - the average heat flux $$J_q$$ [$mW m^-2$]
    - the average rate of radiogenic heat production $$A$$ [$\mu W m^{-3}$]
    - the coefficient of thermal conductivity $$K$$ [$W m^{-1} K^{-1}$]



**Table X**. Default average thermal values for the crust and the lithospheric mantle
|                       | crust |          reference           | lithos. mantle |       reference       |
| :-------------------: | :---: | :--------------------------: | :------------: | :-------------------: |
|   **Jq** [mW m^-2^]   | 65.0  | Jaupart and Mareschal (2007) |      34.0      | Sclater et al. (1980) |
|   **A** [µW m^-3^]    | 0.97  |     Huang et al. (2013)      |      0.01      | Sclater et al. (1980) |
| **K** [W m^-1^ K^-1^] | 2.51  |    Sclater et al. (1980)     |      3.35      | Sclater et al. (1980) |

The table X show the values used by default in the ```stable_geotherm``` function and the corresponding references. As an example, if we set the average heat flux of the crust to 85 mW m^-2^ and the surface temperature to 273.15 K (0 °C):

```python
Hhf_model = stable_geotherm(T_surf=273.15, crust_params=(85, 0.97, 2.51))

# - T_surf for the temperature at surface
# - crust_params and/or mantle_params in the form (Jq, A, K)

ACCORDING TO THE MODEL:
The expected T at the base of the moho is 936.2 [deg C]
The expected T at the lithosphere-asthenosphere boundary is 1409.2 [deg C]
The average temperature gradient in the crust is 33.86 [K km-1]
The average temperature gradient in the lithospheric mantle is 10.15 [K km-1]
```

[Figure]()

In contrast to the first geotherm, the new one cross the Kyanite-Sillimanite around 17 km depth and the granite melting point for wet conditions between 21-22 km. Still, the geotherm never cut the granite solidus for dry conditions implying no magma generation in a dry lower crust.

> :point_right: Tip: see the depths in detail just select the lens icon and zoom in on the desired area. To reset the original view click on the house icon.

Later, in section x.x we will see examples of how different geotherms affect the strength of the lithosphere.



### Estimate the strength of the plastic crust and the mantle lithosphere

A simplistic lithospheric deformation model assume that lithosphere or at least the continental crust deforms mainly through planar zones of intense deformation known as faults or shear zones. In such zones, the presence of fine-grained rocks mainly deformed by crystal-plastic mechanisms, known as mylonites, are the most characteristic feature. Most studies indicate that dislocation creep is the dominant mechanism of deformation in mylonites. Hence, we usually assume dislocation creep flow laws for describing deformation in both the "ductile" crust and mantle. Experimental data for a wide range of conditions usually fits a relation of the form:
$$
\epsilon = A \space \sigma^n \space d^{-m} \space f_{H_2O}^r \space e^{(Q + pV)/RT}
$$
Where:

$$\epsilon$$ is the strain rate in $$s^{-1}$$

$$A$$ is the material constant determined experimentally in $$MPa^{-n} s^{-1}$$

$$\sigma^n$$ is the differential stress in $$MPa$$

$$d$$, $$m$$ are the average grain size in $$\mu m$$ and the grain size exponent, respectively

$f_{H_2O}$, $r$ are the water fugacity (water molecules per 1e6 Si atoms) and the water fugacity exponent, respectively

$$e^{(Q + pV)/RT}$$ is the Arrhenius-type temperature dependence that include the activation energy $$Q$$, the pressure $$P$$, the volume activation per mol $$V$$, the universal gas constant $$R$$, and the absolute temperature $$T$$ in K. For more details use ``help(power_law_creep)`` in the console.



(match nomenclature on the script!) *Further, we also assume that few mineral phases dominates rocks in the crust and the litospheric mantle in crustal-scale shear zones are quartz and feldspar.* For simplicity, we generally assume that dislocation creep in quartz and olivine dominates deformation in the crust and the lithospheric mantle respectively.

To estimate and plot the strength of a continental based on quartz and dislocation creep we have to call the ```qtz_disloc_creep``` function. For example:

```python
qtz_disloc_creep(z0=9.5, geotherm=my_model, law='HTD' label='Hirth et al.')
# we define the parameter "label" to later show in a legend the flow law used using:
ax1.legend(loc='lower right')
```

This function requires to enter at least two parameters: ``z0``, which is the starting depth in km, and the ``geotherm``. Optional parameters include different flow law calibrations ``law`` (see Table X), the strain rate ``strain_rate``, the mean grain size ``d`` and the grain size exponent ``m``, and the water fugacity ``fug``and water fugacity exponent ``r``. The effect of confining pressure is ignored at crustal depths. Finally, you can define the aesthetics of the elements in the plot by using matplotlib standard commands such as ``color``, ``linewidth``, ``linestyle``, ``alpha``, etc. For additional information just use ```help(qtz_disloc_creep)``` in the console. If the flow law calibration is not declared, the Hirth et al. (2001) calibration is used by default.

[Figure]()

|   name   |          reference          |  n   | Q [J mol^-1^] | A [MPa^-n^ s^-1^] |
| :------: | :-------------------------: | :--: | :-----------: | :---------------: |
|  'HTD'   |     Hirth et al. (2001)     | 4.0  |    135e^3^    |     10^-11.2^     |
| 'LP_wet' |   Luan & Paterson (1992)    | 4.0  |    152e^3^    |     10^-7.2^      |
| 'GT_wet' |   Gleason & Tullis (1995)   | 4.0  |    223e^3^    |     1.1e^-4^      |
| 'HK_wet' | Holyoke & Kronenberg (2010) | 4.0  |    223e^3^    |     5.1e^-4^      |
| 'RB_wet' |   Rutter & Brodie (2004)    | 2.97 |    242e^3^    |     10^-4.93^     |

Olivine...briefly explain...

The procedure to estimate the strength of the lithospheric mantle is similar excepting that you do not have to enter the starting depth since this is already defined by the depth of the moho and that the names of the dislocation creep flows laws for olivine are different from those of quartz (see Table X for a list of names). To call this function just write in the console:

```python
ol_disloc_creep(geotherm=my_model, law='KJ_dry', label='Karato & Jung')
```

|    name    |          reference           |  n   | Q [J mol^-1^] | A [MPa^-n^ s^-1^] | V [m^3^ mol^-1^] |
| :--------: | :--------------------------: | :--: | :---------: | :-----------: | :--------------: |
|  'HK_wet'  |   Hirth & Kohlstedt (2003)   | 3.5  |   520e^3^   |    10^3.2^    |     2.2e^-5^     |
|  'HK_dry'  |   Hirth & Kohlstedt (2003)   | 3.5  |   530e^3^   |    10^5.0^    |     1.8e^-5^     |
|  'KJ_wet'  |     Karato & Jung (2003)     | 3.0  |   470e^3^   |    10^2.9^    |     2.4e^-5^     |
|  'KJ_dry'  |    Karato and Jung (2003)    | 3.0  |   510e^3^   |    10^6.1^    |     1.4e^-5^     |
|  'ZK_dry'  | Zimmerman & Kohlstedt (2004) | 4.3  |   550e^3^   |    10^4.8^    |       ---        |
| 'Faul_dry' |      Faul et al. (2011)      | 8.2  |    682e3    |      0.3      |       ---        |

We are done for now :)
