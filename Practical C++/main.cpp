#include <iostream>

using namespace std;

int main()
{
    int value;
    cout << "Enter 1 or 2" << endl;
    cin >> value;
    if(value == 1){
    char letter = 'b';
    int number = 6;
    string word = "Bill";
    double decimal = 4.89;
    cout << "Hello world!" << endl << letter << endl << number << endl << word << endl << decimal << endl << endl;

    int age_2;
    cout << "Enter age 2: ";
    cin >> age_2;

    cout << endl << endl << "You entered: " << age_2<< endl;
    }
    else{
    string first_initial;
    string second_initial;
    cout << "Enter first initial: ";
    cin >> first_initial;
    cout << endl << endl << "Enter second initial: ";
    cin >> second_initial;
    cout << endl << endl << "Your initials are: " << first_initial << second_initial << endl;
    string initials = first_initial + second_initial;
    cout << endl<< endl << "Your initials are: " << initials << endl;
    }
    return 0;

    char grade = 'B';
    switch(grade){
    case 'A':{
        cout << "You made a 90 or above" << endl;
        break;
    }
    case 'B':{
        cout << "You made an 80 or above" << endl;
        break;
    }
    case 'C':{

    }
    }
}
