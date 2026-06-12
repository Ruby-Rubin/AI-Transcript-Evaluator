from lexicalrichness import LexicalRichness

def vocabulary_score(text):

    if not text.strip():
        return {
            "score": 0,
            "mtld": 0
        }

    lex = LexicalRichness(text)

    mtld = lex.mtld()

    score = ((mtld - 20) / 60) * 10

    score = max(0, min(score, 10))

    score = round(score, 2)

    return {
        "score": score,
        "mtld": round(mtld, 2)
    }