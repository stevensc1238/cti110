#Cole Stevenson
#04/05/2025
#P1HW2
#create a program that does some basic math on numbers that are entered

# Pseudocode:
# 1. Ask the user to enter their budget.
# 2. Ask the user to enter their travel destination.
# 3. Ask the user for the amount they will spend on gas.
# 4. Ask the user for the amount they will spend on accommodation/hotel.
# 5. Ask the user for the amount they will spend on food.
# 6. Add the expenses (gas, accommodation, food).
# 7. Subtract the expenses from the budget to calculate the remaining balance.
# 8. Display the results, including travel destination, initial budget, individual expenses, and remaining balance.

# Main Program
def main():
    print("-----Travel Budget Calculator-----\n")
    
    # Ask user for budget
    budget = float(input("Enter your budget: "))
    
    # Ask user for travel destination
    destination = input("Enter your travel destination: ")
    
    # Ask for expenses
    gas = float(input("How much do you think you will spend on gas? "))
    accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
    food = float(input("Last, how much do you need for food? "))
    
    # Calculate total expenses
    total_expenses = gas + accommodation + food
    
    # Calculate remaining balance
    remaining_balance = budget - total_expenses
    
    # Display results
    print("\n------------Travel Expenses------------\n")
    print(f"Location: {destination}")
    print(f"Initial Budget: ${budget:.2f}\n")
    print(f"Fuel: ${gas:.2f}")
    print(f"Accommodation: ${accommodation:.2f}")
    print(f"Food: ${food:.2f}\n")
    print(f"Remaining Balance: ${remaining_balance:.2f}")

# Run the main program
main()
