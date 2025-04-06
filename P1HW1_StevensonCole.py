# Function to calculate exponentiation
def calculate_exponent(base, exponent):
    return base ** exponent

# Function to perform addition and subtraction
def add_and_subtract(start, add, subtract):
    return start + add - subtract

# Main program
def main():
    print("-----Calculating Exponents----\n")
    
    base = int(input("Enter an integer as the base value: "))
    exponent = int(input("Enter an integer as the exponent: "))
    
    result = calculate_exponent(base, exponent)
    print(f"\n{base} raised to the power of {exponent} is {result} !!")
    
    print("\n-----Addition and Subtraction----\n")
    
    start = int(input("Enter a starting integer: "))
    add = int(input("Enter an integer to add: "))
    subtract = int(input("Enter an integer to subtract: "))
    
    final_result = add_and_subtract(start, add, subtract)
    print(f"\n{start} + {add} - {subtract} is equal to {final_result}")

# Run the main program
main()
