from Imports import *
from Graph import Graph


class Data_handler:
    def __init__(self):
        self.data = None

    # Data should be in the from of headers with columns of data, first row should be the headers, (x, y, z)
    def read_data(self, file_path):
        self.data = None
        if file_path.endswith(".csv"):
            self.data = pd.read_csv(file_path)
        elif file_path.endswith(".txt"):
            self.data = pd.read_csv(file_path, delimiter="\t")
        elif file_path.endswith(".xlsx"):
            self.data = pd.read_excel(file_path)
        elif file_path.endswith(".json"):
            self.data = pd.read_json(file_path)
        elif file_path.endswith(".sql"):
            self.data = pd.read_sql(file_path)
        else:
            print("Invalid file format. Please try again.")
            return None
        return self.classify_data()


    def classify_data(self):
        if self.data is None:
            return None
        graph = Graph()
        count = 0
        data_label_x = None
        data_label_y = None
        data_label_z = None
        x = []
        y = []
        z = []
        for column in self.data.columns.values:
            if count == 0:
                data_label_x = column
                x = self.data[column].values
            elif count == 1:
                data_label_y = column
                y = self.data[column].values
            elif count == 2:
                data_label_z = column
                z = self.data[column].values
            count += 1
        graph.x = x
        graph.x_label = data_label_x
        graph.y = y
        graph.y_label = data_label_y
        if z is not []:
            graph.z = z
            graph.z_label = data_label_z
        return graph
