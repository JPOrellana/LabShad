def matrixMultiplier(matrixA, matrixB):

    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    rowsB = len(matrixB)
    colsB = len(matrixB[0])


    if colsA == rowsB:
 
        matrixC = [[0 for _ in range(colsB)] for _ in range(rowsA)]
 
        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                  
                    matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
        return matrixC
    else:
        return None


def vectorXmatrix(matrix, vector):
 
    rows = len(matrix)
    cols = len(matrix[0])
    size = len(vector)

  
    if cols == size:
      
        newVector = [0 for row in range(rows)]

        for i in range(rows):
            for j in range(cols):
                newVector[i] += matrix[i][j] * vector[j]
        return newVector
    else:
        return None

def barycentricCoords(A, B, C, P):

    areaPCB = (B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])
    
    areaACP = (C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])
    
    areaABC = (B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1])

    #areaPBC = abs((P[0]*B[1] + B[0]*C[1] + C[0]*P[1]) - 
    #             (P[1]*B[0] + B[1]*C[0] + C[1]*P[0]))


    #areaACP = abs((A[0]*C[1] + C[0]*P[1] + P[0]*A[1]) - 
    #              (A[1]*C[0] + C[1]*P[0] + P[1]*A[0]))

    #areaABC = abs((A[0]*B[1] + B[0]*C[1] + C[0]*A[1]) - 
    #              (A[1]*B[0] + B[1]*C[0] + C[1]*A[0]))

    try:
        u = areaPCB / areaABC
        v = areaACP / areaABC
        w = 1 - u - v 
        return u, v, w
    except:
        return -1,-1,-1











