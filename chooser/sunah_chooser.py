
def sunah_chooser(constant): #IND
    text = ""
    ptext = f"texts/suna/suna_{constant}"
    with open(ptext, "r") as s:
        for line in s:
            text = text + line
    return text

