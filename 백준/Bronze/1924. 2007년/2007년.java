import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException  {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] month = {31,28,31,30,31,30,31,31,30,31,30,31};
		
		String[] days = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
		
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		
		int answer = y;    // answer 변수를 입력날짜로 초기화
		
		for(int i = 0; i< x-1; i++) {
			answer += month[i];
		}
		System.out.println(days[answer%7]);

	}

}