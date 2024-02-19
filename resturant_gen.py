import random

themes = {
    "Italian": ["Mamma Mia", "La Cucina", "Trattoria", "Il Gusto", "Nonna's"],
    "Mexican": ["Fiesta Cantina", "El Sombrero", "Taco Fiesta", "Burrito Loco", "Viva Mexico"],
    "Chinese": ["Dragon Palace", "Jade Garden", "Golden Wok", "Lucky Panda", "Panda Express"],
    "Pizza": ["Slice of Heaven", "Pizza Paradise", "The Cheesy Crust", "Pie in the Sky", "Doughlicious"],
    "Burger": ["Burger Bar", "Patty Palace", "Flame Broiled Burgers", "The Burger Shack", "Burgerlicious"]
}
theme_list = ["Italian", "Mexican", "Chinese", "Pizza", "Burger"]
themes = [["Mamma Mia", "La Cucina", "Trattoria", "Il Gusto", "Nonna's"],
          ["Fiesta Cantina", "El Sombrero", "Taco Fiesta", "Burrito Loco", "Viva Mexico"],
          ["Dragon Palace", "Jade Garden", "Golden Wok", "Lucky Panda", "Panda Express"],
          ["Slice of Heaven", "Pizza Paradise", "The Cheesy Crust", "Pie in the Sky", "Doughlicious"],
          ["Burger Bar", "Patty Palace", "Flame Broiled Burgers", "The Burger Shack", "Burgerlicious"]]

adjectives = ["Delicious", "Authentic", "Cozy", "Friendly", "Trendy", "Casual", "Fast-casual", "Fine-dining"]

def generate_restaurant_name(theme):
    """
    Generates a random restaurant name based on a theme.
    Args:
    theme: The theme of the restaurant (e.g., "Italian", "Mexican").
    Returns:
    A randomly generated restaurant name.
    """
    name_part1 = ""
    name_part2 = ""
    theme_input = ""
    if theme in theme_list:
        index = theme_list.index(theme)
        name_part1 = random.choice(themes[index])
    else:
        while theme_input not in theme_list:
            print("Theme doesn't exist")
            print(theme_list)
            theme_input = input("Input a theme: ")
        index = theme_list.index(theme_input)
        name_part1 = random.choice(themes[index])
    name_part2 = " ".join(random.sample(adjectives, 1))
    
    return name_part1 + " " + name_part2

# Example usage
print(theme_list)
uin = input("Input a theme: ")
restaurant_name = generate_restaurant_name(uin)
print(restaurant_name)  # Output: Slice of Heaven Delicious Pizza
