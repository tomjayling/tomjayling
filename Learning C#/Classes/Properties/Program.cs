using System;

namespace Properties
{
    class Program
    {
        static void Main(string[] args)
        {
            Book b1 = new Book("War and Peace", "Leo Tolstoy", 825);

            System.Console.WriteLine(b1.Name);
            System.Console.WriteLine(b1.Description);

            b1.ISBN = "100140447938";
            b1.Price = 24.95m;
            System.Console.WriteLine(b1.ISBN);
            System.Console.WriteLine(b1.Price);

            b1.Name = "Crime and Punishment";
            b1.Pagecount = 652;
            System.Console.WriteLine(b1.Description);
            System.Console.WriteLine(b1.Name);
            System.Console.WriteLine(b1.Pagecount);
        }
    }
}
