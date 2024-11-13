"""
Problem Statement
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

E = m * c**2


"""

SPEED_OF_LIGHT = 299792458  # Speed of light in meters per second

def calculate_energy():
    try:
        mass_kg = int(input("Enter the mass in kilograms (kg): "))
        
        if mass_kg < 0:
            print("Mass cannot be negative.")
        else:
            energy_joules = mass_kg * (SPEED_OF_LIGHT ** 2)
            print(f"The equivalent energy for a mass of {mass_kg} kg is: {energy_joules} Joules.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

calculate_energy()
