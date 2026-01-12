# proyecto_icd-pro

Con este proyecto buscamos centrarnos en la notoria pobreza en la que se vive en Cuba en la actualidad, siendo peor aun la situación de nuestros ancianos. Y es que como se comenta en la historia, el salario nunca será suficiente en una nación donde la inflación, la corrupción y el despojo de los valores es el pan de cada día.

El proceso de recopilación de los datos llevó varias etapas, pues tuve que agregar algunos productos estratégicos por ser necesarios para los adultos mayores. Toda la evidencia de los precios se encuentra en el repositorio. Está dividida por carpetas y el nombre de cada una coincide con el id de las mipymes. Lo mismo sucede con las tiendas en USD y MLC. 

Mediante una carta de solicitud de información a varias instituciones, como la ONEI provincial y el Ministerio de Trabajo y Seguridad Social, firmada por la decana de la facultad, pudimos acceder a datos útiles:
  ● La población del municipio elegido por grupos etarios
  ● Cantidad de jubilados, asistenciados
  ● Jubilacion y pensión mínimas 

Al visitar la bodega donde compro la canasta normada de mi hogar, pude solicitar los precios y cantidades de los productos que allí se comercializan.

En el sitio web de la ONEI pude obtener el rango de precios en el que deberían ser vendidos los productos y en el canal de WhatsApp de El Toque, las tasas de cambio en el mercado informal del USD y el MLC. De las páginas de Instagram y Facebook de las mipymes extraje la cantidad de seguidores.

Código de las funciones:
● La primera es para obtener la información de los json que hice para guardar los datos (escogí este formato por ser relativamente sencillo estructurar todo para posteriormente utilizarlo en los gráficos). Uno de estos fue para registrar los valores de los precios máximos y mínimos que aparecían en la ONEI de algunos de los productos analizados (digo algunos, porque no todos se encontraban en la fuente).
  ▪ En “datos_precios_tiendas” se registran los precios de los productos en las 30 mipymes, 4 tiendas de usd y la de mlc.
  ▪ En “datos_tasas_cambio_usd_mlc”, los valores del cambio informal del USD y MLC en El Toque.
  ▪ En “precios_max_min”, los valores máximos y mínimos mencionados anteriormente.
● La segunda para calcular el promedio. Incluí el “try – except” para evitar problemas que se presentaron al procesar algunos de los json.
● La tercera / cuarta para calcular el mínimo / máximo valor de una lista.
● La quinta para calcular el valor más usual entre varios elementos.
● La sexta para calcular la tasa de cambio promedio para el USD y para el MLC
● La séptima para convertir los precios de los productos a medidas específicas (aparecen en la historia) y también al resto de monedas. Utilice .get() para acceder a la información más eficazmente
● La octava para obtener una tupla que contenga los precios en las tiendas de los productos
● La novena permite hallar ciertos parámetros estadísticos de los precios en los 3 tipos de tiendas
● La décima fue para calcular el precio que tendría una canasta normada si se comprara en una mipyme o en una tienda en USD
● La oncena permite analizar si los establecimientos respetan los precios máximos que dicta la ley
● La duodécima fue para ver si existía alguna relación entre tener redes sociales (Instagram y Facebook) para promocionar una mipyme y los precios de los productos
