def calculate_calories(carbs, fats, proteins):
    """
    Calculate total calories based on grams of carbs, fats, and proteins.
    1g carbs = 4 calories
    1g fats = 9 calories
    1g proteins = 4 calories
    """
    total = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total

print("Daily Caloric Intake Calculator")
print("-" * 30)

try:
    carbs_grams = float(input("Enter grams of carbohydrates consumed: "))
    fats_grams = float(input("Enter grams of fats consumed: "))
    proteins_grams = float(input("Enter grams of proteins consumed: "))
    
    total_calories = calculate_calories(carbs_grams, fats_grams, proteins_grams)
    
    print("-" * 30)
    print(f"Total Daily Caloric Intake: {total_calories} calories")
    
except ValueError:
    print("Invalid input. Please enter numeric values for grams.")