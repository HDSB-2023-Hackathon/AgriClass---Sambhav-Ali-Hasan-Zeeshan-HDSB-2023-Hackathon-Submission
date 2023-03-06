def get_seed_characteristics():
    # Prompt user for seed length and width
    while True:
        try:
            length = float(input("Enter the length of the seed (in mm): "))
            width = float(input("Enter the width of the seed (in mm): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Prompt user for seed color and shape
    color = input("Enter the color of the seed: ")
    shape = input("Enter the shape of the seed: ")

    # Return a dictionary containing the seed characteristics
    return {"length": length, "width": width, "color": color, "shape": shape}


# Define a function to identify the type of seed based on its characteristics
def identify_seed_type(seed):
    # Define indicators for each seed type
    bean_indicators = {"length": (lambda x: 5 < x < 15), "width": (lambda x: 2 < x < 10),
                       "color": (lambda x: x == "brown"), "shape": (lambda x: x == "oval")}
    pea_indicators = {"length": (lambda x: 2 < x < 8), "width": (lambda x: 1 < x < 5),
                      "color": (lambda x: x == "green"), "shape": (lambda x: x == "round")}
    watermelon_indicators = {"length": (lambda x: 10 < x < 25), "width": (lambda x: 5 < x < 15),
                             "color": (lambda x: x == "green"), "shape": (lambda x: x == "oblong")}
    pumpkin_indicators = {"length": (lambda x: 15 < x < 30), "width": (lambda x: 15 < x < 30),
                          "color": (lambda x: x == "orange"), "shape": (lambda x: x == "round")}
    sunflower_indicators = {"length": (lambda x: 10 < x < 30), "width": (lambda x: 10 < x < 30),
                            "color": (lambda x: x == "brown"), "shape": (lambda x: x == "disc")}
    tomato_indicators = {"length": (lambda x: 10 < x < 30), "width": (lambda x: 10 < x < 30),
                         "color": (lambda x: x == "red"), "shape": (lambda x: x == "round")}
    soybean_indicators = {"length": (lambda x: 5 < x < 15), "width": (lambda x: 2 < x < 10),
                          "color": (lambda x: x == "yellow"), "shape": (lambda x: x == "elliptical")}
    rice_indicators = {"length": (lambda x: 10 < x < 30), "width": (lambda x: 1 < x < 5),
                       "color": (lambda x: x == "white"), "shape": (lambda x: x == "long and narrow")}
    corn_indicators = {"length": (lambda x: 10 < x < 30), "width": (lambda x: 2 < x < 10),
                       "color": (lambda x: x == "yellow"), "shape": (lambda x: x == "oblong")}
    barley_indicators = {"length": (lambda x: 5 < x < 15), "width": (lambda x: 1 < x < 5),
                         "color": (lambda x: x == "golden"), "shape": (lambda x: x == "pear-shaped")}
    
    # Check if the seed matches the indicators for each seed type
    seed_types = {"bean": bean_indicators, "pea": pea_indicators, "watermelon": watermelon_indicators,
                  "pumpkin": pumpkin_indicators, "sunflower": sunflower_indicators, "tomato": tomato_indicators,
                  "soybean": soybean_indicators, "rice": rice_indicators, "corn": corn_indicators,
                  "barley": barley_indicators}
    
    for seed_type, indicators in seed_types.items():
        if all(indicators[characteristic](seed[characteristic]) for characteristic in seed):
            return seed_type

    # If the seed doesn't match any of the seed types, return "unknown"
    return "unknown"


# Main program loop
while True:
    # Prompt user for seed characteristics
    seed = get_seed_characteristics()

    # Identify the type of seed based on its characteristics
    seed_type = identify_seed_type(seed)

    # Output the result
    if seed_type != "unknown":
        print("The seed you entered is a", seed_type, "seed.")
    else:
        print("Unable to identify seed type based on the characteristics entered.")

    # Ask user if they want to identify another seed
    another_seed = input("Do you want to identify another seed? (y/n): ")
    if another_seed.lower() != "y":
        break
