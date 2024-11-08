// This is how your code will be called.
// You can edit this code to try different testing cases.
bool IsSuccessful = true;
// Create the Checking Account with initial balance.
CheckingAcct checking = new CheckingAcct("John", "Doe", 2500.0m);
IsSuccessful &= (checking.Balance == 2500.0m);
IsSuccessful &= (checking.AccountOwner == "John Doe");

// Create the Savings Account with interest and initial balance.
SavingsAcct saving = new SavingsAcct("Jane", "Doe", 0.03m, 1000.0m);
IsSuccessful &= (saving.Balance == 1000.0m);
IsSuccessful &= (saving.AccountOwner == "Jane Doe");

// Deposit some money in each account.
checking.Deposit(200.0m);
saving.Deposit(150.0m);
IsSuccessful &= (checking.Balance == 2700.0m);
IsSuccessful &= (saving.Balance == 1150.0m);

// Make some withdrawals from each account.
checking.Withdraw(50.0m);
saving.Withdraw(125.0m);
IsSuccessful &= (checking.Balance == 2650.0m);
IsSuccessful &= (saving.Balance == 1025.0m);

// Apply the Savings interest.
saving.ApplyInterest();
IsSuccessful &= (saving.Balance == 1055.75m);

// More than three Savings withdrawals should result in $2 charge.
saving.Withdraw(10.0m);
saving.Withdraw(20.0m);
saving.Withdraw(30.0m);
IsSuccessful &= (saving.Balance == 993.75m);

// try to overdraw savings - this should be denied
saving.Withdraw(2000.0m);
// try to overdraw checking - should be allowed and result in extra charge
checking.Withdraw(3000.0m);
IsSuccessful &= (saving.Balance == 993.75m);
IsSuccessful &= (checking.Balance == -385.00m);
if (IsSuccessful) {
    System.Console.WriteLine("Correct");
}
else {
    System.Console.WriteLine("Incorrect");
}