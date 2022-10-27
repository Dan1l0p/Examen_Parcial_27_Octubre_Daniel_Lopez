

def determinante(matriz):
    return (((matriz[0][0]*matriz[1][1]*matriz[2][2]*matriz[3][3]*matriz[4][4])+(matriz[1][0]*matriz[2][1]*matriz[3][2]*matriz[4][3]*matriz[0][4])+(matriz[2][0]*matriz[3][1]*matriz[4][2]*matriz[0][3]*matriz[1][4])+(matriz[3][0]*matriz[4][1]*matriz[0][2]*matriz[1][3]*matriz[4][4])+(matriz[4][0]*matriz[0][1]*matriz[1][2]*matriz[2][3]*matriz[3][4])))-(((matriz[0][4]*matriz[1][3]*matriz[2][2]*matriz[3][1]*matriz[4][0])+(matriz[1][4]*matriz[2][3]*matriz[3][2]*matriz[4][1]*matriz[0][0])+(matriz[2][4]*matriz[3][3]*matriz[4][2]*matriz[0][1]*matriz[1][0])+(matriz[3][4]*matriz[4][3]*matriz[0][2]*matriz[1][1]*matriz[4][0])+(matriz[4][4]*matriz[0][3]*matriz[1][2]*matriz[2][1]*matriz[3][0])))


print("El det de la matriz 5x5 es: ",determinante([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20], [21,22,23,24,25]]))
