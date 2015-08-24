##Servel-Extract
Extrayendo la información que Servel provee. Para ello, se trabaja con PDF del Servel haciendo varias pruebas, obteniendo mejores resultados con pdftotext -table

##Avances
###Lo Espejo
Con el script publicado en deerme.org he comenzado a procesar la data, comenzando con Lo Espejo (comuna donde vivo). El resultado es el siguiente:
- Información correcta: 92.875 (99.93%)
- Información erronea: 68 (0.07%)

###La Florida (pendiente de subir)
Con algunas mejoras, seguí con La Florida, ya que es una comuna que posee 3 circunscripciones (Bellavista, San Jose de la Estrella y Trinidad). El resultado es el siguiente:
- Información correcta: 288.390 (99.56%)
- Información erronea: 1.281 (0.44%)

###Providencia (pendiente de subir)
- Información correcta: 161.909 (99.92%)
- Información erronea: 133 (0.08%)

###Santiago Centro (pendiente de subir)
- Información correcta: 282.694 (99.67%)
- Información erronea: 950 (0.33%)
 
####Problemas detectados: 

- Direcciones muy largas, lo cual mezcla la información entre la dirección y la circunscripción (no le veo solución)
- Nombres muy cortos (asigné una condición de distancia para buscar el guión, lo cual es facilmente corregible)
- Nombres muy largos, los cuales generan problemas para detectar el RUT.
- Direcciones con el mismo nombre de circunscripciones (por lo que la direccion y la circunscripcion generaban un conflictos de datos, pendiente de revisar)

##Fuente de ayuda
http://deerme.org/web-scraping-2/extraccion-de-datos-en-un-archico-pdf-de-forma-automatizada

