import matplotlib.pyplot as plt
import numpy as np

class Octago:
    def __init__(self, length):
        self.rad = 3 * 3.14 / 4
        self.length = length
        self.kof = 1 + 2 ** 0.5

    def perimetor_area(self):
        area = 2 * self.kof * self.length ** 2 
        perimetor = self.length * 8
        return area, perimetor
    
    def opis_octa(self):
        radius_op = self.length / (2 - 2 ** 0.5) ** 0.5
        area = 3.14 * radius_op ** 2
        return radius_op, area

    def vpis_octa(self):
        radius_vp = self.length / 2 * self.kof
        area =  3.14 * radius_vp ** 2
        return radius_vp, area
    def draw(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.set_aspect('equal')

        r_opis, _ = self.opis_octa()
        r_vpis, _ = self.vpis_octa()
        
        x = [r_opis * np.cos(i * np.pi / 4) for i in range(8)]
        y = [r_opis * np.sin(i * np.pi / 4) for i in range(8)]
        
        ax.fill(x, y, color='black')

        circle_out = plt.Circle((0, 0), r_opis, color="blue", fill=False)
        ax.add_patch(circle_out)

        circle_in = plt.Circle((0, 0), r_vpis, color="red", fill=False)
        ax.add_patch(circle_in)

        plt.grid()
        plt.show()