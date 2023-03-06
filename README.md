# AgriClass

# Seed Identifier
This Python program identifies the type of seed based on its characteristics such as length, width, color, and shape. It prompts the user for the seed characteristics, identifies the type of seed based on those characteristics, and outputs the result.

# How to use the program
Run the program in a Python environment.
When prompted, enter the length and width of the seed in millimeters.
Enter the color and shape of the seed.
The program will identify the type of seed based on the entered characteristics and output the result.
You can choose to identify another seed or exit the program.
Functions

The program has two functions:

get_seed_characteristics() - This function prompts the user for the seed characteristics and returns a dictionary containing the seed characteristics.

identify_seed_type(seed) - This function takes in a dictionary of seed characteristics and identifies the type of seed based on those characteristics. It uses a set of indicators for each seed type and checks if the seed matches those indicators.

Seed Types
The program can identify three types of seeds: beans, peas, and watermelons. The characteristics for each seed type are as follows:

1. Bean
Length > 5mm
Width > 2mm
Color is brown
Shape is oval
2. Pea
Length < 3mm
Width < 1mm
Color is white
Shape is round
3. Watermelon
Length > 3mm
Width < 1mm
Color is black
Shape is teardrop

If the seed doesn't match any of the seed types, the program outputs "unknown".
