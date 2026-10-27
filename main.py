import sys
import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        sys.exit("Failed to initialize GLFW")

    # Request OpenGL 3.3 Core Profile (fixed constant names)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window = glfw.create_window(800, 600, "Lab 01 - Clear Window", None, None)
    if not window:
        glfw.terminate()
        sys.exit("Failed to create GLFW window")

    glfw.make_context_current(window)

    # Print OpenGL version and renderer details
    gl_version = glGetString(GL_VERSION).decode('utf-8')
    gl_renderer = glGetString(GL_RENDERER).decode('utf-8')
    print(f"GL Version: {gl_version}")
    print(f"Renderer: {gl_renderer}")

    # Custom Clear Color: Deep Teal Blue
    glClearColor(0.12, 0.22, 0.32, 1.0)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()