using System;

float MilesToKm(float miles){
    float result = miles * 1.6f;
    return result;
}

void PrintWithPrefix(string theStr) {
    System.Console.WriteLine($"::> {theStr}");
}


System.Console.WriteLine($"The result is {MilesToKm(8.0f)}");
System.Console.WriteLine($"The result is {MilesToKm(52.0f)}");

PrintWithPrefix("Test String");
PrintWithPrefix("Another Test String");
