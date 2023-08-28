import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.*;

/**
 * The Main class implements an application that reads lines from the standard input
 * and prints them to the standard output.
 */
public class Main {
  /**
   * Iterate through each line of input.
   */
  
  public static TreeMap<String, Integer> BFS(HashMap<String, ArrayList<String>> mappings, String a){
    LinkedList<String> queue = new LinkedList<String>();
    HashSet<String> visited = new HashSet<String>();
    TreeMap<String, Integer> distances = new TreeMap<String, Integer>();
    mappings.forEach((key,value) -> distances.put(key, Integer.MAX_VALUE));
    for(ArrayList<String> v: mappings.values()){
      for(String s: v){
        if(!distances.containsKey(s)){
          distances.put(s, Integer.MAX_VALUE);
        }
      }
    }
    distances.put(a, 0);
    queue.add(a);
        
    while(!queue.isEmpty()){
      String n = queue.poll();
      ArrayList<String> neighbors = mappings.getOrDefault(n, new ArrayList<String>());
      for(String neighbor: neighbors){
        if(!distances.containsKey(neighbor)){
          distances.put(neighbor, Integer.MAX_VALUE);
        }
        if(distances.get(n) + 1 < distances.get(neighbor)){
          distances.put(neighbor, distances.get(n) + 1);
          queue.offer(neighbor);
        }
      }
    }
        
    return distances;
  }
  
  
  
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    ArrayList<String> inputs = new ArrayList<String>();
    while ((line = in.readLine()) != null) {
      inputs.add(line);
    }
        
    String[] edges = inputs.get(1).split(";");
    HashMap<String, ArrayList<String>> mapping = new HashMap<String, ArrayList<String>>();
    for(String edge: edges){
      String[] s = edge.split(",");
      ArrayList<String> neighbors = mapping.getOrDefault(s[0], new ArrayList<>());
      neighbors.add(s[1]);
      mapping.put(s[0], neighbors);
    }
    
    String start = inputs.get(0);
    int n = mapping.size();
    
    TreeMap<String, Integer> distances = BFS(mapping, start);
    distances.remove(start);
    
    distances.forEach((key,value) -> System.out.println(key + " " + (value == Integer.MAX_VALUE ? "INF" : value)));
  }
}
