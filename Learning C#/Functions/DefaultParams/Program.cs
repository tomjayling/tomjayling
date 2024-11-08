using System;

void PrintWithPrefix(string thestr, string prefix = "") {
    System.Console.WriteLine($"{prefix} {thestr}");
}

PrintWithPrefix("Hello There!");
PrintWithPrefix("Hello There!", ">:");

PrintWithPrefix(prefix: "% ", thestr: "Hello There!");

