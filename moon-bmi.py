def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def moon_weight(earth_weight_kg):
    # On the Moon, gravity is ~1/6 of Earth's
    moon_weight = earth_weight_kg * 0.1676
    return moon_weight

# Input from user
weight_kg = float(input("Enter your weight on Earth (kg): "))
height_m = float(input("Enter your height (m): "))

# Calculations
bmi = calculate_bmi(weight_kg, height_m)
moon_wt = moon_weight(weight_kg)

# Output
print("\n--- Results ---")
print(f"Your BMI is: {bmi:.3f}")
print(f"Your weight on the Moon would be: {moon_wt:.2f} kgf (kilogram-force)")
