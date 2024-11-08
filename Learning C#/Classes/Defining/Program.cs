using System;

namespace Defining
{
    class Program
    {
        static void Main(string[] args)
        {
            Book b1 = new Book("War and Peace", "Leo Tolstoy", 825);
            Book b2 = new Book("The Grapes of Wrath", "John Steinbeck", 465);

            System.Console.WriteLine(b1.GetDescription());
            System.Console.WriteLine(b2.GetDescription());

            //b1._name = "Aldous Huxley"; ---This line does not work
        }
    }
}
