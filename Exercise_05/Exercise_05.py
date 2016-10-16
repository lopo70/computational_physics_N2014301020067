# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
class trajectory(object):
    def __init__(self,initial_speed):
        self.x = [[]]
        self.y = [[]]
        self.v_0 = initial_speed
        self.v_x = [[]]
        self.v_y = [[]]
        self.initial_angle = [30,35,40,45,50,55,60]
        self.delta_t = 0.1
    def calculate(self):
        g = 0.0098
        for i in self.initial_angle:
            self.x[-1].append([0])
            self.y[-1].append([0])
            self.v_x[-1].append([self.v_0 * math.cos((float(i) / 180) * math.pi)])
            self.v_y[-1].append([self.v_0 * math.sin((float(i) / 180) * math.pi)])
            while (self.y[-1][-1][-1] > 0) or (self.x[-1][-1][-1] == 0):
                self.v_x[-1][-1].append(self.v_x[-1][-1][-1])
                self.v_y[-1][-1].append(self.v_y[-1][-1][-1] - g * self.delta_t)
                self.x[-1][-1].append(self.x[-1][-1][-1] + self.v_x[-1][-1][-1] * self.delta_t)
                self.y[-1][-1].append(self.y[-1][-1][-1] + self.v_y[-1][-1][-1] * self.delta_t)
            if self.y[-1][-1][-1] < 0:
                r = - (self.y[-1][-1][-2] / self.y[-1][-1][-1])
                self.x[-1][-1][-1] = (self.x[-1][-1][-2] + r * self.x[-1][-1][-1]) / (r + 1)    
    def show_results(self):
        for i in range(len(self.initial_angle)):
            plt.plot(self.x[0][i], self.y[0][i])
            plt.annotate('%d'%self.initial_angle[i],xy=(25,6 + 2 * i))
        plt.title('Trajectory of cannon shell')
        plt.xlabel('x (km)')
        plt.ylabel('y (km)')
        plt.ylim(0,)
        plt.show()
class with_air_drag(trajectory):
    def calculate_with_air_drag(self):
        self.x.append([])
        self.y.append([])
        self.v_x.append([])
        self.v_y.append([])
        g = 0.0098
        B_2_divided_by_m = 0.04
        for i in self.initial_angle:
            self.x[-1].append([0])
            self.y[-1].append([0])
            self.v_x[-1].append([self.v_0 * math.cos((float(i) / 180) * math.pi)])
            self.v_y[-1].append([self.v_0 * math.sin((float(i) / 180) * math.pi)])
            while (self.y[-1][-1][-1] > 0) or (self.x[-1][-1][-1] == 0):
                v = math.sqrt((self.v_x[-1][-1][-1]) ** 2 + (self.v_y[1][-1][-1]) ** 2)
                self.x[-1][-1].append(self.x[-1][-1][-1] + self.v_x[-1][-1][-1] * self.delta_t)
                self.y[-1][-1].append(self.y[-1][-1][-1] + self.v_y[-1][-1][-1] * self.delta_t)
                self.v_x[-1][-1].append(self.v_x[-1][-1][-1] - B_2_divided_by_m * v * self.v_x[-1][-1][-1] * self.delta_t)
                self.v_y[-1][-1].append(self.v_y[-1][-1][-1] - (g + B_2_divided_by_m * v * self.v_y[-1][-1][-1]) * self.delta_t)
            if self.y[-1][-1][-1] < 0:
                r = - (self.y[-1][-1][-2] / self.y[-1][-1][-1])
                self.x[-1][-1][-1] = (self.x[-1][-1][-2] + r * self.x[-1][-1][-1]) / (r + 1)
    def show_results(self):
        plt.subplot(121)
        for i in range(len(self.initial_angle)):
            plt.plot(self.x[0][i], self.y[0][i])
            plt.annotate(r'$%d^\circ$'%self.initial_angle[i],xy=(25,6 + 2 * i))
        plt.title('Trajectory of cannon shell')
        plt.xlabel('x (km)')
        plt.ylabel('y (km)')
        plt.xlim(0,60)
        plt.ylim(0,20)
        plt.text(40,17,'No drag')
        plt.subplot(122)
        for j in range(len(self.initial_angle)):
            plt.plot(self.x[1][j], self.y[1][j])
        plt.title('Trajectory of cannon shell')
        plt.xlabel('x (km)')
        plt.ylabel('y (km)')
        plt.xlim(0,60)
        plt.ylim(0,20)
        plt.text(40,17,'With air drag')
        plt.show()
class g_depand_on_altitude(trajectory):
    def calculate_g_depand_on_altitude(self):
        self.x.append([])
        self.y.append([])
        self.v_x.append([])
        self.v_y.append([])
        g_0 = 0.0098
        R = 6371
        for i in self.initial_angle:
            self.x[-1].append([0])
            self.y[-1].append([0])
            self.v_x[-1].append([self.v_0 * math.cos((float(i) / 180) * math.pi)])
            self.v_y[-1].append([self.v_0 * math.sin((float(i) / 180) * math.pi)])
            while (self.y[-1][-1][-1] > 0) or (self.x[-1][-1][-1] == 0):
                self.v_x[-1][-1].append(self.v_x[-1][-1][-1])
                self.v_y[-1][-1].append(self.v_y[-1][-1][-1] - g_0 * (float(R) / (R + self.y[-1][-1][-1])) * self.delta_t)
                self.x[-1][-1].append(self.x[-1][-1][-1] + self.v_x[-1][-1][-1] * self.delta_t)
                self.y[-1][-1].append(self.y[-1][-1][-1] + self.v_y[-1][-1][-1] * self.delta_t)
            if self.y[-1][-1][-1] < 0:
                r = - (self.y[-1][-1][-2] / self.y[-1][-1][-1])
                self.x[-1][-1][-1] = (self.x[-1][-1][-2] + r * self.x[-1][-1][-1]) / (r + 1)
    def show_results(self):
        plt.subplot(121)
        for i in range(len(self.initial_angle)):
            plt.plot(self.x[0][i], self.y[0][i])
            plt.annotate(r'$%d^\circ$'%self.initial_angle[i],xy=(1700,450 + 150 * i))
        plt.title('Trajectory of cannon shell')
        plt.xlabel('x (km)')
        plt.ylabel('y (km)')
        plt.xlim(0,4500)
        plt.ylim(0,1600)
        plt.text(3000,1400,'g is a constant')
        plt.subplot(122)
        for j in range(len(self.initial_angle)):
            plt.plot(self.x[1][j], self.y[1][j])
        plt.title('Trajectory of cannon shell')
        plt.xlabel('x (km)')
        plt.ylabel('y (km)')
        plt.xlim(0,4500)
        plt.ylim(0,1600)
        plt.text(3000,1400,'g depends on altitude')
        plt.show()
a=g_depand_on_altitude(6)
a.calculate()
a.calculate_g_depand_on_altitude()
a.show_results()