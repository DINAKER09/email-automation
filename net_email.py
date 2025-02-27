import os
import re
import smtplib
from email.message import EmailMessage

# 📂 **Read job posting from file**
job_posting_file = "/Users/dinakerreddykesireddy/Desktop/email_project/net_job_posting.txt"

# Check if file exists
if not os.path.exists(job_posting_file):
    print(f"❌ ERROR: Job posting file not found at {job_posting_file}. Please check the file path.")
    exit()

# Read job posting content
with open(job_posting_file, "r", encoding="utf-8") as file:
    job_posting = file.read()

# ✅ **Keep existing role and location extraction as per your request**
role_match = re.search(r"(?:Job Role|Job Title|Position)\s*[:\-]\s*(.+)", job_posting, re.IGNORECASE)
location_match = re.search(r"Location:\s*([\w\s]+?)(?:,|$)", job_posting, re.IGNORECASE)

# 🔹 **Fixed Email Extraction** (Uses `re.findall()` to get all emails and picks the first one)
email_match = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", job_posting)

# **Assign default values if missing**
role = role_match.group(1).strip() if role_match else ".NET Developer"  # Default to ".NET Developer"
location = location_match.group(1).strip() if location_match else "USA"  # Default to "USA"
email = email_match[0] if email_match else "Not Found"  # ✅ Fix: Picks the first valid email or returns "Not Found"

# ✅ **Debugging Output**
print("\n---- Extracted Details ----")
print(f"Recruiter Email: {email}")
print(f"Job Role: {role}")
print(f"Location: {location}")

# **Check if Email is Extracted**
if email == "Not Found":
    print("\n⚠ ERROR: Failed to extract email from the job posting. Check formatting.")
else:
    print("\n✅ Extraction Successful! Proceeding to send the email.")

    # 📩 **Email Content**
    subject = f"Application for {role} in {location}"
    body = f"""Hi {email.split('@')[0]},

I hope you are doing well.

I recently came across your job posting for the {role} position in {location}, and I am very interested in this opportunity.With extensive experience in C#, .NET, RESTful APIs, SQL databases, and front-end technologies like Vue.js/React/Angular, I believe my skills align well with the role requirements.

I have attached my resume for your review. I would love to discuss how my expertise can contribute to your team’s success.
Please let me know a convenient time for a quick call.

Looking forward to your response.

Best regards,  
Dinaker K  
📞 (786) 548-1831  
✉️ dinakerkr@gmail.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/dinakerkr)  
"""

    # 📂 **Resume File Path (Ensure file exists)**
    resume_path = "/Users/dinakerreddykesireddy/Desktop/email_project/Dinaker_Sr Full Stack .NET Developer.docx"

    # ✅ **Prepare Email with Attachment**
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "dinakerkr@gmail.com"
    msg["To"] = email

    # 📎 **Attach Resume**
    try:
        with open(resume_path, "rb") as resume_file:
            resume_data = resume_file.read()
            msg.add_attachment(
                resume_data,
                maintype="application",
                subtype="vnd.openxmlformats-officedocument.wordprocessingml.document",
                filename="Dinaker_Sr_Full_Stack_NET_Developer.docx"
            )
    except FileNotFoundError:
        print(f"❌ ERROR: Resume file not found at {resume_path}. Please check the file path.")
        exit()

    # 📤 **Send Email**
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("dinakerkr@gmail.com", "gllcscuuqqwzqdvf")
            server.send_message(msg)

        print("\n✅ Email sent successfully with the resume attached!")
    except Exception as e:
        print(f"\n❌ ERROR Sending Email: {e}")
