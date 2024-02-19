import random
theme_list = ["Italian", "Mexican", "Chinese", "Pizza", "Burger"]
themes = [["Mamma Mia", "La Cucina", "Trattoria", "Il Gusto", "Nonna's"],
          ["Fiesta Cantina", "El Sombrero", "Taco Fiesta", "Burrito Loco", "Viva Mexico"],
          ["Dragon Palace", "Jade Garden", "Golden Wok", "Lucky Panda", "Panda Express"],
          ["Slice of Heaven", "Pizza Paradise", "The Cheesy Crust", "Pie in the Sky", "Doughlicious"],
          ["Burger Bar", "Patty Palace", "Flame Broiled Burgers", "The Burger Shack", "Burgerlicious"]]
menu = [["Spaghetti Carbonara", "Penne Arrabbiata", "Lasagna al Ragu", "Tiramisu", "Gelato"],
        ["Tacos al Pastor", "Mole Poblano", "Pozole Rojo", "Enchiladas Suizas", "Sopa Azteca"],
        ["Kung Pao Chicken", "Mapo Tofu", "Dumplings", "Beef and Broccoli", "Sweet and Sour Pork"],
        ["Pepperoni", "Mushrooms", "Sausage", "Onions", "Olives"],
        ["Cheeseburger", "Bacon Cheeseburger", "Black Bean Burger", "Turkey Burger", "Mushroom Swiss Burger"]]
adjectives = ["Delicious", "Authentic", "Cozy", "Friendly", "Trendy", "Casual", "Fast-casual", "Fine-dining"]

theme = ""
one_star = ["Bland", "Greasy", "Inattentive", "Overpriced", "Dull"]
two_star = ["Mediocre", "Average", "Basic", "Unremarkable", "Passable"]
three_star = ["Decent", "Average", "Satisfactory", "Familiar", "Reliable"]
four_star = ["Good", "Above Average", "Pleasurable", "Recommended", "Memorable"]
five_star = ["Excellent", "Outstanding", "Exquisite", "Unforgettable", "Top-Notch"]

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

def generate_restaurant_menu(theme):
    """
    Generates a random restaurant menu based on a theme.
    Args:
    theme: The theme of the restaurant (e.g., "Italian", "Mexican").
    Returns:
    A randomly generated restaurant menu.
    """
    name_part1 = ""
    name_part2 = ""
    rand_menu = []
    while theme not in theme_list:
        print("Theme doesn't exist")
        print(theme)
        theme = input("Input a theme: ")
    index = theme_list.index(theme)
    for i in range(3):
        choice = random.choice(menu[index])
        rand_menu.append(choice)
        menu[index].remove(choice)
    return rand_menu
    
    return name_part1 + " " + name_part2

def generate_restaurant_review(rating, restaurant_name, theme):
    """
    Generates a random restaurant review based on a rating.
    Args:
    theme: The theme of the restaurant (e.g., "Italian", "Mexican").
    Returns:
    A randomly generated restaurant review.
    """
    rating_part1 = ""
    rating_part2 = ""
    reivew =""
    while rating not in range(1,5):
        print("Rating is not 1-5")
        rating = input("Input a rating: ")








    if(rating == 1):
        choice = random.choice(one_star)
        rating_part1 = choice
        one_star.remove(choice)
        choice = random.choice(one_star)
        rating_part2 = choice
        one_star.remove(choice)







    elif(rating == 2):   
        choice = random.choice(two_star)
        rating_part1 = choice
        two_star.remove(choice)
        choice = random.choice(two_star)
        rating_part2 = choice
        two_star.remove(choice)
    elif(rating == 3):   
        choice = random.choice(three_star)
        rating_part1 = choice
        three_star.remove(choice)
        choice = random.choice(three_star)
        rating_part2 = choice
        three_star.remove(choice)
    elif(rating == 4):   
        choice = random.choice(four_star)
        rating_part1 = choice
        four_star.remove(choice)
        choice = random.choice(four_star)
        rating_part2 = choice
        four_star.remove(choice)
    else:
        choice = random.choice(five_star)
        rating_part1 = choice
        five_star.remove(choice)
        choice = random.choice(five_star)
        rating_part2 = choice
        five_star.remove(choice)
    
    
    
    
    review = "Quaint resturant spot with " + rating_part1 + " food and " + rating_part2 + " service ([" + str(rating) + "/5] starts)."
    return review 
    

# Example usage
print(theme_list)
theme = input("Input a theme: ")
restaurant_name = generate_restaurant_name(theme)
restaurant_menu = generate_restaurant_menu(theme)
restaurant_review = generate_restaurant_review(1, restaurant_name, theme)
print(restaurant_name)  # Output: Slice of Heaven Delicious Pizza
print(restaurant_menu)
print(restaurant_review)