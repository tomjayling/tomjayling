using System;
using System.Runtime.ConstrainedExecution;
using System.Security.Cryptography.X509Certificates;

namespace Operators
{
    class Program
    {
        /// <summary>
        /// this is the main sample application function
        /// </summary>
        /// <param name="args"> An array of string arguments from the command line</param>
        /// <returns> No return value </returns>
        static void Main(string[] args)
        {
            int x=10, y=5;
            // string a="abcd", b="efgh";

            // // System.Console.WriteLine("----- Basic Math -----");
            // // System.Console.WriteLine((x/y)*x);
            // // System.Console.WriteLine(a + b);

            // System.Console.WriteLine("----- Shorthand -----");
            x++;
            y--;
            // System.Console.WriteLine(x);
            // System.Console.WriteLine(y);

            // a += b;
            // System.Console.WriteLine(a);

            // System.Console.WriteLine(x > y && y >= 5);
            // System.Console.WriteLine(x > y || y >= 5);

            string str = "hello";
            System.Console.WriteLine(str ?? "Unkown string"); //outputs Unknown string if str is null, otherwise outputs str

            str ??= "New String"; //assings a value to str only if it is currently null
            System.Console.WriteLine(str);
        }
    }
}

/* multi line comment
fsbs
dsonfosna
ndsofnoa
*/
