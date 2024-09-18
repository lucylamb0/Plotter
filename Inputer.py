from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as plt3d


class Data:
    def __init__(self):
        self.data = []
        self.data_type = ""
        self.data_name = ""
        self.data_file = ""


class Graph:
    def __init__(self):
        self.kwgraph_args = {}
        self.x = []
        self.y = []
        self.z = []
        self.title = ""
        self.x_label = ""
        self.y_label = ""
        self.z_label = ""
        self.graph_type = None # plot, scatter, bar, etc
        self.dimensions = 1


class Subplot:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.position = (0, 0, 0)


class Plotter:
    def __init__(self):
        self.subplots  = []
        self.graph = None
        self.graph_types = {"plot": plt.plot, "scatter": plt.scatter, "bar": plt.bar, "stem" : plt.stem,
                            "fill_between" : plt.fill_between, "stackplot" : plt.stackplot, "stairs" : plt.stairs,
                            "hist": plt.hist, "boxplot": plt.boxplot, "heatmap": plt.imshow, "contour": plt.contour,
                            "contourf" : plt.contourf, "quiver" : plt.quiver, "plot3d": plt3d.plot, "bar3d": plt3d.bar,
                            "quiver3d" : plt3d.quiver, "stem3d": plt3d.stem, "plot_wireframe": plt3d.plot_wireframe,
                            "plot_surface": plt3d.plot_surface , "scatter3d": plt3d.scatter, }

    def add_subplot(self, subplot: Subplot):
        self.subplots.append(subplot)

    def plot_subplots(self):
        if len(self.subplots) == 0:
            return
        for subplot in self.subplots:
            ax = plt.subplot(subplot.position[0], subplot.position[1], subplot.position[2])
            subplot.graph.graph_type(subplot.graph.kwgraph_args)



class Interface:
    def __init__(self):
        self.input_string = ""
        self.graph_types = ["Pairwise (plot, scatter, bar, etc)", "Distribution (histogram, boxplot, etc)",
                            "Gridded (heatmap, contour, etc)", "3D (scatter, surface, etc)"]


    def get_input(self, output_string):
        self.input_string = input(output_string)

    def get_file(self):
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def ask_for_type_graph(self):
