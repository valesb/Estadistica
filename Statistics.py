#!/usr/bin/env python
# coding: utf-8

# In[1]:


def media_aritmetica(valores):
    """
    Calcula la media aritmética de una lista de números.

    Parámetros
    ----------
    valores: lista
    » Lista con números.

    Retorna
    ---------
    media: float
    » La media aritmética de los números.
    
    Descripción
    ---------
    Esta función toma una lista de números, suma todos los valores y luego divide la sumatoria por la cantidad de valores en la lista.
    """
    return sum(valores) / len(valores)


# In[3]:


def median(valores):
    """
    Calcula la mediana de los datos en una lista de números.

    Parámetros
    ----------
    valores: lista
    » Lista con números.

    Retorna
    ---------
    median: float
    » Calcula la mediana de los datos.

    Descripción
    ---------
    Esta función toma una lista de números, la ordena y luego calcula la mediana de los datos.
    Si la lista tiene una cantidad impar de valores, devuelve el valor central.
    Si la lista tiene una cantidad par de valores, devuelve el promedio de los dos valores centrales.
    """
    lista_ordenada = sorted(valores)
    largo = len(valores)

    if largo % 2 == 1:
        median = lista_ordenada[largo // 2]
    else:
        valor_central1 = lista_ordenada[largo // 2 - 1]
        valor_central2 = lista_ordenada[largo // 2]
        median = (valor_central1 + valor_central2) / 2

    return median


# In[4]:


def mode(variables):
    """
    Calcula la moda de los datos en una lista de números.

    Parámetros
    ----------
    variables: lista
    » Lista con números de la cual se calculará la moda.

    Retorna
    ---------
    mode: lista
    » Una lista que contiene los valores que son considerados modas en los datos.

    Variables
    ----------
    categorias: lista
    » Una lista que almacena las categorías únicas presentes en la lista de valores.
    
    cuentas: lista
    » Una lista que almacena la frecuencia de cada categoría en la lista de valores.
    
    i_max: integer
    » Índice del valor máximo en la lista de frecuencias.
    
    val_max: integer
    » Valor máximo de frecuencia encontrado en la lista de frecuencias.
    
    Descripción
    ---------
    Esta función calcula la moda de una lista de valores. Comienza por encontrar las categorías únicas en la lista,
    luego cuenta la frecuencia de cada categoría y determina cuál(es) es/son la(s) moda(s).
    """
    categorias = []
    for v in variables:
        if v not in categorias:
            categorias.append(v)
    cuentas = []
    for c in categorias:
        n = 0  # Inicializa la cuenta en cero
        for val in variables:
            if val == c:
                n = n + 1
        cuentas.append(n)

    i_max = 0
    val_max = cuentas[0]
    for i in range(1, len(cuentas)):  # El rango debe comenzar en 1
        if cuentas[i] > val_max:
            i_max = i 
            val_max = cuentas[i]
    
    mode = [categorias[i] for i, cuenta in enumerate(cuentas) if cuenta == val_max]
    return mode


# In[6]:


def variance(valores):
    """
    Calcula la varianza de una lista de números.

    Parámetros
    ----------
    valores: lista
    » Lista con los valores de la cual se calculará la varianza.

    Retorna
    ---------
    variance: float
    » El valor de la varianza.

    Descripción
    ---------
    Esta función calcula la varianza de una lista de valores. Primero, calcula la media aritmética de los valores en la lista.
    Luego, calcula la suma de los cuadrados de las diferencias entre cada valor y la media. Finalmente, divide esta suma por 
    la cantidad de valores en la lista para obtener la varianza.
    """
    media = sum(valores) / len(valores)
    suma_de_cuadrados = sum((x - media) ** 2 for x in valores)
    variance = suma_de_cuadrados / len(valores)
    return variance


# In[7]:


from math import sqrt

def desviacion_estandar(valores):
    """
    Calcula la desviación estándar de una lista de números.

    Parámetros
    ----------
    valores: lista
    » Lista con los valores de la cual se calculará la desviación estándar.

    Retorna
    ---------
    STD: float
    » La raíz cuadrada de la varianza.

    Descripción
    ---------
    Esta función importa la raíz cuadrada de la biblioteca math y la aplica a la varianza calculada a partir de los valores.
    """
    varianza = variance(valores)
    STD = sqrt(varianza)
    return STD


# In[8]:


def calcular_rango(valores):
    """
    Calcula el rango de una lista de números.

    Parámetros
    ----------
    valores: lista
    » Lista con los valores de la cual se calculará el rango.

    Retorna
    ---------
    calcular_rango: float
    » El valor máximo menos el valor mínimo de la lista de valores.

    Descripción
    ---------
    Esta función calcula el rango de una lista de números restando el valor mínimo del valor máximo.
    """
    calcular_rango = max(valores) - min(valores)
    return calcular_rango


# In[9]:


def DMA(valores):
    """
    Calcula la Desviación Absoluta Media (DMA) de una lista de valores.

    Parámetros
    ----------
    valores: lista de números
    » Lista de números de la cual se calculará la DMA.

    Retorna
    ---------
    DMA: float
    » La Desviación Absoluta Media de los valores en la lista.

    Descripción
    ---------
    Esta función calcula la Desviación Absoluta Media (DMA) de una lista de valores.
    La DMA se define como la mediana de las diferencias absolutas entre cada valor y la mediana de la lista.
    """
    mediana_valor = median(valores)
    datos = []
    for num in valores:
        datos_dma = abs(num - mediana_valor)
        datos.append(datos_dma)
        
    lista = sorted(datos)
    longitud = len(datos)
    
    if longitud % 2 == 1:
        DMA = lista[longitud // 2]
    else:
        centro1 = lista[longitud // 2 - 1]
        centro2 = lista[longitud // 2]
        DMA = (centro1 + centro2) / 2
    
    return DMA


# In[11]:


def calcular_percentiles(valores):
    """
    Calcula el percentil 25 (Q1) y el percentil 75 (Q3) de una lista de valores.

    Parámetros
    ----------
    valores: list
    » Lista de números de la cual se calcularán los percentiles.

    Retorna
    ---------
    percentiles: tuple
    » Una tupla que contiene el percentil 25 (Q1) y el percentil 75 (Q3) de los valores en la lista.

    Descripción
    ---------
    Esta función calcula el percentil 25 (Q1) y el percentil 75 (Q3) de una lista de valores.
    Estos percentiles dividen los datos en cuatro partes iguales.
    """
    datos_ordenados = sorted(valores)
    longitud = len(datos_ordenados)
    
    if longitud % 4 == 0:
        Q1 = (datos_ordenados[longitud // 4 - 1] + datos_ordenados[longitud // 4]) / 2
        Q3 = (datos_ordenados[3 * longitud // 4 - 1] + datos_ordenados[3 * longitud // 4]) / 2
    else:
        Q1 = datos_ordenados[(longitud + 1) // 4 - 1]
        Q3 = datos_ordenados[3 * (longitud + 1) // 4 - 1]
    
    percentiles = (Q1, Q3)
    return percentiles


# In[13]:


def calcular_iqr(valores):
    """
    Calcula el Rango Intercuartil (IQR) de una lista de valores.

    Parámetros
    ----------
    valores: lista de números
    » Lista de números de la cual se calculará el IQR.

    Retorna
    ---------
    iqr: float
    » El Rango Intercuartil (IQR) de los valores en la lista.

    Descripción
    ---------
    Esta función calcula el Rango Intercuartil (IQR) de una lista de valores. El IQR se calcula
    restando el tercer cuartil (Q3) al primer cuartil (Q1). El IQR es útil para identificar la 
    dispersión de los datos y detectar valores atípicos.
    """
    datos_ordenados = sorted(valores)
    long = len(datos_ordenados)
    
    if long % 4 == 0:
        Q1 = (datos_ordenados[long // 4 - 1] + datos_ordenados[long // 4]) / 2.0
        Q3 = (datos_ordenados[3 * long // 4 - 1] + datos_ordenados[3 * long // 4]) / 2.0
    else:
        Q1 = datos_ordenados[(long + 1) // 4 - 1]
        Q3 = datos_ordenados[3 * (long + 1) // 4 - 1]
    
    iqr = Q3 - Q1
    return iqr


# In[14]:


def limites_galac(valores):
    """
    Calcula los límites y promedios de tamaños de galaxias en diferentes categorías.

    Parámetros
    ----------
    valores : list
    » Lista de tamaños de galaxias representados como números enteros.

    Retorna
    ---------
    resultado : dict
    » Un diccionario que contiene los límites superiores e inferiores y los promedios de tamaños para diferentes categorías de galaxias.

    Descripción
    ---------
    Esta función toma una lista de tamaños de galaxias y los agrupa en categorías (SBa, SBb, SBc, Irr)
    basadas en intervalos. Calcula los límites superior e inferior para cada categoría y también el promedio de tamaños en cada categoría.
    """
    multiplicador = 1.5
    intervalos = {'SBa': (100, 200), 'SBb': (201, 400), 'SBc': (401, 600), 'Irr': (601, 800)}
    categorias = {categoria: [] for categoria in intervalos}

    for valor in valores:
        for categoria, (inicio, fin) in intervalos.items():
            if inicio <= valor <= fin:
                categorias[categoria].append(valor)
                break

    promedios = {categoria: sum(tamanos) / len(tamanos) if tamanos else 0 for categoria, tamanos in categorias.items()}

    Qa1 = promedios['SBa']
    Qa3 = promedios['SBc']

    rango_cuartil = Qa3 - Qa1

    limite_inferior = Qa1 - multiplicador * rango_cuartil
    limite_superior = Qa3 + multiplicador * rango_cuartil

    return {
        'limite_superior': limite_superior,
        'limite_inferior': limite_inferior,
        'promedios': promedios
    }


# In[17]:


def encontrar_repeticiones(valores):
    """
    Encuentra y devuelve los valores de una lista que se repiten al menos 10 veces.

    Parámetros
    ----------
    valores: lista
    » Lista con números.

    Retorna
    ---------
    valores_repetidos: lista
    » Lista que contiene los valores que se repiten al menos 10 veces.

    Descripción
    ---------
    Esta función busca valores en la lista que se repiten al menos 10 veces y los almacena en una nueva lista.
    """
    valores_repetidos = []  # Lista para almacenar valores que se repiten

    for valor in valores:
        if valores.count(valor) >= 10 and valor not in valores_repetidos:
            valores_repetidos.append(valor)

    return valores_repetidos


# In[18]:


def agrupar_tamaños_galaxias(tamaños):
    """
    Agrupa tamaños de galaxias en diferentes categorías y calcula promedios.

    Parámetros
    ----------
    tamaños : lista
    » Lista de tamaños de galaxias representados como números enteros.

    Retorna
    ---------
    resultado : dict
    » Un diccionario que contiene los tamaños agrupados por categorías y sus promedios.

    Descripción
    ---------
    Esta función toma una lista de tamaños de galaxias y los agrupa en categorías (SBa, SBb, SBc, Irr) basadas en intervalos.
    Calcula el promedio de tamaños en cada categoría y devuelve un diccionario con los resultados.
    """
    intervalos = {
        "SBa": (16, 32),
        "SBb": (32, 64),
        "SBc": (64, 128),
        "Irr": (128, float("inf"))
    }

    resultado = {categoria: [] for categoria in intervalos}

    for tamaño in tamaños:
        try:
            tamaño_int = int(tamaño)
        except ValueError:
            continue  # Ignora datos que no son números enteros

        for categoria, (inicio, fin) in intervalos.items():
            if inicio <= tamaño_int < fin:
                resultado[categoria].append(tamaño_int)

    promedios = {categoria: sum(valores) / len(valores) if valores else 0 for categoria, valores in resultado.items()}

    print("Los promedios respectivos a cada categoría: ", promedios, "\n")
    return resultado


# In[ ]:




