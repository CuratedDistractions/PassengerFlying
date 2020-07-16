def decode_xplane_text(text):
    CHARACTERS = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "😳",
        "😳",
        "😳",
        "😳",
        "😳",
        "😳",
        "😳",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    result = ""

    try:
        for i in text:
            # We substract 48 from i because the first 48 characters in the list X-Plane uses are empty
            # And I don't want to add 48 bogus elements to my list above. :)
            corrected_index = int(i) - 48
            if corrected_index > 0:  # Can't request an index below 0
                result = "".join([result, CHARACTERS[corrected_index]])
        return result
    except IndexError as e:
        return f"EMPTY_STRING ({e})"
