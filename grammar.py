import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def grammar_score(text):

    errors = len(tool.check(text))

    words = text.split()
    total_words = len(words)

    if total_words == 0:
        return {
            "score": 0,
            "errors": 0,
            "error_rate": 0
        }

    error_rate = errors / total_words

    # Score based on error density
    if error_rate < 0.005:      # <0.5%
        score = 10
    elif error_rate < 0.01:     # <1%
        score = 9
    elif error_rate < 0.02:     # <2%
        score = 8
    elif error_rate < 0.03:     # <3%
        score = 7
    elif error_rate < 0.05:     # <5%
        score = 6
    elif error_rate < 0.08:     # <8%
        score = 5
    elif error_rate < 0.12:     # <12%
        score = 4
    elif error_rate < 0.16:     # <16%
        score = 3
    elif error_rate < 0.20:     # <20%
        score = 2
    else:
        score = 1

    return {
        "score": score,
        "errors": errors,
        "total_words": total_words,
        "error_rate": round(error_rate * 100, 2)
    }

