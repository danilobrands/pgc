import numpy as np


obj3D = open("objects\cube\_SimpleCubeSize04.obj", "r")

coordenadasVertices = []

for linha in obj3D:
    valores = linha.split()

    try:
        if valores[0] == 'v':
            #print(valores[1])
            #print(valores[2])
            #print(valores[3])
            temp = [valores[1], valores[2], valores[3]]
            print(temp)
            coordenadasVertices.extend(temp)
            print(coordenadasVertices)
    except:
        print('não é coordenada de ponto')
    #print('linha: ')
    #print(type(linha))
    #print(linha)
    #print('valor: ')
    #print(type(valores))
    #print(valores)

print('**************************************')
print(type(coordenadasVertices))
print(coordenadasVertices)

coordenadasVerticesMatriz = np.array(coordenadasVertices)
print(coordenadasVerticesMatriz)
print(coordenadasVerticesMatriz.shape)
coordenadasVerticesMatriz = coordenadasVerticesMatriz.reshape(8,3)
print(coordenadasVerticesMatriz.shape)
print(coordenadasVerticesMatriz)

#print(obj3D)



