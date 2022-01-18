class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for s, e in self.edges:
            if s in self.graph_dict:
                self.graph_dict[s].append(e)
            else:
                self.graph_dict[s] = [e]

    def get_paths(self, s, e, path=[]):
        path = path + [s]
        if s == e:
            return [path]
        if s not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[s]:
            if node not in path:
                new_paths = self.get_paths(node, e, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, s, e, path=[]):
        path = path + [s]

        if s == e:
            return path

        if s not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[s]:
            if node not in path:
                sp = self.get_shortest_path(node, e, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))

    start = "Dubai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ", route_graph.get_paths(start, end))
    print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start, end))
