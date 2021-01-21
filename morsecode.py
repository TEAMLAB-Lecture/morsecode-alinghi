# -*- coding: utf8 -*-
import re
# Help Function - 수정하지 말 것


def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code
# Help Function - 수정하지 말 것


def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    return user_input.lower() == "h" or user_input.lower() == "help"


def is_validated_english_sentence(user_input):
    count = 0
    for ch in user_input:
        if ch.isdigit():
            return False
        elif ch.isalpha():
            count += 1
        else:
            if ch in ".,!? ":
                continue
            else:
                return False
    return count > 0


def is_validated_morse_code(user_input):
    for morse in user_input.split():
        if morse not in reverse_code_dict.keys():
            return False

    return True


def get_cleaned_english_sentence(raw_english_sentence):
    raw_english_sentence = raw_english_sentence.strip()
    return "".join(map(lambda x: x if x not in ".,!?" else "", raw_english_sentence))


def decoding_character(morse_character):
    return reverse_code_dict[morse_character]


def encoding_character(english_character):
    return morse_code_dict[english_character]


def decoding_sentence(morse_sentence):
    ret = ""
    ms = morse_sentence.split("  ")
    for mw in ms:
        for mc in mw.split():
            ret += decoding_character(mc)
        ret += " "
    return ret[:-1]


def encoding_sentence(english_sentence):
    english_sentence = get_cleaned_english_sentence(english_sentence).upper()
    english_sentence = re.sub("\s+", " ", english_sentence)
    return " ".join(map(lambda x: "" if x == " " else encoding_character(x), english_sentence))


def main():
    print("Morse Code Program!!")
    while True:
        s = input("Input your message(H - Help, 0 - Exit): ")
        if s == "0":
            break
        if is_help_command(s):
            print(get_help_message())
            continue
        if is_validated_english_sentence(s):
            print(encoding_sentence(s))
        elif is_validated_morse_code(s):
            print(decoding_sentence(s))
        else:
            print("Wrong Input")
    print("Good Bye")
    print("Morse Code Program Finished!!")


morse_code_dict = get_morse_code_dict()
reverse_code_dict = {}
for k, v in morse_code_dict.items():
    reverse_code_dict[v] = k

if __name__ == "__main__":
    main()
