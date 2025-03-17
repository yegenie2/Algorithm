using System;

public class Example
{
    public static void Main()
    {
        Console.Clear();
        int n = Int32.Parse(Console.ReadLine());
        
        for (int i = 0; i<n; i++){
            for ( int j = 0; j<=i; j++){
                Console.Write("*");
            }
            Console.WriteLine();
        } 
    }
}