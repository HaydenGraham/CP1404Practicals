
HEX_NAMES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "azure1": "#f0ffff", "blueviolet": "#8a2be2", "blue1": "#0000ff", "cadetblue": "#5f9ea0"}


color = (input("Enter colour name: ")).lower()

while color != "":

    if color in HEX_NAMES:

        print(color, "is", HEX_NAMES[color])

    else:

        print("Invalid colour meme")

    color = (input("Enter colour name: ")).lower()