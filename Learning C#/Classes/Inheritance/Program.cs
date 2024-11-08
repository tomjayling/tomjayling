using System;

namespace Inheritance
{
    class Program
    {
        static void Main(string[] args) {
            Book b1 = new Book("War and Peace", "Leo Tolstoy", 825,39.95m);
            Magazine m1 = new Magazine("Time", "Time USA, LLC",75, 4.95m);

            System.Console.WriteLine($"{b1.Name}, {b1.Author}");
            System.Console.WriteLine($"{m1.Name}, {m1.Publisher}");

            //b1.Name = "";
            System.Console.WriteLine(b1.GetDescription());
            System.Console.WriteLine(b1.Price);
            System.Console.WriteLine(m1.GetDescription());
            System.Console.WriteLine(m1.Price);
        }
    }
}
