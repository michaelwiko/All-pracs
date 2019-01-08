print("|----------------------|")
print("| Hex Color Identifier |")
print("|----------------------|")

COLOR_NAMES = {"BLACK": "#000000", "BROWN": "#a52a2a", "CHOCOLATE": "#d2691e", "CORAL": "#ff7f50",
               "CYAN": "#00ffff", "FIREBRICK": "#b22222", "GOLD": "#ffd700", "GRAY": "#bebebe", "IVORY": "#fffff0",
               "RAINBOW": "#wtfidk"}


colors = input("Enter the name of the color: ").upper()
while colors != "":
    if colors in COLOR_NAMES:
        print(colors, "=", COLOR_NAMES[colors])
    else:
        print("Invalid color name")
    colors = input("Enter the name of the color: ").upper()