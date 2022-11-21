def cipher(word, cipherScheme):
    result = ''
    for letter in word:
        if letter.upper() in cipherScheme:
            result += cipherScheme[letter.upper()]
        else:
            result += letter.upper()
    return result


def stringToScheme(text):
    kod = {}
    for i in range(0, len(text)-1, 2):
        kod[text[i].upper()] = text[i+1].upper()
        kod[text[i+1].upper()] = text[i].upper()
    return kod


def isUnequivocal(text):
    if len(text) % 2 == 1:
        return False
    a = {}
    for i in range(0, len(text), 2):
        if text[i] not in a:
            a[text[i]] = text[i+1]
        elif text[i+1] != a[text[i]]:
            return False
        if text[i+1] not in a:
            a[text[i+1]] = text[i]
        elif text[i] != a[text[i+1]]:
            return False
    return True


def main():
    typ = input("Którego szyfru chcesz użyć? Wpisz 1, 2 lub 3\n1: GA-DE-RY-PO-LU-KI\n2: PO-LI-KA-TY-RE-NU\n3: Własny szyfr\n")
    if typ == '1':
        code = "GADERYPOLUKI"
    elif typ == '2':
        code = "POLIKATYRENU"
    elif typ == '3':
        code = input("Wpisz poniżej własny szyfr postaci <<ABCDEF>>:\n")
        if not isUnequivocal(code):
            print("Ten kod nie jest jednoznaczny!")
            return 0
    else:
        print("Error")
        return 0
    text = input("Co chcesz szyfrować? Wpisz tekst poniżej:\n")
    print(f"Zaszyfrowany/odszyfrowany kod to:\n{cipher(text, stringToScheme(code))}")


main()
