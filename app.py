from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

from utils.parser import parse_file
from utils.cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.matcher import match_skills
from utils.report import create_report

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ✅ SINGLE upload route (FIXED)
@app.route('/upload', methods=['POST'])
def upload():
    resume_file = request.files['resume']
    job_file = request.files['job']

    resume_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
    job_path = os.path.join(UPLOAD_FOLDER, job_file.filename)

    resume_file.save(resume_path)
    job_file.save(job_path)

    # 🔥 Parse
    resume_text = parse_file(resume_path)
    job_text = parse_file(job_path)

    # 🔥 Clean
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    # 🔥 Extract Skills
    resume_skills = list(extract_skills(resume_clean))
    job_skills = list(extract_skills(job_clean))

    # 🔥 Match
    score = match_skills(resume_skills, job_skills)

    # 🔥 Matched & Missing Skills (IMPORTANT FIX)
    matched_skills = [skill for skill in job_skills if skill in resume_skills]
    missing_skills = [skill for skill in job_skills if skill not in resume_skills]

    # 🔥 Create Report
    create_report({
        "score": score,
        "resume_skills": resume_skills,
        "job_skills": job_skills
    })

    # ✅ RETURN CORRECT FORMAT (VERY IMPORTANT)
    return jsonify({
        "match_percent": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_skills": resume_skills,
        "job_skills": job_skills
    })


# ✅ Download Route
@app.route('/download')
def download():
    return send_file("report.pdf", as_attachment=True)


# ✅ Run App
if __name__ == "__main__":
    app.run(debug=True)