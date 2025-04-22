# Planetary Weights

"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Prompt the user for the planet name
    planet = input("Enter a planet: ")

    # Dictionary of planet gravity percentages
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Check if the entered planet is valid and calculate
    if planet in gravity_factors:
        planetary_weight = earth_weight * gravity_factors[planet]
        rounded_weight = round(planetary_weight, 2)
        print(f"The equivalent weight on {planet}: {rounded_weight}")
    else:
        print("Invalid planet. Please enter a valid planet name with the first letter capitalized.")

if __name__ == "__main__":
    main()
