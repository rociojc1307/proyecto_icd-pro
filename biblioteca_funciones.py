import json

def cargar_datos_desde_json(path_precios_tiendas = "C:\\Ciencia de Datos\\1er Semestre\\INTRODUCCION A LA CIENCIA DE DATOS\\icd\\THE ULTIMATE PROJECT\\MIPYMES\\mipymes_tusd_tmlc.json", path_tasas_cambio_usd_mlc = "C:\\Ciencia de Datos\\1er Semestre\\INTRODUCCION A LA CIENCIA DE DATOS\\icd\\THE ULTIMATE PROJECT\\MIPYMES\\toque.json", path_precios_max_min = "C:\\Ciencia de Datos\\1er Semestre\\INTRODUCCION A LA CIENCIA DE DATOS\\icd\\THE ULTIMATE PROJECT\\MIPYMES\\precios_max_min.json", path_precios_canasta = "C:\\Ciencia de Datos\\1er Semestre\\INTRODUCCION A LA CIENCIA DE DATOS\\icd\\THE ULTIMATE PROJECT\\MIPYMES\\precios_canasta.json", path_precios_arroz = "C:\\Ciencia de Datos\\1er Semestre\\INTRODUCCION A LA CIENCIA DE DATOS\\icd\\THE ULTIMATE PROJECT\\MIPYMES\\json\\seguimiento_arroz.json",
                            path_datos_extras = "C:\\Ciencia de Datos\\1er Semestre\\INTRODUCCION A LA CIENCIA DE DATOS\\icd\\THE ULTIMATE PROJECT\\MIPYMES\\datos_extras.json"):
    with open(path_precios_tiendas, 'r', encoding='utf-8') as f_precios_tiendas:
        datos_precios_tiendas = json.load(f_precios_tiendas)
    with open(path_tasas_cambio_usd_mlc, 'r', encoding='utf-8') as f_tasas_cambio_usd_mlc:
        datos_tasas_cambio_usd_mlc = json.load(f_tasas_cambio_usd_mlc)
    with open(path_precios_max_min, 'r', encoding='utf-8') as f_precios_max_min:
        precios_max_min = json.load(f_precios_max_min)
    with open(path_precios_canasta, 'r', encoding='utf-8') as f_precios_canasta:
        precios_canasta = json.load(f_precios_canasta)
    with open(path_precios_arroz, 'r', encoding='utf-8') as f_precios_arroz:
        precios_arroz = json.load(f_precios_arroz)
    with open(path_datos_extras, 'r', encoding='utf-8') as f_datos_extras:
        datos_extras = json.load(f_datos_extras)    
    return datos_precios_tiendas, datos_tasas_cambio_usd_mlc, precios_max_min, precios_canasta, precios_arroz, datos_extras

def promedio(Lista : list):
    if not Lista: 
        return 0
    suma = 0
    for i in Lista:
        # Incluí el “try – except” para evitar problemas que se presentaron al procesar algunos de los json
        try:
            i = int(i)
            suma += i
        except ValueError:
            continue
    return round(suma/len(Lista) ,2)

def minimo(lista_precios):
    if not lista_precios: 
        return 0
    return min(lista_precios)

def maximo(lista_precios):
    if not lista_precios: 
        return 0
    return max(lista_precios)

def moda(lista_precios):
    if not lista_precios: 
        return " "
    frecuencias = {}
    for precio in lista_precios:
        # Para extraer el primer valor
        if isinstance(precio, list):
            if len(precio) > 0:
                precio = precio[0]
            else:
                continue # Salta si la lista interna está vacía
        try:
            # Convierto a float y redondeamos a dos cifras después de la coma
            costo = round(float(precio), 2)
            frecuencias[costo] = frecuencias.get(costo, 0) + 1
        except (ValueError, TypeError):
            # Si el dato no es un número (ej. un texto vacío), lo ignoramos
            continue
    if not frecuencias:
        return " "
    # Buscamos el que más se repite
    max_frecuencia = 0
    moda = None
    for precio, cuenta in frecuencias.items():
        if cuenta > max_frecuencia:
            max_frecuencia = cuenta
            moda = precio  
    return moda

def calcular_tasa_promedio(datos_tasas_cambio_usd_mlc):
    #Busco calcular el precio promedio al que han sido valorados el USD y el MLC en el mercado informal.
    tasas_usd = []
    tasas_mlc = []
    # El USD está en la primera posición de la lista "El toque"
    datos_usd = datos_tasas_cambio_usd_mlc["El toque"][0]["Cambio informal del USD en CUP"]
    for registro in datos_usd:
        tasas_usd.append(registro["precio"])
    # El MLC está en la segunda posición de la lista "El toque"
    datos_mlc = datos_tasas_cambio_usd_mlc["El toque"][1]["Cambio informal del MLC en CUP"]
    for registro in datos_mlc:
        tasas_mlc.append(registro["precio"])
    return round(promedio(tasas_usd) ,2), promedio(tasas_mlc)

def convertir_precios_cup_usd_mlc(datos_precios_tiendas, promedio_usd, promedio_mlc):
    analisis = []
    analisis_usd = []
    analisis_mlc = []
    for mipyme in datos_precios_tiendas.get("Mipymes"):
        analisis_mipyme = {
            "nombre": mipyme.get("nombre"),
            "precios_cup": {},
            "precios_usd": {},
            "precios_mlc": {}
        }
        for producto in mipyme.get("productos"):
            nombre = producto.get("nombre")
            categoria = producto.get("categoria")
            presentacion = producto.get("presentacion")
            cantidad = producto.get("cantidad")
            unidad_medida = producto.get("unidad_medida")
            precio_ = producto.get("precio")
            if nombre and categoria and precio_ is not None:
                try:
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
                    if categoria in ["Sal", "Lácteos", "Detergente", "Cereales"] and presentacion != "1 kg":
                        if unidad_medida == "g":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "kg":
                            precio = precio / (cantidad / 1)
                        if unidad_medida == "lb":
                            precio = precio / (cantidad * 0.454)
                        if unidad_medida == "mL":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "L":
                            precio = precio / (cantidad / 1)   
                    if categoria == "Pastas" and presentacion != "500 g":
                        if unidad_medida == "g":
                            precio = ((500 / cantidad) * precio)
                    if categoria == "Café" and presentacion != "4 oz":
                        if unidad_medida == "g":
                            precio = ((precio / cantidad) * 4 * 28.3495)
                    if categoria in  ["Bebidas"] and presentacion != "1 L":
                        if unidad_medida == "mL":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "L":
                            precio = precio / (cantidad / 1)   
                    if nombre == "Compota" and presentacion != "200 mL":
                        if unidad_medida == "g":
                            precio = ((precio / cantidad) * 200)
                    if categoria in ["Jabón"] and presentacion != "115 g":
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
                    if (nombre == "Culeros de niños" or nombre == "Culeros de adultos") and cantidad != 30:
                        precio = ((30 / cantidad) * precio)
                    analisis_mipyme["precios_cup"][nombre] = precio
                    analisis_mipyme["precios_usd"][nombre] = round(precio / promedio_usd ,2)
                    analisis_mipyme["precios_mlc"][nombre] = round(precio / promedio_mlc ,2)
                except ValueError:
                    #Me estaba dando un error de este tipo, pero no pude encontrar el problema en el json, así logré solucionarlo
                    continue
        analisis.append(analisis_mipyme)
    for tienda_usd in datos_precios_tiendas.get("Tiendas_en_USD"):
        analisis_tienda_usd = {
            "nombre": tienda_usd.get("nombre"),
            "precios_cup": {},
            "precios_usd": {},
            "precios_mlc": {}
        }
        for producto in tienda_usd.get("productos"):
            nombre = producto.get("nombre")
            categoria = producto.get("categoria")
            presentacion = producto.get("presentacion")
            cantidad = producto.get("cantidad")
            unidad_medida = producto.get("unidad_medida")
            precio_ = producto.get("precio")
            if nombre and categoria and precio_ is not None:
                try:
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
                    if categoria in ["Sal", "Lácteos", "Detergente", "Cereales"] and presentacion != "1 kg":
                        if unidad_medida == "g":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "kg":
                            precio = precio / (cantidad / 1)
                        if unidad_medida == "lb":
                            precio = precio / (cantidad * 0.454)
                        if unidad_medida == "mL":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "L":
                            precio = precio / (cantidad / 1)   
                    if categoria == "Pastas" and presentacion != "500 g":
                        if unidad_medida == "g":
                            precio = ((500 / cantidad) * precio)
                    if categoria == "Café" and presentacion != "4 oz":
                        if unidad_medida == "g":
                            precio = ((precio / cantidad) * 4 * 28.3495)
                    if categoria in  ["Bebidas"] and presentacion != "1 L":
                        if unidad_medida == "mL":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "L":
                            precio = precio / (cantidad / 1)   
                    if nombre == "Compota" and presentacion != "200 mL":
                        if unidad_medida == "g":
                            precio = ((precio / cantidad) * 200)
                    if categoria in ["Jabón"] and presentacion != "115 g":
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
                    if (nombre == "Culeros de niños" or nombre == "Culeros de adultos") and cantidad != 30:
                        precio = ((30 / cantidad) * precio)
                    analisis_tienda_usd["precios_cup"][nombre] = round(precio * promedio_usd ,2)
                    analisis_tienda_usd["precios_usd"][nombre] = round(precio ,2)
                    analisis_tienda_usd["precios_mlc"][nombre] = round(precio * promedio_usd / promedio_mlc ,2)
                except ValueError:
                    #Me estaba dando un error de este tipo, pero no pude encontrar el problema en el json, así logré solucionarlo
                    continue
        analisis_usd.append(analisis_tienda_usd)
    for tienda_mlc in datos_precios_tiendas.get("Tienda_en_MLC"):
        analisis_tienda_mlc = {
            "nombre": tienda_mlc.get("nombre"),
            "precios_cup": {},
            "precios_usd": {},
            "precios_mlc": {}
        }
        for producto in tienda_mlc.get("productos"):
            nombre = producto.get("nombre")
            categoria = producto.get("categoria")
            presentacion = producto.get("presentacion")
            cantidad = producto.get("cantidad")
            unidad_medida = producto.get("unidad_medida")
            precio_ = producto.get("precio")
            if nombre and categoria and precio_ is not None:
                try:
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
                    if categoria in ["Sal", "Lácteos", "Detergente", "Cereales"] and presentacion != "1 kg":
                        if unidad_medida == "g":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "kg":
                            precio = precio / (cantidad / 1)
                        if unidad_medida == "lb":
                            precio = precio / (cantidad * 0.454)
                        if unidad_medida == "mL":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "L":
                            precio = precio / (cantidad / 1)   
                    if categoria == "Pastas" and presentacion != "500 g":
                        if unidad_medida == "g":
                            precio = ((500 / cantidad) * precio)
                    if categoria == "Café" and presentacion != "4 oz":
                        if unidad_medida == "g":
                            precio = ((precio / cantidad) * 4 * 28.3495)
                    if categoria in  ["Bebidas"] and presentacion != "1 L":
                        if unidad_medida == "mL":
                            precio = ((1000 / cantidad) * precio)
                        if unidad_medida == "L":
                            precio = precio / (cantidad / 1)   
                    if nombre == "Compota" and presentacion != "200 mL":
                        if unidad_medida == "g":
                            precio = ((precio / cantidad) * 200)
                    if categoria in ["Jabón"] and presentacion != "115 g":
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
                    if (nombre == "Culeros de niños" or nombre == "Culeros de adultos") and cantidad != 30:
                        precio = ((30 / cantidad) * precio)
                    analisis_tienda_mlc["precios_cup"][nombre] = round(precio * promedio_mlc ,2)
                    analisis_tienda_mlc["precios_usd"][nombre] = round(precio * promedio_mlc / promedio_usd ,2)
                    analisis_tienda_mlc["precios_mlc"][nombre] = round(precio ,2)
                except ValueError:
                    #Me estaba dando un error de este tipo, pero no pude encontrar el problema en el json, así logré solucionarlo
                    continue
        analisis_mlc.append(analisis_tienda_mlc)
    return analisis, analisis_usd, analisis_mlc

def trabajo_datos_tiendas(datos_mipymes, datos_usd, datos_mlc):
    def procesamiento(lista_tiendas):
        # Creé 20 listas vacías (una para producto)
        lista = []
        for i in range(20):
            lista.append([])
        for tienda in lista_tiendas:
            # Utilizando los precios en CUP
            prod = tienda.get("precios_cup", {})
            # 0. Arroz
            if "Arroz" in prod: 
                lista[0].append(prod["Arroz"])
            # 1. Frijoles
            if "Frijoles negros" in prod: 
                lista[1].append(prod["Frijoles negros"])
            if "Frijoles colorados" in prod: 
                lista[1].append(prod["Frijoles colorados"])
            if "Garbanzos" in prod: 
                lista[1].append(prod["Garbanzos"])
            if "Lentejas" in prod: 
                lista[1].append(prod["Lentejas"])
            # 2. Lácteos
            if "Leche en polvo" in prod: 
                lista[2].append(prod["Leche en polvo"])
            if "Leche fluida" in prod: 
                lista[2].append(prod["Leche fluida"])   
            # 3. Cárnicos
            if "Paquete de pollo" in prod: 
                lista[3].append(prod["Paquete de pollo"])
            if "Pollo entero" in prod: 
                lista[3].append(prod["Pollo entero"])
            if "Paquete de pechuga de pollo" in prod: 
                lista[3].append(prod["Paquete de pechuga de pollo"])
            if "Molleja de pollo" in prod: 
                lista[3].append(prod["Molleja de pollo"])
            if "Hígado de pollo" in prod: 
                lista[3].append(prod["Hígado de pollo"])
            if "Alitas de pollo" in prod: 
                lista[3].append(prod["Alitas de pollo"]) 
            # 4. Pastas
            if "Espaguetis" in prod: 
                lista[4].append(prod["Espaguetis"])
            if "Coditos" in prod: 
                lista[4].append(prod["Coditos"])
            # 5. Aceite
            if "Aceite de girasol" in prod: 
                lista[5].append(prod["Aceite de girasol"])
            if "Aceite de soya" in prod: 
                lista[5].append(prod["Aceite de soya"])
            if "Aceite de oliva" in prod: 
                lista[5].append(prod["Aceite de oliva"])
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
            if "Detergente líquido" in prod: 
                lista[15].append(prod["Detergente líquido"])
            # 16. Jabón
            if "Jabón de tocador" in prod: 
                lista[16].append(prod["Jabón de tocador"])
            if "Jabón de lavar" in prod: 
                lista[16].append(prod["Jabón de lavar"])
            # 17. Pasta dental
            if "Pasta de dientes" in prod: 
                lista[17].append(prod["Pasta de dientes"])
            # 18. Culeros de niños
            if "Culeros de niños" in prod: 
                lista[18].append(prod["Culeros de niños"])
            # 19. Culeros de adultos
            if "Culeros de adultos" in prod: 
                lista[19].append(prod["Culeros de adultos"])
        return lista
    # Obtenemos los productos con sus precios para los 3 tipos de tiendas
    mipymes_final, usd_final, mlc_final = (
        procesamiento(datos_mipymes),
        procesamiento(datos_usd),
        procesamiento(datos_mlc)
    )

    return mipymes_final, usd_final, mlc_final

def trabajo_estadistico(mipymes_final, usd_final, mlc_final):
    nombres = ["Arroz", "Frijoles", "Leche", "Pollo", "Pastas", "Aceite", "Avena", "Azúcar", "Café", "Huevos", "Gelatina", "Sal", "Jugo", "Compota", "Maicena", "Detergente", "Jabón", "Pasta Dental", "Culeros Niños", "Culeros Adultos"]
    resultados = {
        "mipymes": {},
        "tiendas_usd": {},
        "tiendas_mlc": {}
    }
    # Asociamos cada elemento de "resultados" con el parámetro correspondiente
    fuentes = [
        ("mipymes", mipymes_final),
        ("tiendas_usd", usd_final),
        ("tiendas_mlc", mlc_final)
    ]
    for elemento, parametro in fuentes:
        for i in range(len(nombres)):
            producto = nombres[i]         
            if i < len(parametro):
                lista = parametro[i]
            else:
                lista = []
            # Si la lista tiene elementos calcularemos:
            if lista:
                resultados[elemento][producto] = {
                    "promedio": promedio(lista),
                    "minimo": minimo(lista),
                    "maximo": maximo(lista),
                    "moda": moda(lista)
                }
    return resultados

def suma_productos_cb(resultados):
    # Lista de productos que queremos incluir
    filtro = ["Arroz", "Frijoles", "Pollo", "Aceite", "Azúcar", "Café", "Sal", "Detergente", "Jabón", "Pasta Dental"]
    resultado = {"mipymes": 0, "tiendas_usd": 0}
    for categoria in resultado.keys():
        if categoria in resultados:
            for producto in resultados[categoria]:
                if producto in filtro:
                    resultado[categoria] += resultados[categoria][producto]["moda"]
                    round(resultado[categoria] ,2)
    return resultado

def obtener_precios_individuales_cb(resultados):
    filtro = ["Arroz", "Frijoles", "Pollo", "Aceite", "Azúcar", "Café", "Sal", "Detergente", "Jabón", "Pasta Dental"]
    precios_individuales = {}
    if "mipymes" in resultados:
        for producto in resultados["mipymes"]:
            if producto in filtro:
                precios_individuales[producto] = round(resultados["mipymes"][producto]["moda"], 2)
    return precios_individuales

def comparar_precios(precios_max_min, precios):
    precios_tope = {}
    for p in precios_max_min['productos']:
        nombre = p['variedad']
        tope = p['precio_max']
        precios_tope[nombre] = tope
    conversion = {
        'Arroz': 'Arroz', 'Frijoles': 'Frijoles', 'Aceite': 'Aceite a granel', 'Café': 'Café molido', 'Huevos': 'Huevos', 'Leche': 'Leche en polvo'
    }
    resultados = {}
    for producto_mipyme, producto_topado in conversion.items():
        if producto_mipyme in precios['mipymes']:
            estadisticas = precios['mipymes'][producto_mipyme]
            precio_tope = precios_tope.get(producto_topado)
            precio_mipyme = estadisticas['moda'] # Usar promedio es más exacto para economía que la moda

            if precio_tope is not None:
                if precio_mipyme <= precio_tope:
                    texto = "Se respeta el tope de precio"
                else:
                    texto = "No se respeta el tope de precio"
                
                texto += f" ({precio_mipyme} vs {precio_tope})"
                resultados[producto_mipyme] = {texto}
                
    return resultados

def analizar_precios_mip_por_redes_sociales(datos_precios_tiendas):
    precios_mip_redes_soc = []
    precios_mip_sin_redes_soc = []
    mipymes = datos_precios_tiendas.get("Mipymes")
    for mip in mipymes:
        ig = mip['redes_sociales']['instagram']['seguidores'] or 0
        fb = mip['redes_sociales']['facebook']['seguidores'] or 0
        total_seguidores = ig + fb
        precio_arroz = 0
        for producto in mip['productos']:
            if producto['nombre'] == "Arroz":
                precio_arroz = producto['precio']
                break       
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