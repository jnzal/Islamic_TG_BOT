
def nawawi_chooser(constant): #IND
    text = ""
    ptext = f"texts/suna_na/nawawi_{constant}"
    with open(ptext, "r") as s:
        for line in s:
            text = text + line
    return text

