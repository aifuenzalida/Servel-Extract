##Servel-Extract
Extrayendo la información que Servel provee. Para ello, se trabaja con PDF del Servel haciendo varias pruebas, obteniendo mejores resultados con pdftotext -table

##Avances
#Lo Espejo
Con el script publicado en deerme.org he comenzado a procesar la data, comenzando con Lo Espejo (mi comuna).
El resultado es el siguiente:
Información correcta: 92.875 (99.93%)
Información erronea: 68 (0.07%)
Problemas detectados: 
- Direcciones muy largas, lo cual mezcla la información entre la dirección y la circunscripción (no le veo solución)
- Nombres muy cortos (asigné una condición de distancia para buscar el guión, lo cual es facilmente corregible)
- Direcciones con el mismo nombre de circunscripciones (por lo que la direccion y la circunscripcion generaban un conflictos de datos, pendiente de revisar)

#Fuente de ayuda
http://deerme.org/web-scraping-2/extraccion-de-datos-en-un-archico-pdf-de-forma-automatizada

