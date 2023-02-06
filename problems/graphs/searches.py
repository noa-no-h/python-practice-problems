import math
class Vertex:

    def __init__(self, name):
        self.name = name
        self.edges_to = {}
    
    def add_edge_to(self, dest, weight):
        self.edges_to[dest] = weight
        
    def has_edge_to(self, dest):
        return dest in self.edges_to
        
    def weight_to_dest(self, dest):
        return self.edges_to[dest]

            
class Graph:

    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = vertex.name
        
    def get_vertex(self, vertex):
        return self.vertices.get(vertex)

    def print_DFS_r(self, start, visited):
        visited.add(start)
        print(start.name)
        for neighbor in start.edges_to.keys():
            if neighbor not in visited:
                self.print_DFS_r(neighbor, visited)
    
    def print_DFS(self, start):
        self.print_DFS_r(start, set())


    def print_BFS(self, start):
        q = []
        encountered = set()
        encountered.add(start)
        q.append(start)
        while q:
            print([v.name for v in q])
            processing = q.pop(0)
            print(processing.name)
            encountered.add(processing)
            for neighbor in processing.edges_to.keys():
                if neighbor not in encountered:
                    q.append(neighbor)
                    encountered.add(neighbor)

    def dijkstra(self, start, end):
        priority_queue = Minheap()
        previous = {}
        distance = {}
        for vertex in self.vertices:
            distance[vertex] = math.inf
        distance[start] = 0
        priority_queue.insert(start, 0)

        while priority_queue:
            current_vertex_tuple = priority_queue.pop_min()
            current_vertex = current_vertex_tuple[0]
            if current_vertex == end:
                return self.build_path(start, end)
            for neighbor in current_vertex.edges_to:
                new_distance = distance[current_vertex]\
                               + current_vertex.edges_to[neighbor]
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    previous[neighbor] = current_vertex
                    if neighbor in priority_queue.index_of_item:
                        priority_queue.change_priority(neighbor, new_distance)
                    else:
                        priority_queue.insert(neighbor, new_distance)
    
    def build_path(self, start, end):
        path = [end.name]
        vertex = end
        while vertex != start:
            previous = self.previous[vertex]
            if previous is None:
                return None
            path.insert(0, previous.name)
            vertex = previous
        return path

"""6, 7, 12, 10, 15, 17
m, c1, c2, c11, c12, c21, c22,"""

class Minheap:
    def __init__(self, max_capacity=999):
        self.heap_list = [None] * max_capacity
        self.next = 0
        self.index_of_item = {}

    def parent(self, i):
        return (i-1)//2
    
    def left_index(self, i):
        return 2*i + 1
    
    def right_index(self, i):
        return 2*i + 2

    def insert(self, vertex, weight):
        self.heap_list[self.next] = (vertex, weight)
        self.index_of_item[vertex] = self.next
        self.next += 1
        self.sift_up(self.next - 1)
    
    def swap(self, idx1, idx2):
        tuple1 = self.heap_list[idx1]
        tuple2 = self.heap_list[idx2]
        self.heap_list[idx2] = tuple1
        self.heap_list[idx1] = tuple2
        self.index_of_item[tuple1[0]] = idx2
        self.index_of_item[tuple2[0]] = idx1

    def sift_up(self, idx):
        if idx == 0:
            return
        parent_idx = self.parent(idx)
        if self.heap_list[idx][1] < self.heap_list[parent_idx][1]:
            self.swap(idx, parent_idx)
            self.sift_up(parent_idx)
    
    def get_idx_of_min_child(self, idx):
        print(f'{self.right_index(idx)=}')
        if self.right_index(idx) >= self.next:
            return self.left_index(idx)
        l = self.heap_list[self.left_index(idx)]
        r = self.heap_list[self.right_index(idx)]
        if l[1] < r[1]:
            idx_of_min_child = self.index_of_item[l[0]]
        else:
            idx_of_min_child = self.index_of_item[r[0]]
        return idx_of_min_child

    def sift_down(self, idx):
        if self.left_index(idx) >= self.next:
            return
        idx_of_min_child = self.get_idx_of_min_child(idx)
        if self.heap_list[idx][1] > self.heap_list[idx_of_min_child][1]:
            self.swap(idx, idx_of_min_child)
            self.sift_down(idx_of_min_child)

    def pop_min(self):
        #print(self.heap_list)
        if self.next == 0:
            return None
        min_tuple = self.heap_list[0]
        #print(min_tuple)
        if self.next == 1:
            self.next -= 1
            del self.index_of_item[min_tuple[0]]
            self.heap_list[0] = None
            return min_tuple    
        else:
            self.swap(0, self.next - 1)
            del self.index_of_item[min_tuple[0]]
            self.heap_list[self.next - 1] = None
            self.next -= 1
            self.sift_down(0)
            return min_tuple

    def show_vertices(self):
            """
            prints a representation of the heap for heaps containing vertices

            Parameters:
                None
            Returns: str: representation of heap as tree
            """
            if self.next == 0:
                # don't comment out the next line
                print("[empty]")
                return
            linebreak = 1
            row_count = 0
            for i in range(self.next):
                # don't comment out the next line
                print(self.heap_list[i][0], self.heap_list[i][1], end=" ")
                row_count += 1
                if row_count == linebreak or i == self.next - 1:
                    print()
                    linebreak *= 2
                    row_count = 0
    
    def change_priority(self, item, priority):
        """
        Changes the priority for an item in the heap

        Inputs:
            item: str
            priority: int

        returns:
            (nothing)
        """
        if item not in self.index_of_item:
            raise ValueError
        index = self.index_of_item[item]
        self.heap_list[index] = (item, priority)
        self.sift_up(index)
        self.sift_down(index)



def test_minheap():
    mh = Minheap()
    mh.insert('a',5)
    mh.insert('b',3)
    mh.insert('c',1)
    mh.insert('d',7)
    mh.show_vertices()
    return mh


def sample_graph_print():
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")


    a.add_edge_to(b, 1)
    a.add_edge_to(c, 2)
    a.add_edge_to(d, 1)

    b.add_edge_to(a, 1)
    b.add_edge_to(d, 1)
    b.add_edge_to(f, 1)

    c.add_edge_to(a, 3)
    c.add_edge_to(d, 3)
    c.add_edge_to(e, 3)

    d.add_edge_to(a, 1)
    d.add_edge_to(b, 1)
    d.add_edge_to(c, 1)
    d.add_edge_to(f, 1)

    e.add_edge_to(c, 1)

    f.add_edge_to(b, 2)
    f.add_edge_to(d, 2)

    g = Graph()
    for v in [a, b, c, d, e, f]:
        g.add_vertex(v)
    return g.print_BFS(a)
