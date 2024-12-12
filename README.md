# Credit Card Validator

This program validates credit card numbers using the **Luhn Algorithm**. It determines whether a given credit card number is valid or invalid based on its checksum.

## How It Works
The program:
1. Doubles every second digit from the right. If doubling results in a two-digit number, the digits are summed to form a single-digit number.
2. Adds all these single-digit results to the sum of the remaining digits (not doubled).
3. Checks if the final sum is a multiple of 10. If it is, the credit card number is valid.

## Features
- Handles invalid input gracefully by checking if the entered string is numeric.
- Allows users to exit the program by typing `exit`.
- Provides real-time validation feedback for entered credit card numbers.

## Sample Run
```plaintext
This program uses the Luhn Algorithm to validate a CC number.
You can enter 'exit' anytime to quit.
Please enter a CC number to validate: 4532015112830366
Valid!
Please enter a CC number to validate: 1234567890123456
Invalid!
Please enter a CC number to validate: exit
```
## How to Compile and Run
Compile:
```bash
g++ creditcard.cpp -o a
```
Run: 
```bash
./a
```
## Algorithm Reference
The Luhn Algorithm, also known as the "modulus 10" algorithm, is commonly used for validating credit card numbers.
## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.
