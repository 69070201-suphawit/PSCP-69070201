allowed = [
    "Pad Thai Sauce",
    "Tofu",
    "Pickle Turnip",
    "Shrimp",
    "Bean Sprouts",
    "Noodle",
    "Chives",
    "Lime",
    "Egg",
    "Oil",
    "Peanuts",
]
required = ["Sweet", "Sour", "Salty"]
ingredients = []
line = input().strip()
while line != "Cook":
    ingredients.append(line)
    line = input().strip()
tastes = []
line = input().strip()
while line != "End":
    tastes.append(line)
    line = input().strip()
if any(item not in allowed for item in ingredients):
    print("This is not Pad Thai!!!")
elif set(ingredients) != set(allowed):
    print("This is bad!")
elif set(tastes) != set(required):
    print("Not Bad...")
else:
    print("Delicious!")
