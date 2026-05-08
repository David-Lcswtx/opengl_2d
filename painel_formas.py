import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math

def painelFormas():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(-0.6, 0.8)
    gl.glVertex2f(-0.8, 0.4)
    gl.glVertex2f(-0.4, 0.4)
    gl.glEnd()

    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-0.4, -0.8)
    gl.glVertex2f(-0.8, -0.8)
    gl.glVertex2f(-0.8, -0.4)
    gl.glVertex2f(-0.4, -0.4)
    gl.glEnd()

    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(0.6, 0.6)
    for i in range(51):
        angle = i * 2 * math.pi / 50
        x = 0.6 + 0.2 * math.cos(angle)
        y = 0.6 + 0.2 * math.sin(angle)
        gl.glVertex2f(x, y)
    gl.glEnd()

    gl.glColor3f(1.0, 1.0, 0.0)
    gl.glBegin(gl.GL_POLYGON)
    gl.glVertex2f(0.5, -0.4)
    gl.glVertex2f(0.7, -0.4)
    gl.glVertex2f(0.8, -0.6)
    gl.glVertex2f(0.7, -0.8)
    gl.glVertex2f(0.5, -0.8)
    gl.glVertex2f(0.4, -0.6)
    gl.glEnd()

    glut.glutSwapBuffers()

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(600, 600)
glut.glutCreateWindow(b"O Painel de Formas")
glut.glutDisplayFunc(painelFormas)
glut.glutMainLoop()