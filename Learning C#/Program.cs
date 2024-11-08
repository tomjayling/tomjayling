using System;
using System.Text;

namespace Builder
{
    class Program
    {
        static void Main(string[] args)
        {
            int jumpCount = 10;
            string[] animals = {"goats", "cats", "pigs"};

            StringBuilder sb = new StringBuilder("Initial String.", 200);

            System.Console.WriteLine($"Capacity: {sb.Capacity}; Length: {sb.Length}");

            sb.Append("The quick brown fox ");
            sb.Append("jumps over the lazy dog.");

            sb.AppendLine();

            sb.AppendFormat("He did this {0} times.", jumpCount);
            sb.AppendLine();

            sb.Append("He also jumped over ");
            sb.AppendJoin(',', animals);

            sb.Replace("fox", "cat");

            sb.Insert(0, "This is the ");

            System.Console.WriteLine($"Capacity: {sb.Capacity}; Length: {sb.Length}");
            System.Console.WriteLine(sb.ToString());

        }
    }
}
