##Servel-Extract
Extrayendo la información que Servel provee. Para ello, se trabaja con PDF del Servel haciendo varias pruebas, obteniendo mejores resultados con pdftotext -table

##Avances
El orden de las comunas es por el orden de creación.

| Comuna | Cantidad validad | % Valido | Cantidad erróneo | % erróneo |
|---|---|---|---|---|
| Lo Espejo | 92.875 | 99.93 | 68 | 0.07 |
| La Florida | 288.390 | 99.56 | 1.281 | 0.44 |
| Providencia | 161.909 | 99.92 | 133 | 0.08 |
| Santiago | 282.697 | 99.67 | 947 | 0.33 |
| **Total Parcial** | **825.871** | **99.71** | **2.429** | **0.29** |

####Problemas detectados: 

- Direcciones muy largas, lo cual mezcla la información entre la dirección y la circunscripción (no le veo solución)
- Nombres muy cortos (asigné una condición de distancia para buscar el guión, lo cual es facilmente corregible)
- Nombres muy largos, los cuales generan problemas para detectar el RUT.
- Direcciones con el mismo nombre de circunscripciones (por lo que la direccion y la circunscripcion generaban un conflictos de datos, pendiente de revisar)

##Fuente de ayuda
http://deerme.org/web-scraping-2/extraccion-de-datos-en-un-archico-pdf-de-forma-automatizada

