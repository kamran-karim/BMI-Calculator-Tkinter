def calculate_bmi(weight_kg, height_m):
    # Calculate Body Mass Index (BMI)
    bmi = weight_kg / (height_m ** 2)
    return bmi

def moon_weight(earth_weight_kg):
    # On the Moon, gravity is ~16.5% of Earth's
    moon_weight = earth_weight_kg * 0.165
    return moon_weight

try:
    # Input from user
    weight_kg = float(input("Enter your weight on Earth (kg): "))
    height_m = float(input("Enter your height (m): "))

    # Input validation
    if weight_kg <= 0 or height_m <= 0:
        print(" Error: Weight and height must be positive numbers.")
    else:
        # Calculations
        bmi = calculate_bmi(weight_kg, height_m)
        moon_wt = moon_weight(weight_kg)

        # Output
        print("\n--- Results ---")
        print(f" Your BMI is: {bmi:.2f}")
        print(f" Your weight on the Moon would be: {moon_wt:.2f} kgf (kilogram-force)")

except ValueError:
    print(" Invalid input! Please enter numeric values only.")
