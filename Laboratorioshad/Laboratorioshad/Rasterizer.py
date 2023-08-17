
import shaders
from obj import Obj
from gl import Renderer

# La resolucion de la imagen generada
width = 960    # Ancho en pixeles
height = 540   # Alto en pixeles

# Inicializar el Renderer con la resolucion definida
rend = Renderer(width, height)

# Se brindan los shaders a utilizar
rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader


#rend.fragmentShader = shaders.stylizedEdgeDetectionShader
#rend.fragmentShader = shaders.pixelateFragmentShader
rend.fragmentShader = shaders.dotsShader

# metodo look At
rend.glLookAt(camPos=(-2, 0, 0),
              eyePos=(0, 0, -5))


# Cargar el modelo en el renderizador
 

rend.glLoadModel(filename = "model.obj",              
                 textureName = "model.bmp",           
                 translate = (0,0,-5),                
                 rotate = (0,0,0),                    
                 scale = (2,2,2))




# Renderizar el modelo en la imagen
rend.glRender()

# Se crea el FrameBuffer con la imagen renderizada
rend.glFinish("output2.bmp")      