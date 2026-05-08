import OpenGL.GL as gl
import OpenGL.GLUT as glut


def desenhaTexto(x, y, cor, texto):
    gl.glColor3f(*cor)
    gl.glRasterPos2f(x, y)
    for char in texto:
        glut.glutBitmapCharacter(glut.GLUT_BITMAP_HELVETICA_18, ord(char))


def dominioEspaco():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glColor3f(1.0, 1.0, 1.0)
    gl.glBegin(gl.GL_LINES)
    gl.glVertex2f(-1.0, 0.0)
    gl.glVertex2f(1.0, 0.0)
    gl.glVertex2f(0.0, -1.0)
    gl.glVertex2f(0.0, 1.0)
    gl.glEnd()

    gl.glShadeModel(gl.GL_FLAT)

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glVertex2f(-0.8, 0.2)
    gl.glVertex2f(-0.6, 0.8)
    gl.glVertex2f(-0.4, 0.2)

    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex2f(0.0, 0.4)
    gl.glVertex2f(0.2, 0.8)
    gl.glVertex2f(0.8, 0.4)

    gl.glColor3f(0.0, 1.0, 1.0)
    gl.glVertex2f(-0.4, -0.8)
    gl.glVertex2f(0.2, -0.4)
    gl.glVertex2f(0.9, -0.8)

    gl.glEnd()

    desenhaTexto(-0.8, 0.14, (1, 0, 0), "V1 = (-0.8, 0.2)")
    desenhaTexto(-0.6, 0.83, (1, 0, 0), "V2 = (0.0, 0.4)")
    desenhaTexto(-0.4, 0.14, (1, 0, 0), "V3 = (-0.4, 0.2)")

    desenhaTexto(0.0, 0.34, (0, 1, 0), "V1 = (0.0, 0.4)")
    desenhaTexto(0.2, 0.83, (0, 1, 0), "V2 = (0.2, 0.8)")
    desenhaTexto(0.6, 0.34, (0, 1, 0), "V3 = (0.8, 0.4)")

    desenhaTexto(-0.4, -0.86, (0, 1, 1), "V1 = (-0.4, -0.8)")
    desenhaTexto(0.2, -0.38, (0, 1, 1), "V2 = (0.2, -0.4)")
    desenhaTexto(0.6, -0.86, (0, 1, 1), "V3 = (0.9, -0.8)")

    glut.glutSwapBuffers()


glut.glutInit()
glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)
glut.glutInitWindowSize(700, 700)
glut.glutCreateWindow(b"O Dominio do Espaco")
glut.glutDisplayFunc(dominioEspaco)
glut.glutMainLoop()
