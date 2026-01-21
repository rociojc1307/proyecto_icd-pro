# proyecto_icd-pro

Informe:

Título: "La odisea de los más vulnerables"

Asignaturas: Introducción a la Ciencia de Datos e Introducción a la Programación 

Introducción:
La decadencia de la economía cubana es cada vez más notable y el pueblo la sufre.
Por tal motivo, nos preguntamos cuánto se tendría que invertir para suplir el déficit de los productos que conforman la canasta familiar normada y otros que se pudieran necesitar.
Con el propósito de analizar el comportamiento de los precios de diversos artículos en mipymes, tiendas en dólares (USD) y en moneda libremente convertible (MLC) ubicadas en Plaza de la Revolución, se realizó el presente estudio en el período comprendido desde el 30 de octubre hasta el 8 de diciembre del 2025, para ver cómo influyen los mismos en el nivel adquisitivo del sector más vulnerable (jubilados y asistenciados) en el municipio que posee la población más envejecida de la capital.

Método:
El universo del estudio estuvo constituido por:
  -> 30 mipymes  
  -> 4 tiendas en dólares:  
    - 1 perteneciente a TRD
    - 3 pertenecientes a CIMEX
    - 1 tienda en MLC perteneciente a Panamericana
    
Técnicas y procedimientos:
  -> Obtención de los datos:
    - En cada uno de los establecimientos visitados e incluidos en el estudio, expliqué el objetivo del mismo y obtuve autorización para fotografiar los productos y sus precios.
    - Decidimos tomar en cuenta aquellos productos de la canasta familiar normada (arroz, frijoles, leche, pollo, aceite, azúcar, café, sal, compota, detergente, jabón y pasta dental), así como otros que previamente también se comercializaban en las bodegas (pastas alimenticias y huevos) y por último, pero no menos importantes algunos fundamentales para el adulto mayor, ya sea para aquellos que requieren de una dieta blanda o para los que padecen de incontinencia urinaria (avena, gelatina, jugo, maicena y culeros). De todos estos productos se tomaron para realizar el análisis los precios más económicos que pudimos encontrar por establecimiento. Aunque en el caso de la pasta dental utilizamos especialmente la marca Colgate por ser la más común. En el caso de los frijoles tomamos los negros; de la leche, la que es en polvo; del aceite, el de soya, y del jabón, el de tocador; por ser los tipos comunes a tiendas y bodegas. 
      Debe tenerse en consideración que para realizar la comparación del precio de los productos comunes a los 3 tipos de establecimientos se tuvo en cuenta que el producto y la cantidad fueran los mismos, no así la marca, porque no fue posible encontrar tal coincidencia.
    - Mediante una carta de solicitud de información a varias instituciones, como la ONEI provincial y la Dirección Provincial de Trabajo y Seguridad Social, firmada por la decana de la facultad, pudimos acceder a datos útiles:
      ~ La población de más de 60 años en La Habana en diversos años (ONEI)
      ~ La población del municipio por grupos etarios en el 2024 (ONEI)
      ~ Jubilación mínima y asistencia social (Dirección Provincial de Trabajo y Seguridad Social)
      ~ Población total en el municipio (2025) (ONEI)
      ~ Cantidad de jubilados, jubilados reincorporados y asistenciados (2025) (Dirección Provincial de Trabajo y Seguridad Social)
    - Al visitar la bodega donde compro la canasta normada de mi hogar, pude solicitar los precios y cantidades de los productos que allí se comercializan (“Precios establecidos para productos de la canasta familiar normada”, regulados por el Ministerio de Comercio Interior (MINCIN)). 
    - En el sitio web de la ONEI pude obtener el rango de precios en el que deberían ser vendidos algunos de los productos analizados (el resto no aparece en el documento).
    - En el canal de WhatsApp de El Toque obtuve las tasas de cambio en el mercado informal del USD y el MLC.
    - De las páginas de Instagram y Facebook de las mipymes extraje la cantidad de seguidores, así como un video de apoyo que fundamenta la problemática económica. 
  -> Estructura de los datos:
    Decidí guardar los datos en formato Json. Lo escogí por ser relativamente sencillo estructurar todo, para posteriormente utilizarlo en los gráficos. Se adjuntan las plantillas del de las mipymes, tiendas en USD y MLC y del de las tasas de El Toque. 
    - A cada producto se le asoció un id y una categoría:
      ~ pro_1: Arroz (Granos)
      ~ pro_2: Frijoles negros (Granos)
      ~ pro_3: Frijoles colorados (Granos)
      ~ pro_4: Alubias (Granos)
      ~ pro_5: Arvejas (Granos)
      ~ pro_6: Lentejas (Granos)
      ~ pro_7: Garbanzos (Granos)
      ~ pro_8: Leche en polvo (Lácteos)
      ~ pro_9: Leche fluida (Lácteos)
      ~ pro_10: Hígado de pollo (Cárnicos)
      ~ pro_11: Paquete de pollo (Cárnicos)
      ~ pro_12: Molleja de pollo (Cárnicos)
      ~ pro_13: Paquete de pechuga de pollo (Cárnicos)
      ~ pro_14: Bistec de pechuga de pollo (Cárnicos)
      ~ pro_15: Fajitas de pechuga de pollo (Cárnicos)
      ~ pro_16: Pollo entero (Cárnicos)
      ~ pro_17: Coditos (Pastas)
      ~ pro_18: Espaguetis (Pastas)
      ~ pro_19: Aceite de girasol (Aceite)
      ~ pro_20: Aceite de oliva (Aceite)
      ~ pro_21: Aceite de soya (Aceite)
      ~ pro_22: Avena (Cereales)
      ~ pro_23: Azúcar (Otros)
      ~ pro_24: Café molido (Café)
      ~ pro_25: Huevos (Otros)
      ~ pro_26: Gelatina (Otros)
      ~ pro_27: Sal (Condimentos)
      ~ pro_28: Jugo (Bebidas) (en las tiendas que tenían más de un tipo se tomó el sabor más económico)
      ~ pro_29: Compota (Otros)
      ~ pro_30: Maicena (Cereales)
      ~ pro_31: Detergente en polvo (Detergente)
      ~ pro_32: Detergente líquido (Detergente)
      ~ pro_33: Jabón de lavar (Jabón)
      ~ pro_34: Jabón de tocador (Jabón)
      ~ pro_35: Pasta de dientes (Pasta dental)
      ~ pro_36: Culeros de adultos (Otros) (se tomó la talla)
      El id, nombre, marca, categoría, presentación, unidad de medida, origen y fecha se guardaron como strings. La cantidad y precio como int o float.
      Además, se tomaron datos específicos de cada tienda, como el nombre y la moneda (string), la ubicación con parámetros como: consejo popular y dirección (string), latitud y longitud (float).
      Los id fueron de la forma:
      ~ m + número de mipyme 
      ~ u + número de tienda de USD
      ~ ml + número de tienda de MLC
      En el caso de las mipymes también se tomó el horario, con días de apertura (lista de strings), hora de apertura y de cierre (string), si tenían servicio a domicilio (string), el número al que se podía contactar (int), las redes sociales, en especial Instagram y Facebook con el usuario y la fecha en que tomé la información (string) y la cantidad de seguidores (int). Todas las fechas siguieron el formato “día/mes/año”. Además, se agregó el sitio web (string). Cada vez que las mipymes no tenían alguno de estos parámetros se colocó null. En las tiendas de USD y MLC se añadió la cadena respectiva. 
      [mipymes_tusd_tmlc.json, precios_template.json]
    - Los datos de las tasas de cambio también se guardaron en un diccionario, el cual presenta una lista con dos ‘dict’ interiores: uno para el USD y otro para la MLC, cada uno de estos contenía una lista con diccionarios con dos llaves: fecha (string) y precio (int). Los datos se tomaron en el período ya mencionado. 
      [toque.json, toq_template.json]
    - Los precios específicos de la canasta familiar normada también se guardaron en un diccionario que contenía una lista con diccionarios para cada producto. Se puso de cada uno: el nombre (string), la unidad de medida (string), la cantidad solo en el café, la pasta dental y el jabón (int) y el precio (float).
      [precios_canasta.json]
    - Los precios máximos y mínimos establecidos por la ONEI para La Habana se registraron en otro diccionario, el cual contiene una lista llamada productos con varios diccionarios para todos los productos: se incluyen las llaves variedad, unidad de medida (string), precio máximo y mínimo (float) y cantidad (int) solo para el café y los huevos. En la fuente no aparecen todos los productos analizados en el proyecto.
      [precios_max_min.json]
    - En otro diccionario se registran datos adicionales, como el porcentaje histórico la población habanera de más de 60 años, lo cual se guarda específicamente en diccionarios dentro de una lista (el año y el porcentaje son int). Además, las pensiones para sectores vulnerables (int) que son un diccionario que contiene dos llaves, para la jubilación mínima y la asistencia social. Así como otro diccionario con datos específicos de Plaza de la Revolución (2025), como la población total (int), cantidad de personas por grupos vulnerables (int) (se incluyen los jubilados y los reincorporados y los asistenciados), la estructura etaria al cierre del año 2024 (una lista de diccionarios) dividida por tres rangos de edad: el primero el de los más jóvenes, el segundo de la mayor parte de la población laboralmente activa y el tercero el que contiene fundamentalmente a los jubilados. El rango se guardó como string y la población como int.
      [datos_extras.json]
  -> Procesamiento de los datos:
    - La primera es para obtener la información de los Json que hice para guardar los datos. El encoding permite que las ñ o tildes se reconozcan. 'r' porque sólo busco leer los archivos. Esta función recibe la dirección de cada Json.
    - La segunda para calcular el promedio. Recibe una lista. En el caso de la lista esté vacía devuelve cero directamente para evitar la división por cero. Convierte directamente cada elemento de la lista a float antes de pasar a calcular y devuelve un resultado redondeado a dos números después de la coma. Utilicé las funciones sum y len de Python.
    - La tercera para calcular el valor más usual entre varios elementos. Recibe una lista. En el caso de la lista esté vacía devuelve un "". Creé un diccionario llamado frecuencias para registrar precios (keys) y cantidades (values). Convertí cada precio a float y lo redondeé a dos números después de la coma. El método .get() me permitió modificar eficazmente la cantidad de veces que cada precio se repetía. Si era la primera vez que aparecía les asignaba 0 y sumaba 1. Si no hay frecuencias también devuelve "". Accediendo a los items de frecuencias pudimos obtener el precio que más se repetía.
    - La cuarta para calcular la tasa de cambio promedio para el USD y para el MLC. Utiliza directamente la función de promedio que creé anteriormente. Recibe los datos del json de El Toque y la moneda. Primero creé una lista llamada tasas para registrar todos los valores. En dependencia de la moneda elegida, busca especialmente la lista de registros, de los cuales posteriormente toma los precios.
    - La quinta permite tomar los datos del cambio informal de las divisas en fechas determinadas. Recibe las monedas y fechas deseadas. Primero creé dos listas: fechas y precios. Mediante dos bucles while y condicionales se obtiene la información. Finalmente devuelve las fechas y precios.
    - La sexta para convertir los precios de los productos a medidas específicas:
      ~ 1 lb para los granos, aceite, azúcar y el pollo
        Cuando un producto está en gramos (g):
          precio final = precio inicial / ((cantidad / 1000) / 0.454)
        Cuando un producto está en kilogramos (kg):
          precio final = precio inicial / (cantidad / 0.454)
        Cuando un producto está en libras (lb), pero no es exactamente una:
          precio final = precio inicial / cantidad
        Cuando un producto está en mililitros (mL):
          precio final = precio inicial * 515.4 / cantidad
        Cuando un producto está en litros (L):
          precio final = precio inicial * 515.4 / cantidad * 1000
      ~ 1 kg para la sal, la leche, el detergente y los cereales
        Cuando un producto está en gramos (g):
          precio final = (1000 / cantidad) * precio inicial
        Cuando un producto está en kilogramos (kg), pero no es exactamente uno:
          precio final = precio inicial / cantidad
        Cuando un producto está en libras (lb):
          precio final = precio inicial / cantidad * 0.454
        Cuando un producto está en mililitros (mL):
          precio final = (1000 / cantidad) * precio inicial
        Cuando un producto está en litros (L), pero no es exactamente uno:
          precio final = precio inicial / cantidad
      ~ 500 g para las pastas alimenticias 
        Cuando un producto está en gramos (g), pero no son exactamente 500:
          precio final = (500 / cantidad) * precio inicial
      ~ 4 oz (onzas) para el café
        Cuando un producto está en gramos (g):
          precio final = (precio inicial / cantidad) * 4 * 28.3495
      ~ 1 L para el jugo
        Cuando un producto está en mililitros (mL):
          precio final = (1000 / cantidad) * precio inicial
        Cuando un producto está en litros (L), pero no es exactamente uno:
          precio final = precio inicial / cantidad
      ~ 200 mL para las compotas
        Cuando un producto está en gramos (g):
          precio final = (precio inicial / cantidad) * 200
      ~ 115 g para el jabón
        Cuando un producto está en gramos (g), pero no son exactamente 115:
          precio final = (115 / cantidad) * precio inicial
      ~ 85 mL para la pasta dental
        Cuando un producto está en gramos (g):
          precio final = (85 / cantidad) * precio inicial
        Cuando un producto está en mililitros (mL), pero no son exactamente 85:
          precio final = (85 / cantidad) * precio inicial
      ~ 100 g para la gelatina
        Cuando un producto está en gramos (g), pero no son exactamente 100:
          precio final = (100 / cantidad) * precio inicial
      Toma de cada producto: el nombre, categoría, presentación, cantidad, unidad de medida, precio (este se convierte a float). Posteriormente devuelve el nuevo precio redondeado a dos números después de la coma
    - La séptima utiliza la función conversor para obtener los precios en las medidas deseadas. Recibe los datos del Json de las tiendas y la moneda en que se desean conocer los precios. Así como el precio promedio del dólar y el mlc. Creé la lista análisis para guardar en un diccionario el nombre de la tienda, la moneda original y los precios en la escogida. Devuelve análisis.
    - La octava recibe la tienda deseada. Mediante una función interior se crean listas para cada producto dentro de una. Devuelve la lista principal con todos los precios.
      * Producto y su posición:
        ~ 0: Arroz 
        ~ 1: Frijoles 
        ~ 2: Lácteos 
        ~ 3: Cárnicos 
        ~ 4: Pastas
        ~ 5: Aceite 
        ~ 6: Avena
        ~ 7: Azúcar 
        ~ 8: Café 
        ~ 9: Huevos 
        ~ 10: Gelatina 
        ~ 11: Sal
        ~ 12: Jugo 
        ~ 13: Compota 
        ~ 14: Maicena 
        ~ 15: Detergente 
        ~ 16: Jabón 
        ~ 17: Pasta dental 
        ~ 18: Culeros de adultos 
    - La novena permite hallar ciertos parámetros estadísticos de los precios en los 3 tipos de tiendas: promedio, mínimo y máximo valor registrado y moda. Partimos de una lista de productos (la misma posición de la función anterior) y creamos el diccionario resultados. 
    - La décima fue para calcular el precio que tendría una canasta normada si se comprara en una mipyme o en una tienda en USD. Se agrega la lista filtro para saber exactamente cuáles son los productos. Utiliza específicamente la moda de precio. Devuelve la suma.
    - La oncena permite obtener los precios individuales de los productos anteriores. El filtro es el mismo. Guarda los precios en un diccionario. Utiliza la moda.
    - La duodécima fue para ver si existía alguna relación entre tener redes sociales (Instagram y Facebook) para promocionar una mipyme y los precios de los productos.
    - La decimotercera permite analizar si los establecimientos respetan los precios máximos que dicta la ley. Guarda los topes en un diccionario. Agregué un diccionario denominado conversión donde las keys son los nombres de los productos de las mipymes y los values los de la ONEI. Facilitó obtener los datos. Nuevamente se usa la moda. No se llega a comparar en sí, pero se utiliza para ello.

Conclusiones:
  -> Al analizar el comportamiento de los precios de los productos comunes a los tres tipos de establecimientos, se observó que las mipymes ofrecían los mejores precios, a excepción del café que resultó ser más económico en la de MLC.
  -> Aquellas mipymes con redes sociales tienen precios más altos. 
  -> Si se fueran a obtener los productos de la canasta básica en las mipymes sería más ventajoso en comparación con las tiendas en USD.
  -> De manera general se incumple en las mipymes con los precios topados por el Estado.
  -> Ni la jubilación mínima ni la asistencia social cubren las necesidades básicas de las personas.
  
Recomendación: Establecer mecanismos de control efectivos que garantizar que se cumplan los precios topados, para así impedir que la adquisición de productos básicos se convierta en una odisea
