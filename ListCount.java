import java.util.ArrayList;
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.*;

public class ListCount{

  public  HashMap<String, LinkedList<Node>> dataMap = new HashMap<String, LinkedList<Node>>();
  public  Map<String, Integer> maxMap = new HashMap<String,Integer>();
  public  HashSet<String> stopSet = new HashSet<String>();

  public static void main(String args[]){

    try
   {
       ListCount obj = new ListCount ();
       obj.run(args);
   }
   catch (Exception e)
   {
       e.printStackTrace ();
   }

  }

  public void run(String args[]){

    try{

      File stopFile= new File("stopwords.txt");
      Scanner stopScan = new Scanner(stopFile);
      while(stopScan.hasNextLine()){
        String word = stopScan.nextLine();
        word= word.toUpperCase().replace("\n", "");
        stopSet.add(word);
      }
    }catch(Exception e){
      System.out.println(e);
    }

    System.out.println(stopSet.size());

    try {
      File myObj = new File("ShakeOut");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        data = data.replace("\n", "");
        String[] elements = data.split("[ :\t\n]", 0);
        String key = elements[0];
        if(stopSet.contains(key)) {continue;}
        int sum = 0;
        LinkedList<Node> nodeList = new LinkedList<Node>();
        for(int i = 1; i < (elements.length+1)/2; i++){
          Node n = new Node(elements[2*i-1], Integer.parseInt(elements[2*i]));
          nodeList.add(n);
          sum+= Integer.parseInt(elements[2*i]);
        }
        dataMap.put(key,nodeList);
        maxMap.put(key,sum);
        String output = key + ":";
        for(Node node: nodeList){
          output = output + node.toString();
        }
        //System.out.println(output);
      }
      List<Map.Entry<String, Integer>> maxList = new ArrayList<>(maxMap.entrySet());

      maxList.sort(Map.Entry.<String, Integer>comparingByValue().reversed());

      for (int i = 0; i < 100 ; i++) {
        System.out.println(maxList.get(i).getKey() + "\t" + maxList.get(i).getValue());
      }



      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }

  public class Node{
    String title;
    int occurence;
    public Node(String tit, int occ){
      this.title = tit;
      this.occurence = occ;
    }
    public String toString(){
      return title + ":" + occurence+ "\t";
    }
  }
}
