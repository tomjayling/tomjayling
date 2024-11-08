// C# code​​​​​​‌‌​​​​​‌​​‌‌​​​‌‌‌​​​‌​‌‌ below
using System;
using System.Text;

// Write your answer here, and then test your code.

public class Answer {

    // Change these Boolean values to control whether you see 
    // the expected result and/or hints.
   public  static Boolean ShowExpectedResult = false;
   public  static Boolean ShowHints = false;

    // Determine whether a string is a Palindrome
    public static bool IsPalindrome(string thestr) {
        // Your code goes here.
        string testStr = thestr.ToUpper();
        StringBuilder sb = new StringBuilder();
        foreach (char c in testStr){
            
            if (Char.IsPunctuation(c) || Char.IsWhiteSpace(c)){
                continue;
            }
            sb.Append(c);
        }
        char[] chars = sb.ToString().ToCharArray();
        Array.Reverse(chars);
        string reversedString = new string(chars);
        if (sb.ToString() == reversedString){
            return true;
        }

        return false;
    }
}
