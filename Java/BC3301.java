import java.io.IOException;
import java.util.Scanner;

public class BC3301 {
    public static void main(String[] args) throws IOException {


        Scanner input = new Scanner(System.in);

        int resultado0 = input.nextInt();
        int resultado1 = input.nextInt();
        int resultado2 = input.nextInt();

        if (resultado0 > resultado1 && resultado0 < resultado2 ){
            System.out.println("huguinho");
        }
        if (resultado0 > resultado2 && resultado0 < resultado1 ){
            System.out.println("huguinho");
        }
        if (resultado1 > resultado0 && resultado1 < resultado2 ){
            System.out.println("zezinho");
        }
        if (resultado1 > resultado2 && resultado1 < resultado0 ){
            System.out.println("zezinho");
        }
        if (resultado2 > resultado1 && resultado2 < resultado0 ){
            System.out.println("luisinho");
        }
        if (resultado2 > resultado0 && resultado2 < resultado1 ){
            System.out.println("luisinho");
        }
    }
}
    }
            }