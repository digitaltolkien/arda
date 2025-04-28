import re


def is_vowel(ch, ipa):
    if ipa:
        return ch.lower() in "ɑeiouy"
    else:
        return ch.lower() in "aeiouyäëïöüÿáéíóúý"


def is_short_vowel(ch):
    return ch.lower() in "aeiouyäëïöüÿ"


def is_ipa_vowel(ch):
    return ch.lower() in "ɑeiouy"


def is_diphthong(s, ipa):
    if ipa:
        return s.lower() in [
            "ɑi",
            "ui",
            "ɑu",
            "oi",
            "iu",
            "eu",
            "ɑe",
            "ei",
            "oe",  # @@@
        ]
    else:
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


def is_valid_consonant_cluster(s, ipa):
    return s.lower().startswith(("gl",))  # @@@ INCOMPLETE!


def display_word(w):
    return "·".join(s.strip("·") for s in w)


def syllabify(word, ipa=False, debug=False):
    word = word.lower()
    if not ipa:
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
            if ipa and ch == "ˈ":
                state = 1
            elif is_vowel(ch, ipa):
                state = 1
            if debug:
                print("c", state, current_syllable)  # pragma: no cover
        elif state == 1:
            if is_vowel(ch, ipa):
                if current_syllable[0] == "ˈ":
                    current_syllable.insert(0, ch)
                    if debug:
                        print("c", state, current_syllable)  # pragma: no cover
                elif is_diphthong(ch + current_syllable[0], ipa):
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
            if is_vowel(ch, ipa):
                result.insert(0, current_syllable)
                if debug:
                    print("r", result)  # pragma: no cover
                current_syllable = [ch]
                if debug:
                    print("c", state, current_syllable)  # pragma: no cover
                state = 1
            else:
                if is_valid_consonant_cluster(ch + "".join(current_syllable), ipa):
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
        if ipa:
            result[-1] = "ˈ" + result[-1]
        else:
            result[-1] = result[-1].upper()
    elif len(result) == 2:
        if ipa:
            result[-2] = "ˈ" + result[-2]
        else:
            result[-2] = result[-2].upper()
    elif ipa and (result[-2][-1] == "ː" or not is_ipa_vowel(result[-2][-1])):
        result[-2] = "ˈ" + result[-2]
    elif not ipa and not is_short_vowel(result[-2][-1]):
        result[-2] = result[-2].upper()
    else:
        if ipa:
            result[-3] = "ˈ" + result[-3]
        else:
            result[-3] = result[-3].upper()

    return result


rules = [
    ("b", "b"),
    ("ch", "χ"),  # weakened in Gondor unless word final or before t
    ("c", "k"),
    ("dh", "ð"),
    ("d", "d"),
    ("f#", "v"),
    ("f", "f"),
    ("gh", "ɣ"),  # black speech / orkish
    ("g", "g"),
    ("ht", "çt"),
    ("hw", "w̥"),
    ("hy", "ç"),
    ("h", "h"),
    ("kh", "χ"),  # not Elvish (and incorrect for Dwarvish)
    ("k", "k"),
    ("lh", "l̥"),
    ("l", "l"),
    ("m", "m"),
    ("ng#", "ŋ"),
    ("ng", "ŋg"),
    ("#ñ", "ŋ"),
    ("n", "n"),
    ("ph", "f"),  # ff if derived from pp
    ("p", "p"),
    ("qu", "kw"),
    ("rh", "r̥"),
    ("r", "r"),
    ("sh", "ʃ"),
    ("s", "s"),
    ("th", "θ"),  # not in Dwarvish
    ("ty", "tj"),
    ("t", "t"),
    ("v", "v"),
    ("w", "w"),
    ("á", "ɑː"),
    ("a", "ɑ"),
    ("eä", "e·ɑ"),
    ("e", "e"),
    ("ëa", "e·ɑ"),
    ("ë", "e"),
    ("#io", "jο"),
    ("i", "i"),
    ("ó", "oː"),
    ("o", "o"),
    ("û", "uː"),
    ("ú", "uː"),
    ("u", "u"),
    ("#", ""),
]


def to_ipa(word):
    ipa = ""
    word = "#" + word.lower() + "#"
    while word:
        for rule_in, rule_out in rules:
            if word.startswith(rule_in):
                ipa += rule_out
                word = word[len(rule_in) :]
                break
        else:
            raise ValueError(f"Can't match: {word}")
    return ipa
