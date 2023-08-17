import time
import math

def vertexShader(vertex, **kwargs):
    
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]

    vt =  vpMatrix * projectionMatrix * viewMatrix * modelMatrix @ vt

    vt = vt.tolist()[0]

    vt = [vt[0]/vt[3],
          vt[1]/vt[3],
          vt[2]/vt[3]]

    return vt


def stylizedEdgeDetectionShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)
    
    # Valor de umbral para detección de bordes
    edgeThreshold = 0.1
    
    # Calcula la intensidad del color
    intensity = (color[0] + color[1] + color[2]) / 3
    
    # Define los colores de los bordes y del interior
    edgeColor = (0.8, 0.2, 0.2)  # Color de los bordes
    fillColor = (0.1, 0.1, 0.1)  # Color del interior
    
    # Si la intensidad es mayor al umbral, aplica el color de borde
    if intensity > edgeThreshold:
        return edgeColor
    else:
        return fillColor




def pixelateFragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    pixelSize = kwargs.get("pixelSize", 20)  # Valor predeterminado si no se proporciona

    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calcula las coordenadas del píxel en la textura original
    origX = int(texCoords[0] * texture.width)
    origY = int(texCoords[1] * texture.height)

    # Calcula las coordenadas del píxel correspondiente en la textura pixelada
    pixelatedX = origX - (origX % pixelSize)
    pixelatedY = origY - (origY % pixelSize)

    # Obtiene el color del píxel pixelado
    pixelatedColor = texture.getColor(pixelatedX / texture.width, pixelatedY / texture.height)

    return pixelatedColor




def dotsShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Tamaño y separación de los puntos
    dotSize = 0.015
    dotSpacing = 0.03

    # Calcula las coordenadas normalizadas de los puntos
    dotX = texCoords[0] % dotSpacing
    dotY = texCoords[1] % dotSpacing

    # Compara con el tamaño del punto para determinar si se colorea el punto
    if dotX < dotSize and dotY < dotSize:
        return color
    else:
        return (0, 0, 0)  # Punto negro si no está dentro del área del punto






























def fragmentShader(**kwargs):

    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]

    if texture != None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1,1,1)

    return color