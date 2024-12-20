from re import findall
from sys import argv

HIDDEN_POWERS = {
    0: "Bug",
    1: "Dark",
    2: "Dragon",
    3: "Electric",
    4: "Fight",
    5: "Fire",
    6: "Fly",
    7: "Ghost",
    8: "Grass",
    9: "Ground",
    10: "Ice",
    11: "Water",
    12: "Poison",
    13: "Psychic",
    14: "Rock",
    15: "Steel",
}


def calculate_formula(a: int, b: int, c: int, d: int, e: int, f: int, *_) -> int:
    tmp = a + 2 * b + 4 * c + 8 * d + 16 * e + 32 * f
    return int(tmp * 15 / 63)


def calculate_hidden_power(genocode: str) -> str:
    numbers = findall(r"\d+", genocode)
    numbers_from_string = map(lambda x: int(x) % 2, numbers)

    try:
        return HIDDEN_POWERS.get(calculate_formula(*numbers_from_string))
    except:
        return "Error"


def main():
    for id, genocode in enumerate(argv[1:]):
        print(id + 1, genocode, calculate_hidden_power(genocode))


if __name__ == "__main__":
    main()
