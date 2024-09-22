from Imports import *
from Graph import Graph
from Data_handler import Data_handler
from Subplot import Subplot
from Plotter import Plotter

class Interface:
    def __init__(self):
        self.plotter = Plotter()
        self.graph_types = {colour.blue + "Pairwise (plot, scatter, bar, etc)" + colour.reset: 1, colour.red + "Distribution (histogram, boxplot, etc)" + colour.reset :2,
                            colour.green + "Gridded (heatmap, contour, etc)" + colour.reset: 3, colour.bright_white + "3D (scatter, surface, etc)" + colour.reset: 4}

        self.pairwise_graphs = {"plot": plt.plot, "scatter": plt.scatter, "bar": plt.bar, "stem" : plt.stem,
                            "fill_between" : plt.fill_between, "stackplot" : plt.stackplot, "stairs" : plt.stairs}
        self.distribution_graphs = {"hist": plt.hist, "boxplot": plt.boxplot}
        self.gridded_graphs = {"heatmap": plt.imshow, "contour": plt.contour, "contourf" : plt.contourf, "quiver" : plt.quiver}
        self.three_d_graphs = {"plot3d": plt3d.plot, "bar3d": plt3d.bar, "quiver3d" : plt3d.quiver, "stem3d": plt3d.stem,
                            "plot_wireframe": plt3d.plot_wireframe, "plot_surface": plt3d.plot_surface , "scatter3d": plt3d.scatter}



    def get_file(self):
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt"),
                                                          ("Excel files", "*.xlsx"), ("JSON files", "*.json"),
                                                          ("SQL files", "*.sql"), ("All files", "*.*")])
        return file_path


    def choose_graph_type(self, graph_type_dict, graph_type_name):
        print("Choose the type of %s graph you want to plot:".format(graph_type_name))
        for key in graph_type_dict:
            print(key)
        try:
            graph = input(colour.cyan + "Enter the type corresponding to the graph type (-1 to go back): " + colour.reset)
        except ValueError:
            print(colour.bright_red + "Invalid choice. Please try again." + colour.reset)
            return None
        if graph in graph_type_dict:
            return graph
        elif graph == "-1":
            return None
        else:
            print("Invalid choice. Please try again.")


    def ask_for_type_graph(self):
        while True:
            while True:
                print("Choose the type of graph you want to plot:")
                for key in self.graph_types:
                    print(key + " (" + str(self.graph_types[key]) + ")")
                graph_type = int(input(colour.cyan + "Enter the number corresponding to the graph type (-1 to go back): " + colour.reset))
                if graph_type in self.graph_types.values():
                    break
                elif graph_type == -1:
                    return None
                else:
                    print("Invalid choice. Please try again.")
            graph_type_detail = None
            if graph_type == 1:
                graph_type_detail = self.choose_graph_type(self.pairwise_graphs, "pairwise")
            elif graph_type == 2:
                graph_type_detail = self.choose_graph_type(self.distribution_graphs, "distribution")
            elif graph_type == 3:
                graph_type_detail = self.choose_graph_type(self.gridded_graphs, "gridded")
            elif graph_type == 4:
                graph_type_detail = self.choose_graph_type(self.three_d_graphs, "3D")
            else:
                print("Invalid choice. Please try again.")
                continue
            if graph_type_detail is None:
                continue
            else:
                break
        return graph_type_detail


    def ask_graph_title(self):
        print("What would you like the title of the graph to be?")
        title = input(colour.cyan + "Title: " + colour.reset)
        return title


    def ask_graph_labels(self):
        bool_label = input(colour.cyan + "Would you like to manually enter the x and y axis labels? (y/n, default=n): " + colour.reset)
        if bool_label == "n" or bool_label == "":
            return None, None
        x_label = input(colour.cyan + "X-axis label: " + colour.reset)
        y_label = input(colour.cyan + "Y-axis label: " + colour.reset)
        return x_label, y_label


    def ask_subplot_position(self):
        position = input(colour.cyan + "Enter the position of the subplot (row, column, index): " + colour.reset)
        return position


    def ask_args(self):
        print("Would you like to add any arguments to the graph?")
        print("1. Yes")
        print("2. No")
        choice = input(colour.cyan + "Enter the number corresponding to your choice: " + colour.reset)
        if choice == "1":
            print("Enter the arguments you would like to add to the graph in the form of a dictionary.")
            print("Example: {'color': 'red', 'linestyle': 'dashed'}")
            args = input(colour.cyan + "Arguments: " + colour.reset)
            return args
        elif choice == "2":
            return None
        else:
            print("Invalid choice. Please try again.")


    def loop(self):
        data_handler = Data_handler()
        while True:
            print("What would you like to do?")
            print(colour.blue + "1.Plot a graph" + colour.reset)
            print(colour.green + "2.Plot a graph with subplots" + colour.reset)
            print(colour.red + "3.Exit" + colour.reset)
            choice = input(colour.cyan + "Enter the number corresponding to your choice: " + colour.reset)
            if choice == "1":
                type_graph = self.ask_for_type_graph()
                if type_graph is None:
                    continue
                else:
                    graph = data_handler.read_data(self.get_file())
                    graph.graph_type = type_graph
                    graph.title = self.ask_graph_title()
                    x_label, y_label = self.ask_graph_labels()
                    if x_label is not None or y_label is not None:
                        graph.x_label = x_label
                        graph.y_label = y_label
                    args = self.ask_args()
                    if args is not None and args[0] == "{" and args[-1] == "}":
                        try:
                            graph.kwgraph_args = eval(args)
                        except SyntaxError:
                            print("Invalid arguments. Continuing without arguments.")
                            graph.kwgraph_args = {}
                            continue
                    self.plotter.graph = graph
                    self.plotter.plot_graph()

            elif choice == "2":
                print("How many subplots would you like to add? (Each subplot will need it's own data file)")
                num_subplots = int(input(colour.cyan + "Number of subplots: " + colour.reset))
                for i in range(num_subplots):
                    type_graph = self.ask_for_type_graph()
                    if type_graph is None:
                        continue
                    else:
                        graph = data_handler.read_data(self.get_file())
                        graph.graph_type = type_graph
                        graph.title = self.ask_graph_title()
                        x_label, y_label = self.ask_graph_labels()
                        if x_label is not None or y_label is not None:
                            graph.x_label = x_label
                            graph.y_label = y_label
                        args = self.ask_args()
                        if args is not None and args[0] == "{" and args[-1] == "}":
                            try:
                                graph.kwgraph_args = eval(args)
                            except SyntaxError:
                                print("Invalid arguments. Continuing without arguments.")
                                graph.kwgraph_args = {}
                                continue
                        try:
                            position = int(self.ask_subplot_position())
                        except ValueError:
                            print("Invalid position. Please try again.")
                            position = int(self.ask_subplot_position())
                        subplot = Subplot(graph)
                        subplot.position = position
                        self.plotter.add_subplot(subplot)
                self.plotter.plot_subplots()

            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")