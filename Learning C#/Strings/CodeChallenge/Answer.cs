// C# code​​​​​​‌‌​​​​​‌​​‌‌​​​​​‌‌​​​​​‌ below
using System;

// Write your answer here, and then test your code.
// Your job is to implement the findLargest() method.

public class Answer {
    // Change these Boolean values to control whether you see 
    // the expected result and/or hints.
    public  static Boolean ShowExpectedResult = false;
    public  static Boolean ShowHints = false;

    public static bool CountTheType(object Arg, string TypeToCount) {
        // Your code goes here. Return true if the type of the Arg is the same
        // as what the TypeToCount parameter says to count.
        string type = Arg.GetType().ToString();
        if (type == TypeToCount) {
            return true;
        }
        return false;
    }
}
