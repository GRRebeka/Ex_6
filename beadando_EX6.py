
###Write a program that automatically converts English text to Morse code and vice versa###
###Írj egy olyan programot, amely automatikusan átalakítja az angol szöveget Morse-kódra és fordítva###


morse_abc={'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..',
'0': '-----', '1': '.----', '2': '..---',
'3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..',
'9': '----.', '!':'--.--', ',':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-',
'(':'-.--.', ')':'-.--.-'}

def encode(eng_text):
    ncode=''
    szoveg=eng_text.upper()
    for szo in szoveg:
        for betu in szo.split():
            ncode +=morse_abc[betu]
        ncode +='***'


    print(ncode)


#def decode(morse_code):



letter=input("Add meg a mondatot: ")
encode(letter)

