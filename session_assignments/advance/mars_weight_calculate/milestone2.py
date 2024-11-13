# Milestone:2

planets_constant: dict = {
    "mars": 0.378,
    "mercury": 0.376,
    "venus": 0.889,
    "jupiter": 2.360,
    "saturn": 1.081,
    "uranus": 0.815,
    "neptune": 1.140,
}

def calculate_planets_weight(earth_weight, planet):
    planet = planet.lower()
    while True:
      if planet in planets_constant:
          weight_on_planet = earth_weight * planets_constant[planet]
          return f"Your weight on {planet.capitalize()} is {weight_on_planet:.2f}"
          break
      else:
          return "Invalid planet name. Please enter a valid planet name."

def error_handle():
    while True:
      try:
        earth_weight: float = float(input("Enter your weight on Earth: "))
        break
      except ValueError:
        print("Invalid input. Please enter a valid number.")

    planet = input("Enter the name of the planet: ")
    user_weight = calculate_planets_weight(earth_weight, planet)
    print(user_weight)

error_handle()
