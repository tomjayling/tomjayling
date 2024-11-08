// This is how your code will be called.
// You can edit this code to try different testing cases.
string[] teststrings = { "Hello World!", "Race car!", "Rotor", "More cowbell!", "Madam, I'm Adam." };
int palcount = 0;
foreach (string str in teststrings) {
	bool learnerResult = Answer.IsPalindrome(str);
	if (learnerResult)
		palcount++;
}
if (palcount == 3){
    System.Console.WriteLine("Correct");
}
else {
    System.Console.WriteLine("Incorrect");
}
