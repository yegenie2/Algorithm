import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int t = scanner.nextInt();
		
		for (int i=0; i<t; i++) {
			String num = scanner.next();
			
			String[] arr = num.split(",");
			
			int a = Integer.parseInt(arr[0]);
			int b = Integer.parseInt(arr[1]);
			
			System.out.println(a+b);
		}
		
	}
}
