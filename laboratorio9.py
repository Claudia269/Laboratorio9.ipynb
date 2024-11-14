# -*- coding: utf-8 -*-
"""Laboratorio9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1veFhKD_MZ8nyhYRM8wSrDQ-o25qI6WAL
"""

import pandas as pd
import cryptography.fernet as Fernet

datos = { 'Nombre':['juan', 'ana', 'pedro', 'maria', 'luis', 'ana' ],
          'edad':[28, 34, None, 45, 38, 34 ],
          'salario':[3000, 4000, None, 4500, 4000, 5000 ],
          'fecha_ingreso':['2021-01-15', '2020/03/12', 	'2022-07-01', '2021/12/01', '2021-05-20', '2020-03-12']
}

# Creación del datafram
df = pd.DataFrame(datos)

#Identificamos tipo de dato del dataframe
df.dtypes

#Muestra los cinco primeros datos
df.head()

# Punto 1: Identificar y contar los valores faltantes en cada columna
missing_values_datos = df.isnull().sum()
missing_values_datos

# Paso 2: Convertir 'Edad' a numérico, reemplazando valores no numéricos con NaN
df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
print("\nEdades después de la conversión:")
print(df['edad'])

# Paso 2: Convertir 'salario' a numérico, reemplazando valores no numéricos con NaN
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')
print("\nSalario empleados después de la conversión:")
print(df['salario'])

# Punto 3 visualiamos lo que contiene la columna fecha_ingreso
df['fecha_ingreso']

#Estandarizamos lo que contiene la columna fecha_ingreso
df['fecha_ingreso'] = pd.to_datetime(df['fecha_ingreso'], errors='coerce').dt.strftime('%Y-%m-%d')
df['fecha_ingreso']

# Punto 2 Parte 1

datos2 = { 'Nombre':['juan', 'ana', 'pedro', 'maria', 'luis', 'carla' ],
          'edad':[28, None, 40, 45, 38, 34 ],
          'salario':[3000, 4000, 4500, 'cuatro mil', 5000, 4000 ],
          'cargo':['Analista', 'Gerente',	'Desarrollador', 'Gerente', 'Analista', None],
          'fecha_ingreso':['2021-01-15', '2020/03/12', 	'2022-07-01', '2021/12/01', None, '2020-03-12']
}

# Creación del datafram
df2 = pd.DataFrame(datos2)

#Identificamos tipo de dato del dataframe
df2.dtypes

#Muestra los cinco primeros datos
df.head()

# Punto 1: Identificar y contar los valores faltantes en cada columna
missing_values_datos = df2.isnull().sum()
missing_values_datos

# Paso 2: Convertir 'Edad' a numérico, reemplazando valores no numéricos con NaN
df2['edad'] = pd.to_numeric(df2['edad'], errors='coerce')
print("\nEdades después de la conversión:")
print(df2['edad'])

# Paso 2: Convertir 'salario' a numérico, reemplazando valores no numéricos con NaN
df2['salario'] = pd.to_numeric(df2['salario'], errors='coerce')
print("\nSalario empleados después de la conversión:")
print(df2['salario'])

#Estandarizamos lo que contiene la columna fecha_ingreso
df2['fecha_ingreso'] = pd.to_datetime(df2['fecha_ingreso'], errors='coerce').dt.strftime('%Y-%m-%d')
df2['fecha_ingreso']

#Verificar que no haya valores faltantes en la columna "Cargo".
cargo_faltantes = df2[df2['cargo'].isna()]
print(cargo_faltantes)

"""**PARTE 2 LABORATORIO 9**"""

productos = { 'producto':['Producto A', 'Producto B', 'Producto c', 'Producto D'],
          'precio':[150, -25, 100,None],
          }

# Creación del datafram
df3 = pd.DataFrame(productos)

#Identificamos tipo de dato del dataframe
df3.dtypes

# Imprimimos los datos del dataframe
df3

# Validamos números negativos  y faltantes
df3['Datosinvalidos']= df3['precio'].apply(lambda x: 'Valido' if pd.notnull (x) and x>=0 else 'Invalido')
print(df3)

# Creamos dataframe con los datos del cliente
clientes={ 'Nombre':['Ana', 'Luis', 'Maria', 'Luis', 'Carlos'],
             'IDCliente':[1, 2, 3, 2, 4],
          }

# Verificar si hay duplicados en la columna de IDCliente
df4 = pd.DataFrame(clientes)
duplicados = df4[df4.duplicated('IDCliente')]
print(duplicados)

# Encriptar y desencriptar número tarjeta de crédito
key = Fernet.Fernet.generate_key()
cipher_suite = Fernet.Fernet(key)
datos_sensibles = '1234-5678-91011121'.encode()
dato_encriptado=cipher_suite.encrypt(datos_sensibles)
print('DATOS CIFRADOS:', dato_encriptado)

dato_desencriptado = cipher_suite.decrypt(dato_encriptado)
print('DATOS DESCIFRADOS:', dato_desencriptado.decode())