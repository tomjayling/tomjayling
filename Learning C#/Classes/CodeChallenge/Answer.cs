// C# code​​​​​​‌‌​​​​​‌‌​​​​​‌​​‌​​‌‌​‌‌ below
using System;

// Write your answer here, and then test your code.
// Your job is to implement the findLargest() method.

public class Answer {

    // Change these Boolean values to control whether you see 
    // the expected result and/or hints.
   public  static Boolean ShowExpectedResult = true;
   public  static Boolean ShowHints = true;

}

public class BankAccount {
    public BankAccount(string firstname, string lastname, decimal startingbalance = 0.0m){
        AccountOwner = $"{firstname} {lastname}";
        Balance = startingbalance;
    }

    public string AccountOwner{
        get;
    }

    public decimal Balance {
        get; set;
    }

    public virtual void Deposit(decimal amount) {
        Balance += amount;
    }

    public virtual void Withdraw(decimal amount) {
        Balance -= amount;
    }
}

public class CheckingAcct : BankAccount {

    private const decimal OVERDRAW_CHARGE = 35;
    public CheckingAcct(string firstname, string lastname, decimal startingbalance = 0.0m): base(firstname, lastname, startingbalance) {

    }

    public override void Withdraw(decimal amount)
        {
            if (amount > Balance){
                amount += OVERDRAW_CHARGE;
            }
            
            base.Withdraw(amount);
        }
}

public class SavingsAcct : BankAccount {

    private int _withdrawcount = 0;
    private const decimal WITHDRAW_CHARGE = 2;
    private const int WITHDRAW_LIMIT = 3;

    public SavingsAcct(string firstname, string lastname, decimal interest, decimal startingbalance) : base(firstname, lastname, startingbalance) {
        InterestRate = interest;
    }

    public decimal InterestRate {
        get;set;
    }

    public void ApplyInterest() {
        base.Deposit(Balance * InterestRate);
    }

    public override void Withdraw(decimal amount)
        {
            if (amount > Balance){
                System.Console.WriteLine("Attempt to withdraw savings - denied");
            }
            else {
                base.Withdraw(amount);
                _withdrawcount ++;
                if (_withdrawcount > WITHDRAW_LIMIT){
                System.Console.WriteLine($"More than {WITHDRAW_LIMIT} withdrawals - extra charge of {WITHDRAW_CHARGE}");
                base.Withdraw(WITHDRAW_CHARGE);
                _withdrawcount = 0;
            }
            }
            
        }
}
