import java.io.IOException;
import java.util.Scanner;


public class BC1008 {
    public static void main(String[] args) throws IOException {

        Scanner input = new Scanner(System.in);

        int numero = input.nextInt();
        int horas = input.nextInt();
        double valor = input.nextDouble();
        double salario = valor * horas;

        System.out.println("NUMBER = " + numero);
        System.out.printf("SALARY = U$ %.2f%n", salario);

    }
}