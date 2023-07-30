import java.util.Scanner;
import java.io.IOException;


public class BC1067 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int entrada = input.nextInt();

        for (int contador = 0 ; contador <= entrada;contador++) {
            if (contador % 2 != 0){
                System.out.println(contador);
            }
        }

    }
}
