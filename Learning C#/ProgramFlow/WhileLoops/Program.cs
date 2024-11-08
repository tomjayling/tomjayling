using System;
using System.Runtime.ConstrainedExecution;

namespace WhileLoops
{
    class Program
    {
        static void Main(string[] args)
        {
            string inputStr = "";

            // System.Console.WriteLine("Basic while() loop:");
            // while (inputStr != "exit") {
            //     inputStr = Console.ReadLine();
            //     System.Console.WriteLine("You entered: {0}", inputStr);
            // }

            System.Console.WriteLine("The do-while() loop:");
            do {
                inputStr = Console.ReadLine();
                System.Console.WriteLine("You entered: {0}", inputStr);
            } while (inputStr != "exit");
        }
    }
}
