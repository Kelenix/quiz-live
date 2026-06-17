# -*- coding: utf-8 -*-
def S(statement, correct, *wrongs, time_limit=20):
    answers = [{"text": correct, "is_correct": True}] + [{"text": w, "is_correct": False} for w in wrongs]
    return {"statement": statement, "type": "single", "time_limit": time_limit, "answers": answers}

def M(statement, corrects, *wrongs, time_limit=30):
    answers = [{"text": c, "is_correct": True} for c in corrects] + [{"text": w, "is_correct": False} for w in wrongs]
    return {"statement": statement, "type": "multiple", "time_limit": time_limit, "answers": answers}

def TF(statement, is_true, time_limit=15):
    answers = [{"text": "Vrai", "is_correct": is_true}, {"text": "Faux", "is_correct": not is_true}]
    return {"statement": statement, "type": "truefalse", "time_limit": time_limit, "answers": answers}
