import re


def is_vowel(ch):
    return ch.lower() in "aeiouyäëïöüÿáéíóúý"


def is_short_vowel(ch):
    return ch.lower() in "aeiouyäëïöüÿ"


def is_diphthong(s):
    return s.lower() in [
        # Both
        "ai",
        "ui",
        "au",
        # Quenya only
        "oi",
        "iu",
        "eu",
        # Sindarin only
        "ae",
        "ei",
        "oe",
        "aw",  # @@@ at end
    ]


def is_valid_consonant_cluster(s):
    return s.lower().startswith(("gl",))  # @@@ INCOMPLETE!


def display_word(w):
    return ".".join(w)


def syllabify(word, debug=False):
    word = word.lower()
    word = re.sub("dh", "ð", word)
    word = re.sub("th", "θ", word)
    word = re.sub("ch", "χ", word)
    word = re.sub("ng(?=.)", "ŋg", word)
    word = re.sub("ng", "ŋ", word)
    state = 0
    result = []
    current_syllable = []
    for ch in word[::-1]:
        if state == 0:
            current_syllable.insert(0, ch)
            if is_vowel(ch):
                state = 1
            if debug:
                print("c", state, current_syllable)  # pragma: no cover
        elif state == 1:
            if is_vowel(ch):
                if is_diphthong(ch + current_syllable[0]):
                    current_syllable.insert(0, ch)
                    if debug:
                        print("c", state, current_syllable)  # pragma: no cover
                else:
                    result.insert(0, current_syllable)
                    if debug:
                        print("r", result)  # pragma: no cover
                    current_syllable = [ch]
                    if debug:
                        print("c", state, current_syllable)  # pragma: no cover
            else:
                current_syllable.insert(0, ch)
                state = 2
                if debug:
                    print("c", state, current_syllable)  # pragma: no cover
        elif state == 2:
            if is_vowel(ch):
                result.insert(0, current_syllable)
                if debug:
                    print("r", result)  # pragma: no cover
                current_syllable = [ch]
                if debug:
                    print("c", state, current_syllable)  # pragma: no cover
                state = 1
            else:
                if is_valid_consonant_cluster(ch + "".join(current_syllable)):
                    current_syllable.insert(0, ch)
                    if debug:
                        print("c", state, current_syllable)  # pragma: no cover
                else:
                    result.insert(0, current_syllable)
                    if debug:
                        print("r", result)  # pragma: no cover
                    current_syllable = [ch]
                    state = 0
                    if debug:
                        print("c", state, current_syllable)  # pragma: no cover
    result.insert(0, current_syllable)
    if debug:
        print("r", result)  # pragma: no cover

    result = ["".join(syllable) for syllable in result]

    if len(result) == 1:
        result[-1] = result[-1].upper()
    elif len(result) == 2:
        result[-2] = result[-2].upper()
    elif not is_short_vowel(result[-2][-1]):
        result[-2] = result[-2].upper()
    else:
        result[-3] = result[-3].upper()

    return result
