// This is how your code will be called.
// You can edit this code to try different testing cases.
object[] items = {1, 2, "Hello!", "World", 'X', true, 2.0, ".NET", 'A'};
int total = 0;
string CountType = "System.String";
foreach (object item in items) {
    if (Answer.CountTheType(item, CountType)) {
		total++;
	}
}
if (total == 3){
    System.Console.WriteLine("Correct");
}
else {
    System.Console.WriteLine("Incorrect");
}
