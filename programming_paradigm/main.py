import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
# This code is a simple command-line interface for the robust division calculator.
# It takes two command-line arguments (numerator and denominator) and uses the `safe_divide` function to perform the division.
# If the arguments are not provided correctly, it prints a usage message and exits.
# The `safe_divide` function handles division by zero and type errors, returning appropriate error messages.
# The result of the division or an error message is printed to the console.