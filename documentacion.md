# Gradiente de temperatura en la litosfera: cálculo de la *geoterma* estable

La temperatura es una variable esencial en la leyes constitutivas del flujo que describen el comportamiento plástico de los materiales cristalinos y por tanto para el calculo del esfuerzo necesario para deformar un material policristalino plásticamente. Como veremos a continuación, estimar la variación de la temperatura con la profundidad no es sencillo dado que las fuentes que generan calor y las propiedades térmicas de los materials cambian tanto en profundidad como lateralmente.

Aunque existen medidas directas del gradiente geotérmico en numerosos lugares del mundo, la mayoría presentan una limitación muy clara en cuanto a la profundidad, situandose la mayoría por debajo de los 5 km. De hecho, hasta ahora solo existen datos del gradiente geotérmico para la corteza continental superior (zona sismogénica), justamente donde las leyes de flujo que describen el comportamiento plástico de las rocas no aplican de manera generalizada. Además, se ha observado que los gradientes de temperatura en las partes más superficiales de la corteza pueden estar perturbados en gran medida por la historia geologica reciente (p. ej. casquetes de hielo...).... Los datos reales más fiables que tenemos proceden de sondeos superprofundos. Específicamente del sondeo ruso *Kola superdeep* que alcanzó los 12262 m (Kozlovsky, 1987), el alemán *KTB superdeep borehole* que alcanzó los 9101 m (Emmermann y Lauterjung, 1997), y los sondeos suecos *Gravberg-Stenberg boreholes* que alcanzarón un máximo de 6779 m (Lund y Zoback, 1999). Los gradientes obtenidos en estos sondeos profundos muestran que los gradientes dentro de la corteza continental presentan valores diferentes. Así, aunque los sondeos *Kola* y *Gravberg-1* mostraron gradientes bastante similares, de 15.5 y 16.1 K/km respectivamente (Lund y Zoback, 1999; Smithson et al. 2000). El sondeo *KTB* presentó un gradiente muy superior de 27.5 K/km (Emmermann y Lauterjung, 1977), alcanzando una temperatura de ~ 265 °C a los 9.1 km.

La extrapolación lineal de estos gradientes de temperature en profundidad conducen a temperaturas inadmisibles (Fig. X). Por ejemplo...TODO. Esto significa que tenemos que buscar un modelo que tenga en cuenta cómo **cambia del gradiente de temperatura con la profundidad** y que esté además de acuerdo con los datos (geofísicos) sobre estructura de la litósfera y (petrológicos) de los puntos de fusión de rocas representativas determinados experimentalmente. La limitaciones más fiable que tenemos para estos modelos en la litósfera son:

 se sitúa en la base de la litosfera, la cual coincide con la zona de baja velocidad caracterizada por la fusión parcial...TODO Otras limitaciones útiles en el espacio *P-T* serían los campos de estabilidad de los aluminosilicatos, las líneas del *solidus* del granito o las peridotitas...TODO

 - La base de la litósfera se caracteriza por una cambio abrupto en la velocidad de las ondas sísmicas, denominada capa de baja velocidad o astenosfera. Esta zona se extiende a profundidades que van de los 70 a los 250 km. Según el conocimiento actual, este límite abrupto representa una zona de transición entre una peridotita sólida (manto litosférico) y una peridotita que presenta un pequeño porcentaje de fundido (manto astenoférico). De acuerdo con los datos petrológicos (Kushiro et al., 1968), a presiones típicas a 70 km de profudidad las peridotitas alcanzarían su punto de fusión en del rango de temperaturas 1000-1330 °C (fusión en condiciones de exceso de agua y secas respectivamente).

 - Dentro de la corteza continental, ...TODO

 - La presencia de polimorfos de Al2SiO5 (andalucita, cianita, y sillimanita), relativamente comúnes en rocas metamórficas, es también un buen criterio limitador...TODD

### Fuentes generadoras de calor

### Cálculo de la geoterma estable

Ley de conducción del calor de Fourier (Fourier, 1816)...TODO

Como aquí consideramos que el gradiente de temperatura en un momento dado (dt = 0), podemos considerar que este gradiente es estable. En este caso, una de las aproximaciones más utilizadas para modelizar el gradiente usa las series de Taylor y la ecuación de Laplace (**mirar!**) (Turcotte and Schubert, 1982) que una vez resuelta presenta la siguiente forma:

ecuación [2]


El primer término de esta ecuación describe la temperatura en la superficie de la Tierra. El segundo término (primera derivada) describe la variación de temperatura con la profundidad, es decir, el gradiente. El tercer término (segunda derivada) incluye la variación del gradiente de temperatura con la profundidad. Los dos primeros términos extrapolan linealmente la temperatura en profundidad y por tanto conducen a una sobreestimación de la misma con la profundidad. El tercer término es el que nos permite variar el gradiente e incluir por ejemplo la variación en la distribución causada por una producción desigual de calor debida al contenido en elementos radioactivos.
