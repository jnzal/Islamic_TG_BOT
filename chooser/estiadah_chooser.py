
def estiadah_chooser(constant): #IND
    text = ""
    ptext = f"texts/suna_es/suna_es_{constant}"
    with open(ptext, "r") as s:
        for line in s:
            text = text + line
    return text

