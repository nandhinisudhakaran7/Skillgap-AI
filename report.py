from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_report(data, filename="report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("SkillGap AI Report", styles['Title']))
    content.append(Paragraph(f"Match Score: {data['score']}%", styles['Normal']))
    content.append(Paragraph(f"Resume Skills: {data['resume_skills']}", styles['Normal']))
    content.append(Paragraph(f"Job Skills: {data['job_skills']}", styles['Normal']))

    doc.build(content)