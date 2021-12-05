'''evitar usar, pois é usado apenas para um tipo específico
    otimiza o processamento de maneira mais eficiente
    para processamento é melhor usar o numpy
    para uso comuns utilizar as listas e tuplas
'''
import array as arr
arr.array('d', [1, 3.5])

#preferencialmente usar quando precisa de calculo numerico - usado no data science
import numpy as np
numeros = np.array([1, 3.5])
print(numeros)
numeros + 3
print(numeros)

