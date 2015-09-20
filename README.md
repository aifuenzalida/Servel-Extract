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
|Cerro Navia|A1321011|115.851|99,95%|60|00,05%|115.911|
|Lo Prado|A1321012|88.918|99,91%|78|00,09%|88.996|
|Maipú|A1321013|341.319|99,43%|1.958|00,57%|343.277|
|Cerrillos|A1321014|65.856|99,39%|401|00,61%|66.257|
|La Cisterna|A1321015|82.641|99,90%|83|00,10%|82.724|
|El Bosque|A1321017|135.517|99,83%|235|00,17%|135.752|
|La Granja|A1321018|102.930|99,90%|101|00,10%|103.031|
|La Pintana|A1321019|128.180|99,80%|255|00,20%|128.435|
|San Ramón|A1321020|82.465|99,93%|55|00,07%|82.520|
|San Miguel|A1321021|95.829|99,91%|82|00,09%|95.911|
|Pedro Aguirre Cerda|A1321022|96.006|99,92%|80|00,08%|96.086|
|San Joaquin|A1321023|83.350|99,91%|73|00,09%|83.423|
|Ñuñoa|A1321025|177.940|99,84%|280|00,16%|178.220|
|Macul|A1321026|97.489|99,36%|632|00,64%|98.121|
|Peñalolen|A1321027|174.768|99,80%|354|00,20%|175.122|
|La Reina|A1321028|87.117|99,92%|74|00,08%|87.191|
|Las Condes|A1321030|236.926|99,87%|306|00,13%|237.232|
|Vitacura|A1321031|79.731|99,84%|128|00,16%|79.859|
|Lo Barnechea|A1321032|64.085|99,78%|143|00,22%|64.228|
|Puente Alto|A1322001|335.915|99,23%|2.608|00,77%|338.523|
|Pirque|A1322002|18.924|99,04%|183|00,96%|19.107|
|**Total Parcial**||**4.632.443**|**99,65%**|**16.289**|**00,35%**|**4.648.732**|

####Problemas detectados: 

- Direcciones muy largas, lo cual mezcla la información entre la dirección y la circunscripción (no le veo solución)
- Nombres muy cortos (asigné una condición de distancia para buscar el guión, lo cual es facilmente corregible)
- Nombres muy largos, los cuales generan problemas para detectar el RUT.
- Direcciones con el mismo nombre de circunscripciones (por lo que la direccion y la circunscripcion generaban un conflictos de datos, pendiente de revisar)

##Fuente de ayuda
http://deerme.org/web-scraping-2/extraccion-de-datos-en-un-archico-pdf-de-forma-automatizada
