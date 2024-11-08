using System;

namespace Modifiers
{
    class Program
    {
        static void Main(string[] args)
        {
            Book b1 = new Book("War and Peace", "Leo Tolstoy", 825);

            // b1._name = "Aldous Huxley";

            // System.Console.WriteLine(b1.GetDescription());

            b1.SetName("Grapes of Wrath");
            b1.SetAuthor("John Steinbeck");
            b1.SetPages(464);
            System.Console.WriteLine(b1.GetDescription());
           
        }
    }
}