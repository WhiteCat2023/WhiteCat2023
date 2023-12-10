import java.util.*;
//BERNDT DENNIS FABIAN CANAYA BSIT-A1
public class Multiplication {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("START: ");
        int start = sc.nextInt();
        System.out.print("END: ");
        int end = sc.nextInt();
        System.out.print("\t");
        
        for (int i = start; i <= end; i++){
            System.out.print(i + "\t");
        }
        System.out.println(" ");
        
        for (int i = start; i <= end; i++){
            System.out.print(i + "\t");
            for (int j = start; j <= end; j++){
            System.out.print(i * j + "\t");
            }
            System.out.println();
        }
    }
}