import ahocorasick

def build_automata():
    A = ahocorasick.Automaton()
    keywords = {
        "ruby": ["def ", "puts ", "end ","print "],
        "julia": ["function", "println"],
        "perl": ["sub ", "print "]
    }

    for lang, words in keywords.items():
        for word in words:
            A.add_word(word, (lang, word))
    A.make_automaton()
    return A

def detect_language(code):
    automata = build_automata()
    results = []
   
    for _, (lang, word) in automata.iter(code):
        results.append(lang)
    return results




