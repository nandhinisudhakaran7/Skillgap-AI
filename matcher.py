from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_skills(resume_skills, job_skills):
    if not job_skills:
        return 0

    resume_text = " ".join(resume_skills)
    job_text = " ".join(job_skills)

    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_text, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()

    return round(score * 100, 2)