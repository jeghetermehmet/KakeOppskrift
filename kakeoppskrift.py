def skriv_oppskrift(sukker, mel, smor):
    print("Oppskrift på kaker")
    print("Du trenger:")
    print(sukker, "gram sukker")
    print(mel, "gram mel")
    print(smor, "gram smør")

def oppskrift_fra_sukker(sukker):
    return {"sukker": sukker,
            "mel": sukker * 2,
            "smor": sukker * 3}

def oppskrift_fra_mel(mel):
    return {"sukker": mel / 2,
            "mel": mel,
            "smor": mel / 2 * 3}

def oppskrift_fra_smor(smor):
    return {"sukker": smor / 3,
            "mel": smor / 3 * 2,
            "smor": smor}

def bake_kaker():
    ingrediens = input("Vil du basere oppskriften på 'sukker', 'mel' eller 'smør'? ")

    if ingrediens == "sukker":
        sukker = int(input("Hvor mye sukker har du? "))
        ingredienser = oppskrift_fra_sukker(sukker)
    elif ingrediens == "mel":
        mel = int(input("Hvor mye mel har du? "))
        ingredienser = oppskrift_fra_mel(mel)
    elif ingrediens == "smør":
        smor = int(input("Hvor mye smør har du? "))
        ingredienser = oppskrift_fra_smor(smor)
    else:
        print("Ugyldig valg av ingrediens.")
        return

    skriv_oppskrift(ingredienser["sukker"],
                    ingredienser["mel"],
                    ingredienser["smor"])

bake_kaker()
