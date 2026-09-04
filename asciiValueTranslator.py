import os


def ascii_Translator():
    logo = r"""
    ___              _ _     ______                      __      __     
   /   |  __________(_|_)   /_  __/________ _____  _____/ /___ _/ /____ 
  / /| | / ___/ ___/ / /_____/ / / ___/ __ `/ __ \/ ___/ / __ `/ __/ _ \
 / ___ |(__  ) /__/ / /_____/ / / /  / /_/ / / / (__  ) / /_/ / /_/  __/
/_/  |_/____/\___/_/_/     /_/ /_/   \__,_/_/ /_/____/_/\__,_/\__/\___/ 
    """

    help_manual = ">> Press 'q' for quit or 'c' for clear the screen...."

    ascii_list = {
        "A": 65,
        "B": 66,
        "C": 67,
        "D": 68,
        "E": 69,
        "F": 70,
        "G": 71,
        "H": 72,
        "I": 73,
        "J": 74,
        "K": 75,
        "L": 76,
        "M": 77,
        "N": 78,
        "O": 79,
        "P": 80,
        "Q": 81,
        "R": 82,
        "S": 83,
        "T": 84,
        "U": 85,
        "V": 86,
        "W": 87,
        "X": 88,
        "Y": 89,
        "Z": 90,
        "[": 91,
        "\\": 92,
        "]": 93,
        "^": 94,
        "_": 95,
        "`": 96,
        "a": 97,
        "b": 98,
        "c": 99,
        "d": 100,
        "e": 101,
        "f": 102,
        "g": 103,
        "h": 104,
        "i": 105,
        "j": 106,
        "k": 107,
        "l": 108,
        "m": 109,
        "n": 110,
        "o": 111,
        "p": 112,
        "q": 113,
        "r": 114,
        "s": 115,
        "t": 116,
        "u": 117,
        "v": 118,
        "w": 119,
        "x": 120,
        "y": 121,
        "z": 122,
        "{": 123,
        "|": 124,
        "}": 125,
        "~": 126,
    }

    reversed_ascii_list = {v: k for k, v in ascii_list.items()}
    os.system("clear")
    print(logo)
    print("Press -h for the manual or 'q' for quit")

    while True:
        try:
            select_type = input(
                "\nTranslate To:\n1. Decimal to Char\n2. Char to Decimal\n >> "
            )
        except ValueError:
            print("PLEASE INSERT 1 OR 2")
            return

        if select_type == "1":
            print("please insert numbers separated by space (e.g., 65 66)")
            try:
                user_input = input("(range 65 - 126)>> ")
                decimal_list = [int(num) for num in user_input.split()]

                char_list = []

                for decimal_char in decimal_list:
                    if 65 <= decimal_char <= 126:
                        char_list.append(reversed_ascii_list[decimal_char])
                    else:
                        print(f"{decimal_char} its out of the range")
                        continue

                result = "".join(char_list)

                print(f"the number u give: {decimal_list}")
                print(f"The result is: {result}")
                continue_quest = input(">> Continue? (press y or n)>> ").lower()
                if continue_quest == "y":
                    continue
                else:
                    break

            except ValueError:
                print("the value is undifined!")
                print("Please separate with a space between the number")
                continue_quest = input(">> Continue? (press y or n)>> ").lower()
                if continue_quest == "y":
                    continue
                else:
                    break

            except KeyError:
                print("the key is undifined")
                print("Please separate with a space between the number")
                continue_quest = input(">> Continue? (press y or n)>> ").lower()
                if continue_quest == "y":
                    continue
                else:
                    break

        elif select_type == "2":
            print("please type any alphabet (e.g., 'CAR')")
            try:
                user_input = input(" >> ")

                decimal_result_list = []

                for char in user_input:
                    if char in ascii_list:
                        decimal_result_list.append(ascii_list[char])
                    else:
                        print("The character is not avaiable")
                        continue_quest = input(">> Continue? (press y or n)>> ").lower()
                        if continue_quest == "y":
                            continue
                        else:
                            break

                else:
                    print(f"The word u give: {user_input}")
                    print(f"The result: {decimal_result_list}")
                    continue_quest = input(">> Continue? (press y or n)>> ").lower()
                    if continue_quest == "y":
                        continue
                    else:
                        break

            except KeyError:
                print("The value is undifined")

        elif select_type == "q":
            os.system("clear")
            print("GOOD BYE :)")
            break

        elif select_type == "-h":
            print(help_manual)

        elif select_type == "c":
            os.system("clear")

        else:
            print("Operation is not avaiable")
            continue


if __name__ == "__main__":
    ascii_Translator()
