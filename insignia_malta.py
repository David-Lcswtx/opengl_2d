import OpenGL.GL as gl
import OpenGL.GLUT as glut
import random

cor_atual = [1.0, 0.0, 0.0]


def desenharInsignia():

    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glColor3f(cor_atual[0], cor_atual[1], cor_atual[2])
    gl.glBegin(gl.GL_TRIANGLES)

    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(0.3, 0.7)
    gl.glVertex2f(0.0, 0.5)

    gl.glVertex2f(-0.3, 0.7)
    gl.glVertex2f(0.0, 0.5)
    gl.glVertex2f(0.0, 0.0)

    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(-0.7, 0.3)
    gl.glVertex2f(-0.5, 0.0)

    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(-0.5, 0.0)
    gl.glVertex2f(-0.7, -0.3)

    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(0.0, -0.5)
    gl.glVertex2f(0.3, -0.7)

    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(0.0, -0.5)
    gl.glVertex2f(-0.3, -0.7)

    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(0.7, 0.3)
    gl.glVertex2f(0.5, 0.0)

    gl.glVertex2f(0.0, 0.0)
    gl.glVertex2f(0.5, 0.0)
    gl.glVertex2f(0.7, -0.3)

    gl.glEnd()

    glut.glutSwapBuffers()


def atualizarCor(key, x, y):
    global cor_atual
    if key == b"c":
        cor_atual = [random.random(), random.random(), random.random()]
        glut.glutPostRedisplay()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(400, 400)
glut.glutCreateWindow(b"A Insignia de Malta")
glut.glutDisplayFunc(desenharInsignia)
glut.glutKeyboardFunc(atualizarCor)
glut.glutMainLoop()
