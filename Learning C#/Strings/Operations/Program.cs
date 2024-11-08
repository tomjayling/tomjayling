using System;

namespace Operations
{
    class Program
    {
        static void Main(string[] args)
        {
            string outstr;
            string str1 = "the quick brown fox jumps over the lazy dog.";
            string str2 = "This is a string";
            string str3 = "THIS is a STRING";
            string[] strs = {"one", "two", "three", "four"};

            System.Console.WriteLine(str1.Length);

            System.Console.WriteLine(str1[14]);

            foreach (char c in str1){
                System.Console.Write(c);
                if (c == 'b'){
                    System.Console.WriteLine();
                    break;
                }
            }

            outstr = String.Concat(strs);
            System.Console.WriteLine(outstr);

            outstr = String.Join('.', strs);
            System.Console.WriteLine(outstr);

            outstr = String.Join("---", strs);
            System.Console.WriteLine(outstr);


            int result = String.Compare(str2, "This is a string");
            System.Console.WriteLine(result);

            bool isEqual = str2.Equals(str3);
            System.Console.WriteLine(isEqual);

            System.Console.WriteLine(str1.IndexOf('e'));
            System.Console.WriteLine(str1.IndexOf("fox"));
            System.Console.WriteLine(str1.LastIndexOf('e'));
            System.Console.WriteLine(str1.LastIndexOf("the"));

            outstr = str1.Replace("fox", "cat");
            System.Console.WriteLine(outstr);
            System.Console.WriteLine(outstr.IndexOf("fox"));
        }
    }
}
