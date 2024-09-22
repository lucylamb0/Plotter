class Graph:
    def __init__(self):
        self.manual_labels = False
        self.kwgraph_args = {}
        self.x = []
        self.y = []
        self.z = []
        self.title = ""
        self.x_label = ""
        self.y_label = ""
        self.z_label = ""
        self.graph_type = None # plot, scatter, bar, etc