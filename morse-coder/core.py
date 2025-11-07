morse = {
    "a": "._",
    "b": "_...",
    "c": "_._.",
    "d": "_..",
    "e": ".",
    "f": ".._.",
    "g": "__.",
    "h": "....",
    "i": "..",
    "j": ".___",
    "k": "_._",
    "l": "._..",
    "m": "__",
    "n": "_.",
    "o": "___",
    "p": ".__.",
    "q": "__._",
    "r": "._.",
    "s": "...",
    "t": "_",
    "u": ".._",
    "v": "..._",
    "w": ".__",
    "x": "_.._",
    "y": "_.__",
    "z": "__..",
    "0": "_____",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    ".": "._._._",
    ",": "__..__",
    "?": "..__..",
    "'": ".____.",
    "!": "_._.__",
    "/": "_.._.",
    "(": "_.__.",
    ")": "_.__._",
    "&": "._...",
    ":": "___...",
    ";": "_._._.",
    "=": "_..._",
    "+": "._._.",
    "-": "_...._",
    "_": "..__._",
    '"': "._.._.",
    "$": "..._.._",
    "@": ".__._.",
    " ": "/",
}

morse_inverse = {v: k for k, v in morse.items()}


def encode(text: str) -> str:
    """Translates text in morse code."""
    return " ".join(morse.get(c.lower(), "") for c in text)


def decode(code: str) -> str:
    """Translates Morse code into text."""
    return "".join(morse_inverse.get(c, "") for c in code.split(" "))


def compare(text: str, code: str) -> bool:
    """Checks if the given text is the given code translated."""
    return text == code
