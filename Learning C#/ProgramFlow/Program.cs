using System;

namespace Conditionals
{
    class Program
    {
        static void Main(string[] args)
        {
            int theVal = 51;

            // if (theVal == 50){
            //     System.Console.WriteLine("theVal is 50");
            // }
            // else if (theVal >= 51 && theVal <= 60){
            //     System.Console.WriteLine("theVal is between 51 and 60");
            // }
            // else {
            //     System.Console.WriteLine("theVal is something else");
            // }

            System.Console.WriteLine(theVal < 50 ? "theVal is small" : "theVal is large");
        }
    }
}