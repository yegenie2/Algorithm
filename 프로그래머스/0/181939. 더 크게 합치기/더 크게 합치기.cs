using System;

public class Solution {
    public int solution(int a, int b) {
        string temp_ab = a.ToString() + b.ToString();
        string temp_ba = b.ToString() + a.ToString();
        
        int ab = int.Parse(temp_ab);
        int ba = int.Parse(temp_ba);
        
        if (ab < ba){
            return ba;
        }
        else{
            return ab;
        }

    }
}