import OpenGL.GL as gl
import OpenGL.GLUT as glut


def desenhaTriangulo(base, altura, x, y, cor):
    gl.glColor3f(*cor)
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(x - base / 2, y)
    gl.glVertex2f(x + base / 2, y)
    gl.glVertex2f(x, y + altura)
    gl.glEnd()


def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    desenhaTriangulo(b, a, 0.0, 0.0, (0.0, 1.0, 1.0))

    desenhaTriangulo(0.3, 0.3, -0.6, 0.5, (1.0, 0.0, 0.0))
    desenhaTriangulo(0.8, 0.2, 0.4, -0.7, (0.0, 0.1, 0.1))
    desenhaTriangulo(0.1, 0.9, -0.8, -0.8, (0.0, 0.0, 0.1))
    desenhaTriangulo(0.4, 0.4, 0.5, 0.2, (1.0, 1.0, 0.0))
    desenhaTriangulo(0.2, 0.6, -0.3, -0.5, (1.0, 0.0, 1.0))

    glut.glutSwapBuffers()


b = float(input("Digite a base: "))
a = float(input("Digite a altura: "))

glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(700, 700)
glut.glutCreateWindow(b"A Alianca dos Triangulos")
glut.glutDisplayFunc(display)
glut.glutMainLoop()
