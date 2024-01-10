class graph:
    # an edge list for the graph
    # each vertex is a tuple containing the index of the vertex and a list of connected vertices
    vertices = []
    # adds a vertex to the graph, at the index is the list of vertices of the vertices index
    # returns: nothing
    # index: the desired index of the added vertex
    def addVertex(self, index):
        if len(self.vertices) == index:
            self.vertices.append((index, []))
        elif len(self.vertices) > index:
            oldOutgoingEdges = self.vertices[index][1]
            self.vertices[index] = (index, oldOutgoingEdges)
        else:
            while len(self.vertices) < index:
                self.vertices.append((-1, []))
            self.vertices.append((index, []))
    # indicates if the graph contains a vertex of the given index
    # returns: true if the graph contains a vertex with the given index
    # index: the desired index for the graph to contain
    def containsVertex(self, index):
        if len(self.vertices) <= index:
            return False
        elif self.vertices[index][0] != -1:
            return True
        return False
    # adds an edge to the graph, doing nothing if either of the vertices dont exist
    # returns: nothing
    # index1: the index of the outgoing edge
    # index2: the index of the incoming edge
    def addEdge(self, index1, index2):
        if self.containsVertex(index1) & self.containsVertex(index2):
            if self.containsEdge(index1, index2) == False:
                self.vertices[index1][1].append(index2)

    # indicates if index1 has an outgoing edge to index2
    # returns: true if index1 has an outgoing edge to index2, false otherwise
    # index1: the index of the desired outgoing edge
    # index2: the index of the desired incoming edge
    def containsEdge(self, index1, index2):
        if self.containsVertex(index1) & self.containsVertex(index2):
            for edge in self.vertices[index1][1]:
                if (edge == index2):
                    return True
        return False
    # prints the graph
    # returns: nothing
    def printGraph(self):
        print(self.vertices)
    # gets a list of all vertices in the graph
    # returns: the list of vertices
    def getVertexList(self):
        vertexList = []
        for vertex in self.vertices:
            if vertex[0] != -1:
                vertexList.append(vertex[0])
        return vertexList
    # indicates if the graph is connected
    # returns: true if the graph is connected, false otherwise
    def isConnected(self):
        totalVertices = self.getVertexList()
        if len(self.getVertexList()) <= 1:
            return True
        explorableVertices = [totalVertices[0]]
        exploredVertices = []
        while (len(explorableVertices) + len(exploredVertices) < len(totalVertices) and len(explorableVertices) > 0): # worst case O(n)
            nodeBeingExplored = explorableVertices[0]
            explorableVertices.remove(nodeBeingExplored)
            exploredVertices.append(nodeBeingExplored)
            for node in self.vertices[nodeBeingExplored][1]:
                if node not in explorableVertices and node not in exploredVertices:
                    explorableVertices.append(node)
        if len(explorableVertices) + len(exploredVertices) == len(totalVertices):
            return True
        return False