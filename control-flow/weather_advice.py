#declaring the weather variable.
weather = input("What's the weather like today? (sunny/rainy/cold):")

#new line for proper formatting... Also wastage of space...
print()

#declaring cases
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
print()