from Imports import *
from Graph import Graph
from Data_handler import Data_handler
from Subplot import Subplot

class Plotter:
    def __init__(self):
        self.subplots  = []
        self.graph = None
        self.graph_types = {"plot": plt.plot, "scatter": plt.scatter, "bar": plt.bar, "stem" : plt.stem,
                            "fill_between" : plt.fill_between, "stackplot" : plt.stackplot, "stairs" : plt.stairs,
                            "hist": plt.hist, "boxplot": plt.boxplot, "heatmap": plt.imshow, "contour": plt.contour,
                            "contourf" : plt.contourf, "quiver" : plt.quiver, "plot3d": plt3d.plot, "bar3d": plt3d.bar,
                            "quiver3d" : plt3d.quiver, "stem3d": plt3d.stem, "plot_wireframe": plt3d.plot_wireframe,
                            "plot_surface": plt3d.plot_surface , "scatter3d": plt3d.scatter}
        self.threed_graphs = ["plot3d", "bar3d", "quiver3d", "stem3d", "plot_wireframe", "plot_surface", "scatter3d"]

    def add_subplot(self, subplot: Subplot):
        self.subplots.append(subplot)


    def plot_graph(self):
        if self.graph is None:
            return
        if self.graph.graph_type in self.graph_types:
            if self.graph.graph_type in self.threed_graphs:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                self.graph_types[self.graph.graph_type](ax, self.graph.x, self.graph.y, self.graph.z, **self.graph.kwgraph_args)
                ax.set_title(self.graph.title)
                ax.set_xlabel(self.graph.x_label)
                ax.set_ylabel(self.graph.y_label)
                ax.set_zlabel(self.graph.z_label)
                plt.show()
            else:
                self.graph_types[self.graph.graph_type](self.graph.x, self.graph.y, **self.graph.kwgraph_args)
                plt.title(self.graph.title)
                plt.xlabel(self.graph.x_label)
                plt.ylabel(self.graph.y_label)
                plt.show()


    def plot_subplots(self):
        for subplot in self.subplots:
            if subplot.graph.graph_type in self.graph_types:
                if subplot.graph.graph_type in self.threed_graphs:
                    fig = plt.figure()
                    ax = fig.add_subplot(subplot.position, projection='3d')
                    self.graph_types[subplot.graph.graph_type](ax, subplot.graph.x, subplot.graph.y, subplot.graph.z, **subplot.graph.kwgraph_args)
                    ax.set_title(subplot.graph.title)
                    ax.set_xlabel(subplot.graph.x_label)
                    ax.set_ylabel(subplot.graph.y_label)
                    ax.set_zlabel(subplot.graph.z_label)

                else:
                    plt.subplot(subplot.position)
                    self.graph_types[subplot.graph.graph_type](subplot.graph.x, subplot.graph.y, **subplot.graph.kwgraph_args)
                    plt.title(subplot.graph.title)
                    plt.xlabel(subplot.graph.x_label)
                    plt.ylabel(subplot.graph.y_label)
        plt.show()