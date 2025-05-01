import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

FORM_MAP = {
    "wages": "Form 1040, Line 1",
    "interest": "Form 1040, Line 2b",
    "dividends": "Form 1040, Line 3b",
    "capital gains": "Form 1040, Line 7",
    "schedule c": "Schedule C, Line 31",
    "self-employment": "Schedule SE, Line 6",
    "student loan interest": "Schedule 1, Line 20",
    "premium tax credit": "Form 8962, Line 26",
    "adoption credit": "Form 8839, Line 18",
    "child tax credit": "Schedule 8812, Line 14f",
    "dependent care credit": "Form 2441, Line 11",
    "additional child tax credit": "Schedule 8812, Line 27",
    "credit for the elderly or disabled": "Schedule R, Line 22",
    "earned income tax credit": "Form 1040, Line 27",
    "retirement savings contributions credit": "Form 8880, Line 14",
    "credit for prior year minimum tax": "Form 8801, Line 25",
    "american opportunity tax credit": "Form 8863, Line 8",
    "lifetime learning credit": "Form 8863, Line 19",
    "residential clean energy credit": "Form 5695, Line 5",
    "energy efficient home improvement credit": "Form 5695, Line 22",
    "clean vehicle credit": "Form 8936, Line 15",
    "alternative fuel vehicle refueling property credit": "Form 8911, Line 19",
}

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(term) for term in FORM_MAP]
matcher.add("TAX_TERMS", patterns)

def extract_keywords(text):
    doc = nlp(text)
    matches = matcher(doc)
    keywords = set()
    for _, start, end in matches:
        span = doc[start:end]
        keywords.add(span.text.lower())
    return [{"keyword": k, "mapping": FORM_MAP[k]} for k in keywords]
