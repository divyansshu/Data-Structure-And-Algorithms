package graph.questions;

import java.util.ArrayList;

public class Neighbors {

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

    public static void main(String[] args) {
        
        //declare and initialize vertex of graph
        int v = 5;

        ArrayList<Edge>[] graph = new ArrayList[v];

        for(int i = 0; i < v; i++) {
            graph[i] = new ArrayList<>();
        }
        /*
               4  
              /
     0       /
      \     2
       \   / \
        \ /   \
        1 ---- 3

         */

        //0-vertex
        graph[0].add(new Edge(0,1 , 5));

        //1-vertex
        graph[1].add(new Edge(1, 0, 5));
        graph[1].add(new Edge(1, 2, 1));
        graph[1].add(new Edge(1, 3, 3));

        // 2-vertex
        graph[2].add(new Edge(2, 4, 2));
        graph[2].add(new Edge(2, 3, 1));

        // 3-vertex
        graph[3].add(new Edge(3, 1, 3));
        graph[3].add(new Edge(3, 2, 1));

        // 4-vertex
        graph[4].add(new Edge(4, 2, 2));

        //find neighbors of all vertices
        System.out.println("neighbors of all vertices :");
        for(int i = 0; i < v; i++) {
            for(int j = 0; j < graph[i].size(); j++) {
                Edge e = graph[i].get(j); //source, destination, weight
                System.out.println("neighbor of " + i + " is : " + e.dest);
            }
            System.out.println();
        }
    }
    
}
    
