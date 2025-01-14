import numpy as np

from screen import Screen
from camera import PerspectiveCamera,OrthoCamera
from mesh import Mesh
from renderer import Renderer
from light import PointLight



if __name__ == '__main__':
    screen = Screen(500,500)

    camera = PerspectiveCamera(-1.0, 1.0, -1.0, 1.0, -1.5, -10)
    camera.transform.set_position(0, 0, 3)


    mesh = Mesh.from_stl("suzanne.stl", np.array([1.0, 0.0, 1.0]),\
        np.array([1.0, 1.0, 1.0]),0.05,1.0,0.2,100)
    #mesh.transform.set_position(0,-10,0)
    mesh.transform.set_rotation(15, -20, 0)

    light = PointLight(50.0, np.array([1, 1, 1]))
    light.transform.set_position(-1, 5, 5)

    renderer = Renderer(screen, camera, [mesh], light)
    renderer.render("flat",[80,80,80], [0.2, 0.2, 0.2])

    screen.show()