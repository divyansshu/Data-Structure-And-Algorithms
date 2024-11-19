package graph.traversals.BFS;

import java.util.*;

class BFS_Traversal {
    // Class to represent an edge in a weighted undirected graph
    static class Edge {
        int src;
        int dest;
        int weight;

        public Edge(int s, int d, int w) {
            this.src = s;
            this.dest = d;
            this.weight = w;
        }
    }

    // Method to perform BFS traversal on the graph
    public static void BFS(ArrayList<Edge> graph[]) {
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[graph.length];

        q.add(0); // Start BFS from node 0

        while (!q.isEmpty()) {
            int curr = q.remove();

            if (!visited[curr]) {
                visited[curr] = true;
                System.out.print(curr + " ");

                // Add all adjacent nodes to the queue
                for (int i = 0; i < graph[curr].size(); i++) {
                    Edge e = graph[curr].get(i);
                    q.add(e.dest);
                }
            }
        }
    }

    // Method to create a graph with edges
    public static void createGraph(ArrayList<Edge> graph[]) {
        // 0-vertex
        graph[0].add(new Edge(0, 1, 5));
        graph[0].add(new Edge(0, 2, 1));

        // 1-vertex
        graph[1].add(new Edge(1, 0, 1));
        graph[1].add(new Edge(1, 3, 1));

        // 2-vertex
        graph[2].add(new Edge(2, 0, 1));
        graph[2].add(new Edge(2, 4, 1));

        // 3-vertex
        graph[3].add(new Edge(3, 1, 1));
        graph[3].add(new Edge(3, 4, 1));
        graph[3].add(new Edge(3, 5, 1));

        // 4-vertex
        graph[4].add(new Edge(4, 2, 1));
        graph[4].add(new Edge(4, 3, 1));
        graph[4].add(new Edge(4, 5, 1));

        // 5-vertex
        graph[5].add(new Edge(5, 3, 1));
        graph[5].add(new Edge(5, 4, 1));
        graph[5].add(new Edge(5, 6, 1));

        // 6-vertex
        graph[6].add(new Edge(6, 5, 1));
    }

    public static void main(String[] args) {
        // Number of vertices in the graph
        int v = 7;

        // Initialize the graph with empty adjacency lists
        ArrayList<Edge>[] graph = new ArrayList[v];
        for (int i = 0; i < v; i++) {
            graph[i] = new ArrayList<>();
        }

        // Create the graph with edges
        createGraph(graph);

        // Perform BFS traversal
        System.out.println("Breadth First Traversal of Graph: ");
        BFS(graph);
    }
}
