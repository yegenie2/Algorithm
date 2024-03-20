import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		String a = scanner.nextLine();
		
		for( int i=0; i<a.length(); i++) {
			System.out.print(a.charAt(i));
			
			if ((i+1) % 10 == 0) {
				System.out.println();
			}
		}
	}
}