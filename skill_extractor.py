import spacy

nlp = spacy.load("en_core_web_sm")

skills_list = [
 "python","java","sql","machine learning",
 "deep learning","nlp","data science",
 "html","css","javascript","react"
]

def extract_skills(text):
    doc = nlp(text)
    found = set()

    for token in doc:
        if token.text in skills_list:
            found.add(token.text)

    return found