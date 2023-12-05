import java.util.*;
//BERNDT DENNIS FABIAN CANAYA BSIT-A1
public class loan_calculator {
    public static void main(String args[])  {
  
        Scanner sc = new Scanner(System.in);
          
        System.out.print("ENTER YOUR LOAN AMOUNT: ");
        int principal_amount = sc.nextInt();
        
        if (principal_amount < 1000 || principal_amount > 100000)
            System.out.print("Invalid Amount");
        else {
            
            System.out.print("INTEREST RATE PER MONTH: ");
            float interest_rate_per_month = sc.nextFloat();
            
            if(interest_rate_per_month < 1 || interest_rate_per_month > 20)
                System.out.print("Invalid Amount");
                
            else{
                System.out.print("LOAN TERMS: ");
                int loan_terms = sc.nextInt();
                if (loan_terms == 12 || loan_terms == 18 || loan_terms == 24 || loan_terms ==30 || loan_terms == 36){
                    
                    int i = (int)interest_rate_per_month;
                    
                    float q = interest_rate_per_month / 100;
                    float interest_amount_per_month = principal_amount * q;
                    float total_interest_amount = interest_amount_per_month * loan_terms;
                    float total_loan_amount = principal_amount + total_interest_amount;
                    float payment_per_month = total_loan_amount / loan_terms;
                    
                    System.out.print("=============================================\n");
                    System.out.print("\n");
                    System.out.print("===========😎 LOAN CALCULATOR 😎=============\n");
                    System.out.print("\n");
                    System.out.printf("PRINCIPAL AMOUNT: %d \n", principal_amount);
                    System.out.printf("INTEREST RATE PER MONTH: %d \n", i);
                    System.out.printf("INTEREST AMOUNT PER MONTH: %f \n",interest_amount_per_month, 2);
                    System.out.printf("LOAN TERMS: %d \n", loan_terms);
                    System.out.printf("TOTAL INTEREST AMOUNT: %f \n", total_interest_amount, 2);
                    System.out.printf("TOTAL LOAN AMOUNT: %f \n", total_loan_amount, 2);
                    System.out.printf("PAYMENT PER MONTH: %f \n", payment_per_month, 2);
                    System.out.print("\n");
                    System.out.print("=============================================\n");
                    
                    }
                else{
                    System.out.print("INVALID NUMBER");
                }
                }
            }
        }
    }
