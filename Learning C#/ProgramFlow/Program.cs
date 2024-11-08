using System;

namespace ConditionalOps
{
    class Program
    {
        static void Main(string[] args)
        {
            int theVal = 60;

            switch (theVal){
                case 50:
                    System.Console.WriteLine("theVal is 50");
                    break;
                case 51:
                    System.Console.WriteLine("theVal is 51");
                    break;
                case 52:
                case 53:
                case 54:
                    System.Console.WriteLine("theVal is between 52 and 54");
                    break;
                default:
                    System.Console.WriteLine("theVal is something else");
                    break;
            }
        }
    }
}
