##Servel-Extract
Extrayendo la información que Servel provee. Para ello, se trabaja con PDF del Servel haciendo varias pruebas, obteniendo mejores resultados con pdftotext -table<br>
Todos los datos fueron solicitados a Servel por medio de la Ley de Transparencia, y los PDF con el listado original lo pueden descargar deste este link: https://mega.nz/#F!UNEHxLjJ!rkoE4qHLvhhIo0KM6JLMZw<br>
(La info no está disponible de momento en Servel.cl)

##Avances
El orden de las comunas es por el orden de creación.

|Comuna|Codigo|Cantidad validad|% Valido|Cantidad erróneo|% erróneo|Total datos|
|---|---|:---:|:---:|:---:|:---:|:---:|
|Lo Espejo|A1321016|92.875|99,93%|68|00,07%|92.943|
|La Florida|A1321024|288.390|99,56%|1.281|00,44%|289.671|
|Providencia|A1321029|161.909|99,92%|133|00,08%|162.042|
|Santiago|A1321001|282.697|99,67%|947|00,33%|283.644|
|Colina|A1320001|66.864|97,44%|1.759|02,56%|68.623|
|Lampa|A1320002|41.686|99,67%|140|00,33%|41.826|
|Tiltil|A1320003|12.751|99,72%|36|00,28%|12.787|
|Independencia|A1321002|78.550|99,87%|105|00,13%|78.655|
|Recoleta|A1321003|135.702|99,56%|597|00,44%|136.299|
|Estacion Central|A1321004|127.082|99,77%|290|00,23%|127.372|
|Conchali|A1321005|119.160|99,91%|113|00,09%|119.273|
|Huechuraba|A1321006|61.331|99,21%|491|00,79%|61.822|
|Quilicura|A1321007|111.995|98,71%|1.460|01,29%|113.455|
|Renca|A1321008|109.902|99,81%|205|00,19%|110.107|
|Quinta Normal|A1321009|99.685|99,85%|153|00,15%|99.838|
|Pudahuel|A1321010|150.107|99,77%|342|00,23%|150.449|
|**Total Parcial**||**1.940.686**|**99,58%**|**8.120**|**00,42%**|**1.948.806**|

####Problemas detectados: 

- Direcciones muy largas, lo cual mezcla la información entre la dirección y la circunscripción (no le veo solución)
- Nombres muy cortos (asigné una condición de distancia para buscar el guión, lo cual es facilmente corregible)
- Nombres muy largos, los cuales generan problemas para detectar el RUT.
- Direcciones con el mismo nombre de circunscripciones (por lo que la direccion y la circunscripcion generaban un conflictos de datos, pendiente de revisar)

##Fuente de ayuda
http://deerme.org/web-scraping-2/extraccion-de-datos-en-un-archico-pdf-de-forma-automatizada
