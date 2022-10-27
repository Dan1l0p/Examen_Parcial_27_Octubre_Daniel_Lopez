""Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5], regla de Sarrus de forma recursiva y de forma iterativa""

def determinante(matriz):
    return (matriz[0][0]*matriz[1][1]*matriz[2][2]*matriz[3][3]*matriz[4][4]*matriz[5][5])+(matriz[1][0]*matriz[0][0]*matriz[0][0]*matriz[0][0]*matriz[0][0])+(matriz[0][0]*matriz[0][0])