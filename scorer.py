def judge(question, expects, answer, results) -> bool:
    """
    `expects` may hold more than one required phrase, separated by ";" —
    used for questions that ask for two things at once. An answer passes
    only if every phrase shows up in it.
    """
    answer_lower = answer.lower().strip()
    parts = [p.strip().lower() for p in expects.split(";") if p.strip()]
    return all(part in answer_lower for part in parts)