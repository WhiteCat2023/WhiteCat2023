import java.util.*;
//BERNDT DENNIS FABIAN CANAYA
public class Calculator {
    public static void main(String args[])  {
        
        Scanner sc = new Scanner(System.in);
        
        int positive = 0 , negative = 0, zero = 0;
        
        for (int i = 1; i <= 10; i++) {
            System.out.print("ENTER A NUMBER: ");
            int result = sc.nextInt();
            if (result < 0){
                negative++;}
            else if (result > 0){
                positive++;}
            else if (result == 0 ){
                zero++;}
        }
            System.out.print("\n");
            System.out.print("=======================\n");
            System.out.print("\n");
            System.out.printf("TOTAL POSITIVE: %d \n",  positive);
            System.out.printf("TOTAL NEGATIVE: %d \n",  negative);
            System.out.printf("TOTAL ZEROS: %d \n",  zero);
            System.out.print("\n");
            System.out.print("=======================");
    }
}    
            