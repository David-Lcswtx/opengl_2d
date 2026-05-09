import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random
import math

estrelas = []
modo_noturno = False

def gerarEstrela():
    x = random.uniform(-0.9, 0.9)
    y = random.uniform(-0.9, 0.9)
    
    raio_em_pixels = random.randint(10, 50)
    tamanho_janela = 600.0
    tamanho_opengl = 2.0
    raio_proporcional = (raio_em_pixels * tamanho_opengl) / tamanho_janela

    return {
        'x': x, 
        'y': y, 
        'raio': raio_proporcional, 
        'r': random.random(), 
        'g': random.random(), 
        'b': random.random()
    }

def iniciarConstelacao():
    global estrelas
    estrelas = []
    for _ in range(7):
        estrelas.append(gerarEstrela())

def desenharEstrela(x, y, raio):
    gl.glBegin(gl.GL_POLYGON)
    for i in range(30):
        angulo = 2.0 * math.pi * i / 30
        cx = raio * math.cos(angulo)
        cy = raio * math.sin(angulo)
        gl.glVertex2f(x + cx, y + cy)
    gl.glEnd()

def desenharConstelacao():

    if modo_noturno:
        gl.glClearColor(0.05, 0.05, 0.1, 1.0)
    else:
        gl.glClearColor(0.8, 0.8, 0.9, 1.0)

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    if len(estrelas) > 1:
        gl.glLineWidth(1.0)
        if modo_noturno:
            gl.glColor3f(0.4, 0.4, 0.6)
        else:
            gl.glColor3f(0.3, 0.3, 0.3)
            
        gl.glBegin(gl.GL_LINES)
        for i in range(len(estrelas) - 1):
            gl.glVertex2f(estrelas[i]['x'], estrelas[i]['y'])
            gl.glVertex2f(estrelas[i+1]['x'], estrelas[i+1]['y'])
        gl.glEnd()

    for est in estrelas:
        if modo_noturno:
            gl.glColor3f(1.0, 1.0, 0.0)
        else:
            gl.glColor3f(est['r'], est['g'], est['b'])
            
        desenharEstrela(est['x'], est['y'], est['raio'])

    glut.glutSwapBuffers()

def teclado(key, x, y):
    global modo_noturno, estrelas
    
    if key == b"n":
        estrelas.append(gerarEstrela())
    elif key == b"x":
        if len(estrelas) > 0:
            estrelas.pop()
    elif key == b"r":
        iniciarConstelacao()
    elif key == b"t":
        modo_noturno = not modo_noturno
                        
    glut.glutPostRedisplay()

iniciarConstelacao()
glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(600, 600) 
glut.glutCreateWindow(b"Constelacao dos Guardioes")
glut.glutDisplayFunc(desenharConstelacao)
glut.glutKeyboardFunc(teclado)
glut.glutMainLoop()
