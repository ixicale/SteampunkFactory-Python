import pandas as pd

# Completar un diccionario de datos con diferentes tipos de valor 
df = pd.DataFrame({'foo': [1, 2, 3, 4],
    'bar': ['a', 'b', 'c', 'd'],
    'baz': pd.date_range('2018-01-01', freq='d', periods=4),
    'qux': pd.Categorical(['a', 'b', 'c', 'c'])
    }, index=pd.Index(range(4), name='idx'))

# Impresiones de arreglo 
print df
print df.dtypes

# Escribir JSON 'test.json' con la tabla df
df.to_json('test.json', orient='table')
# Leer el JSON 'test.json' para almacenar en la variable
new_df = pd.read_json('test.json', orient='table')
print new_df

#Imprimir sus tipo de dato
print new_df.dtypes

#
df.index.name = 'Index'

# Escribir JSON 'test.json' con la tabla df
df.to_json('test.json', orient='table')
# Leer el JSON 'test.json' para almacenar en la variable
new_df = pd.read_json('test.json', orient='table')
print new_df



