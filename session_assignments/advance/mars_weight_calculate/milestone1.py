# Mlestone:1

Mars_constant:float=0.378

def calculate_mars_weight():
   user_weight:float=float(input("Enter your weight on earth: "))
   user_weight_on_mars=user_weight*Mars_constant
   return user_weight_on_mars

weight=calculate_mars_weight()
print(f"Your weight on mars is {weight:.2f}")

