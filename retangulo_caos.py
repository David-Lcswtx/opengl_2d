import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random

cor_retangulo = [0.1, 0.1, 0.1]


def desenhaRetangulo(base, altura):
    gl.glColor3f(cor_retangulo[0], cor_retangulo[1], cor_retangulo[2])
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-base / 2, -altura / 2)
    gl.glVertex2f(base / 2, -altura / 2)
    gl.glVertex2f(base / 2, altura / 2)
    gl.glVertex2f(-base / 2, altura / 2)
    gl.glEnd()


def display():

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    desenhaRetangulo(l, a)
    gl.glFlush()


l = float(input("Digite a largura do retangulo: "))
a = float(input("Digite a altura do retangulo: "))


def atualizarCor(key, x, y):
    global cor_retangulo
    if key == b" ":
        cor_retangulo = [random.random(), random.random(), random.random()]
        cor_fundo = [random.random(), random.random(), random.random()]
        gl.glClearColor(cor_fundo[0], cor_fundo[1], cor_fundo[2], 1.0)
        glut.glutPostRedisplay()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
glut.glutInitWindowSize(512, 512)
glut.glutCreateWindow(b"O Retangulo do Caos")
glut.glutDisplayFunc(display)
glut.glutKeyboardFunc(atualizarCor)
glut.glutMainLoop()
