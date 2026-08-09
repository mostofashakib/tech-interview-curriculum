"""
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices
such that for every directed edge uv, vertex u comes before v in the ordering.

Things to note:
    Topological Sorting for a graph is not possible if the graph is not a DAG.
    Topological Sort orderings are not unique
    Topological Sort is used to solve real-world problems such as course scheduling problem, item-assembly
"""

"""
Algorithm: Targan's Topological Sort: Modified Depth-First-Search
    We recursively call topologicalSort for all its adjacent vertices, then push it to a stack. Finally, print contents of stack.
    Note that a vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on) are visited.

Time Complexity: O(V+E)
    V = Vertice
    E = Edge
Space Complexity: O(n)
"""

from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Print contents of the stack 
        print (stack)


"""
Algorithm: Kahn’s algorithm
    Step 1: Compute in-degree (number of incoming edges) for each of the vertex present in the DAG and initialize the count of visited nodes as 0.
    Step 2: Pick all the vertices with in-degree as 0 and add them into a queue (Enqueue operation)
    Step 3: Remove a vertex from the queue (Dequeue operation) and then.
                Increment count of visited nodes by 1.
                Decrease in-degree by 1 for all its neighboring nodes.
                If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.
    Step 4: Repeat Step 3 until the queue is empty.
    Step 5: If count of visited nodes is not equal to the number of nodes in the graph then the topological sort is not possible for the given graph.

Time Complexity: O(V+E)
    V = Vertice
    E = Edge
Space Complexity: O(n)
"""

from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # The function to do Topological Sort.  
    def topologicalSort(self): 
          
        # Create a vector to store indegrees of all 
        # vertices. Initialize all indegrees as 0. 
        in_degree = [0]*(self.V) 
          
        # Traverse adjacency lists to fill indegrees of 
           # vertices.  This step takes O(V+E) time 
        for i in self.graph: 
            for j in self.graph[i]: 
                in_degree[j] += 1
  
        # Create an queue and enqueue all vertices with 
        # indegree 0 
        queue = [] 
        for i in range(self.V): 
            if in_degree[i] == 0: 
                queue.append(i) 
  
        #Initialize count of visited vertices 
        cnt = 0
  
        # Create a vector to store result (A topological 
        # ordering of the vertices) 
        top_order = [] 
  
        # One by one dequeue vertices from queue and enqueue 
        # adjacents if indegree of adjacent becomes 0 
        while queue: 
  
            # Extract front of queue (or perform dequeue) 
            # and add it to topological order 
            u = queue.pop(0) 
            top_order.append(u) 
  
            # Iterate through all neighbouring nodes 
            # of dequeued node u and decrease their in-degree 
            # by 1 
            for i in self.graph[u]: 
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue 
                if in_degree[i] == 0: 
                    queue.append(i) 
            cnt += 1
  
        # Check if there was a cycle 
        if cnt != self.V: 
            print("There exists a cycle in the graph")
        else : 
            #Print topological order 
            print(top_order)