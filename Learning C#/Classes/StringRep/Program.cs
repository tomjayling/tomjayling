using System;

namespace StringRep
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 1000;
            System.Console.WriteLine(x.ToString());

            object a = new object();
            System.Console.WriteLine(a.ToString());

            Book b1 = new Book("War and Peace", "Leo Tolstoy", 825);
            System.Console.WriteLine(b1.ToString());
            System.Console.WriteLine(b1);

            System.Console.WriteLine(b1.ToString('B'));
            System.Console.WriteLine(b1.ToString('F'));
        }
    }
}
