using System;

namespace Exceptions
{
    class Program
    {
        static void Main(string[] args){
            int x = 10000;
            int y = 0;
            int result;

            try {
                if (x > 1000){
                    throw new ArgumentOutOfRangeException("x","x has to be 1000 or less");
                }
                result = x/y;
                System.Console.WriteLine("The result is: {0}", result);
            }
            catch (DivideByZeroException e){
                System.Console.WriteLine("Whoops!");
                System.Console.WriteLine(e.Message);
            }
            catch (ArgumentOutOfRangeException e) {
                System.Console.WriteLine("Sorry, 1000 is the limit");
                System.Console.WriteLine(e.Message);
            }
            finally {
                System.Console.WriteLine("This code always runs");
            }
        }
    }
}
