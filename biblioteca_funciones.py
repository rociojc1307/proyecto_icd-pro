import json

def cargar_datos_desde_json(path = ''):
    with open(path, 'r', encoding='utf-8') as f:
        datos = json.load(f)  
    return datos

def promedio(Lista : list):
    if not Lista: 
        return 0
    for i in Lista:
        i = float(i)
    return round(sum(Lista)/len(Lista) ,2)

def moda(Lista : list):
    if not Lista: 
        return ""
    frecuencias = {}
    for precio in Lista:
        costo = round(float(precio), 2)
        frecuencias[costo] = frecuencias.get(costo, 0) + 1
    if not frecuencias:
        return ""
    # Buscamos el que más se repite
    max_frecuencia = 0
    moda = None
    for precio, cuenta in frecuencias.items():
        if cuenta > max_frecuencia:
            max_frecuencia = cuenta 
            moda = precio
    return moda

def calcular_tasa_promedio(datos_tasas_cambio_usd_mlc, moneda = "USD/ MLC"):
    #Busco calcular el precio promedio al que han sido valorados el USD y el MLC en el mercado informal.
    tasas = []
    # El USD está en la primera posición de la lista "El toque" y el MLC en la segunda
    if moneda == "USD":
        datos = datos_tasas_cambio_usd_mlc["El toque"][0]["Cambio informal del USD en CUP"]
    else:
        datos = datos_tasas_cambio_usd_mlc["El toque"][1]["Cambio informal del MLC en CUP"]
    for registro in datos:
        tasas.append(registro["precio"])
    return promedio(tasas)

def toque(datos_tasas_cambio_usd_mlc, fecha_inicial, fecha_final, moneda = 'USD/MLC'):
    fechas = []
    precios = []
    i=0
    if moneda == "USD":
        datos = datos_tasas_cambio_usd_mlc["El toque"][0]["Cambio informal del USD en CUP"]
    else:
        datos = datos_tasas_cambio_usd_mlc["El toque"][1]["Cambio informal del MLC en CUP"]
    while i < len(datos):
        if datos[i]['fecha']!= fecha_inicial:
            i+=1
            continue
        else:
            fechas.append(datos[i]['fecha'])
            precios.append(datos[i]["precio"])
            j = i+1
            while j <= (len(datos)-1):
                if datos[j]['fecha'] == fecha_final:
                    fechas.append(datos[j]['fecha'])
                    precios.append(datos[j]["precio"])
                    break
                else:
                    fechas.append(datos[j]['fecha'] )
                    precios.append(datos[j]["precio"])
                j+=1
        break
    return fechas, precios

def conversor(producto):
    nombre = producto.get("nombre")
    categoria = producto.get("categoria")
    presentacion = producto.get("presentacion")
    cantidad = producto.get("cantidad")
    unidad_medida = producto.get("unidad_medida")
    precio_ = producto.get("precio")
    if nombre and categoria and precio_ is not None:
        precio = float(precio_)
        if categoria in ["Granos", "Aceite", "Azúcar", "Cárnicos"] and presentacion != "1 lb":
            if unidad_medida == "g":
                precio = precio / ((cantidad / 1000) / 0.454)
            if unidad_medida == "kg":
                precio = precio / (cantidad / 0.454)
            if unidad_medida == "lb":
                precio = precio / cantidad
            if unidad_medida == "mL":
                precio = ((precio * 515.4) / cantidad)
            if unidad_medida == "L":
                precio = ((precio * 515.4) / (cantidad * 1000))
        if categoria in ["Condimentos", "Lácteos", "Detergente", "Cereales"] and presentacion != "1 kg":
            if unidad_medida == "g":
                precio = ((1000 / cantidad) * precio)
            if unidad_medida == "kg":
                precio = precio / cantidad
            if unidad_medida == "lb":
                precio = precio / (cantidad * 0.454)
            if unidad_medida == "mL":
                precio = ((1000 / cantidad) * precio)
            if unidad_medida == "L":
                precio = precio / cantidad   
        if categoria == "Pastas" and presentacion != "500 g":
            if unidad_medida == "g":
                precio = ((500 / cantidad) * precio)
        if categoria == "Café" and presentacion != "4 oz":
            if unidad_medida == "g":
                precio = ((precio / cantidad) * 4 * 28.3495)
        if categoria == "Bebidas" and presentacion != "1 L":
            if unidad_medida == "mL":
                precio = ((1000 / cantidad) * precio)
            if unidad_medida == "L":
                precio = precio / cantidad   
        if nombre == "Compota" and presentacion != "200 mL":
            if unidad_medida == "g":
                precio = ((precio / cantidad) * 200)
        if categoria == "Jabón" and presentacion != "115 g":
            if unidad_medida == "g":
                precio = ((115 / cantidad) * precio)
        if categoria in ["Pasta dental"] and presentacion != "85 mL":
            if unidad_medida == "g":
                precio = ((85 / cantidad) * precio)
            if unidad_medida == "mL":
                precio = ((85 / cantidad) * precio)
        if nombre == "Gelatina" and presentacion != "100 g":
            if unidad_medida == "g":
                precio = ((100 / cantidad) * precio)  
    return round(precio, 2)

def convertir_precios_cup_usd_mlc(datos_precios_tiendas, promedio_usd, promedio_mlc, establecimiento = 'Mipymes/ Tiendas_en_USD/ Tienda_en_MLC', monedas = 'CUP/ USD/ MLC'):
    analisis = []
    for tienda in datos_precios_tiendas.get(establecimiento):
        analisis_tienda = {
            "nombre": tienda.get("nombre"),
            "moneda": tienda.get("moneda"),
            "precios_cup": {},
            "precios_usd": {},
            "precios_mlc": {}
        }
        for producto in tienda.get("productos"):
            nombre = producto.get("nombre")
            precio = conversor(producto)
            if analisis_tienda["moneda"] == "CUP":
                if monedas == 'CUP':
                    analisis_tienda["precios_cup"][nombre] = precio
                if monedas == 'USD':
                    analisis_tienda["precios_usd"][nombre] = round(precio / promedio_usd ,2)
                if monedas == 'MLC':
                    analisis_tienda["precios_mlc"][nombre] = round(precio / promedio_mlc ,2)  
            if analisis_tienda["moneda"] == "USD":
                if monedas == 'CUP':
                    analisis_tienda["precios_cup"][nombre] = round(precio * promedio_usd ,2)
                if monedas == 'USD':
                    analisis_tienda["precios_usd"][nombre] = round(precio ,2)
                if monedas == 'MLC':
                    analisis_tienda["precios_mlc"][nombre] = round(precio * promedio_usd / promedio_mlc ,2)
            if analisis_tienda["moneda"] == "MLC":
                if monedas == 'CUP':
                    analisis_tienda["precios_cup"][nombre] = round(precio * promedio_mlc ,2)
                if monedas == 'USD':
                    analisis_tienda["precios_usd"][nombre] = round(precio * promedio_mlc / promedio_usd ,2)
                if monedas == 'MLC':
                    analisis_tienda["precios_mlc"][nombre] = round(precio ,2)
        analisis.append(analisis_tienda)
    return analisis

def trabajo_datos_tiendas(datos):
    def procesamiento(tiendas):
        # Creé 19 listas vacías (una para producto)
        lista = []
        for i in range(19):
            lista.append([])
        for tienda in tiendas:
        # Utilizando los precios en CUP
            prod = tienda.get("precios_cup", {})
            # 0. Arroz
            if "Arroz" in prod: 
                lista[0].append(prod["Arroz"])
                # 1. Frijoles
            if "Frijoles negros" in prod: 
                lista[1].append(prod["Frijoles negros"])
            # 2. Lácteos
            if "Leche en polvo" in prod: 
                lista[2].append(prod["Leche en polvo"])   
            # 3. Cárnicos
            if "Paquete de pollo" in prod: 
                lista[3].append(prod["Paquete de pollo"])
            # 4. Pastas
            if "Espaguetis" in prod: 
                lista[4].append(prod["Espaguetis"])
            elif "Coditos" in prod: 
                lista[4].append(prod["Coditos"])
            # 5. Aceite
            if "Aceite de soya" in prod: 
                lista[5].append(prod["Aceite de soya"])
            # 6. Avena
            if "Avena" in prod: 
                lista[6].append(prod["Avena"])
            # 7. Azúcar
            if "Azúcar" in prod: 
                lista[7].append(prod["Azúcar"])
            # 8. Café
            if "Café molido" in prod: 
                lista[8].append(prod["Café molido"])
            # 9. Huevos
            if "Cartón de huevos" in prod: 
                lista[9].append(prod["Cartón de huevos"])
            # 10. Gelatina
            if "Gelatina" in prod: 
                lista[10].append(prod["Gelatina"])
            # 11. Sal 
            if "Sal" in prod: 
                lista[11].append(prod["Sal"])
            # 12. Jugo
            if "Jugo" in prod: 
                lista[12].append(prod["Jugo"])
            # 13. Compota
            if "Compota" in prod: 
                lista[13].append(prod["Compota"])
            # 14. Maicena
            if "Maicena" in prod: 
                lista[14].append(prod["Maicena"])
            # 15. Detergente
            if "Detergente en polvo" in prod: 
                lista[15].append(prod["Detergente en polvo"])
            # 16. Jabón
            if "Jabón de tocador" in prod: 
                lista[16].append(prod["Jabón de tocador"])
            # 17. Pasta dental
            if "Pasta de dientes" in prod: 
                lista[17].append(prod["Pasta de dientes"])
            # 18. Culeros de adultos
            if "Culeros de adultos" in prod: 
                lista[18].append(prod["Culeros de adultos"])
        return lista
    # Obtenemos los productos con sus precios para los 3 tipos de tiendas
    tienda = procesamiento(datos)
    return tienda

def trabajo_estadistico(datos):
    nombres = ["Arroz", "Frijoles", "Leche", "Pollo", "Pastas", "Aceite", "Avena", "Azúcar", "Café", "Huevos", "Gelatina", "Sal", "Jugo", "Compota", "Maicena", "Detergente", "Jabón", "Pasta Dental", "Culeros Adultos"]
    resultados = {}
    # Asociamos cada elemento de "resultados" con el parámetro correspondiente
    for i in range(len(nombres)):
        producto = nombres[i]         
        if i < len(datos):
            lista = datos[i]
        else:
            lista = []
        # Si la lista tiene elementos calcularemos:
        if lista:
            resultados[producto] = {
                "promedio": promedio(lista),
                "minimo": min(lista),
                "maximo": max(lista),
                "moda": moda(lista)
            }
    return resultados

def suma_productos_cb(datos):
    # Lista de productos que queremos incluir
    filtro = ["Arroz", "Frijoles", "Pollo", "Aceite", "Azúcar", "Café", "Sal", "Detergente", "Jabón", "Pasta Dental"]
    resultado = 0
    for producto in datos:
        if producto in filtro:
            resultado += datos[producto]["moda"]
    return resultado

def obtener_precios_individuales_cb(resultados):
    filtro = ["Arroz", "Frijoles", "Pollo", "Aceite", "Azúcar", "Café", "Sal", "Detergente", "Jabón", "Pasta Dental"]
    precios_individuales = {}
    for producto in resultados:
        if producto in filtro:
            precios_individuales[producto] = resultados[producto]["moda"]
    return precios_individuales

def analizar_precios_mip_por_redes_sociales(datos_precios_tiendas):
    precios_mip_redes_soc = []
    precios_mip_sin_redes_soc = []
    mipymes = datos_precios_tiendas.get("Mipymes")
    for mip in mipymes:
        ig = mip['redes_sociales']['instagram']['seguidores'] or 0
        fb = mip['redes_sociales']['facebook']['seguidores'] or 0
        total_seguidores = ig + fb
        for producto in mip['productos']:
            if producto['nombre'] == "Arroz":
                precio_arroz = producto['precio']   
        # Clasificamos la mipyme en dependencia de si tiene o no redes sociales
        if total_seguidores > 0:
            precios_mip_redes_soc.append(precio_arroz)
        else:
            precios_mip_sin_redes_soc.append(precio_arroz)
    # Calculamos el promedio del precio del arroz para cada tipo de mipyme
    promedio_con_redes = promedio(precios_mip_redes_soc)
    promedio_sin_redes = promedio(precios_mip_sin_redes_soc)
    if promedio_con_redes > promedio_sin_redes:
        return f"Aquellas mipymes con redes sociales tienen precios más altos. El costo promedio del arroz en aquellas con redes es {promedio_con_redes} CUP y en las que no tienen : {promedio_sin_redes} CUP."
    else:
        return f"Las redes sociales no implican precios más altos. El costo promedio del arroz en aquellas con redes es {promedio_con_redes} CUP y en las que no tienen : {promedio_sin_redes} CUP."
     
def comparar_precios(precios_max_min, analisis_mip):
    precios_tope = {}
    for p in precios_max_min['productos']:
        nombre = p['variedad']
        tope = p['precio_max']
        precios_tope[nombre] = tope
    conversion = {
        'Arroz': 'Arroz', 'Frijoles': 'Frijoles', 'Aceite': 'Aceite', 'Huevos': 'Huevos', 'Leche': 'Leche en polvo'
    }
    precios_mipyme = []
    topes = []
    for producto_mipyme, producto_topado in conversion.items():
        if producto_mipyme in analisis_mip:
            precio_mipyme = analisis_mip[producto_mipyme]['moda']
            precio_tope = precios_tope.get(producto_topado)
            precios_mipyme.append(precio_mipyme)
            topes.append(precio_tope)
    return precios_mipyme, topes