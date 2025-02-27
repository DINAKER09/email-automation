import os
import re
import smtplib
from email.message import EmailMessage

# Email Credentials (Consider using environment variables for security)
sender_email = "dinakerkr@gmail.com"
sender_password = "gllcscuuqqwzqdvf"

# Sample job posting message
job_posting = """
We are looking for C# Developer with Blazor @ Moorestown, NJ which is 3 to 4 days a week onsite from Day one. And its Contract to hire, we are looking for US Citizen or Green Card, who can accept Full time with 6 months time frame

 

Please check the below JD and get back If you comfortable. Let me know, the best time to call you discuss further.

 

Key Attributes:

Problem Solver that really cares
Someone who wants to build cool stuff, not maintain old stuff, but jump  into projects and not be afraid to build and do things they haven’t done before
Hungry (younger) Engineer 
High sense of urgency
Good technical person
These Engineers will be working with a team of best people, a big product they’re focused on right now is building out an UW workbench
 

Technical Skills:

C# (Must have)- Skill #1
Entity Framework (Must have)- Skill #2
Web API Experience (Must have)- Skill #3
Understanding of SQL Server
Blazor UI- If they don’t have Blazor, but they have React or Angular, this will work
 

Cheers

Vijay

 



VIJAY KUMAR ALLAMSETTI

VP, Staffing Operations & Recruiting

(M) 609 582 1491 (W) 408 722 9031

vkallamsetti@stratustech.com

www.stratustech.com

740 Broad Street, Ste 1, Shrewsbury, NJ 07702

"""

# Improved regex (case-insensitive)
role_match = re.search(r"(?:Job Role|Job Title|Position)\s*[:\-]\s*(.+)", job_posting, re.IGNORECASE)
location_match = re.search(r"Location\s*[:\-]\s*(.+)", job_posting, re.IGNORECASE)
email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", job_posting, re.IGNORECASE)

# Extract values and set defaults
role = role_match.group(1).strip() if role_match else ".NET Developer"  # Default role if not found
location = location_match.group(1).strip() if location_match else "USA"  # Default location if not found
email = email_match.group(1).strip() if email_match else "Not Found"

# Debugging Output
print("\n---- Extracted Details ----")
print(f"Recruiter Email: {email}")
print(f"Job Role: {role}")
print(f"Location: {location}")

# Check if email is missing
if email == "Not Found":
    print("\n⚠ ERROR: Failed to extract email from the job posting. Check formatting.")
else:
    print("\n✅ Extraction Successful! Proceeding to send the email.")

    # Email Content
    subject = f"Application for {role} in {location}"
    body = f"""Hi {email.split('@')[0]},

I hope you are doing well.

I recently came across your job posting for the {role} position in {location}, and I am highly interested in this opportunity. With extensive experience in C#, .NET, RESTful APIs, SQL databases,and front-end technologies like Vue.js/React/Angular, I believe my skills align well with the role requirements.

I have attached my resume for your review. I would love to discuss how my expertise can contribute to your team’s success. Please let me know a convenient time for a quick call.

Looking forward to your response.

Best regards,  
Dinaker K  
📞 (786) 548-1831  
✉️ dinakerkr@gmail.com  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/dinakerkr)  
"""

    # Resume file path (Ensure the file exists)
    resume_path = "/Users/dinakerreddykesireddy/Desktop/email_project/Dinaker_Sr Full Stack .NET Developer.docx"

    # Prepare Email with Attachment
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = email

    # Attach Word Document Resume
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
        print(f"Error: Resume file not found at {resume_path}. Please check the file path.")
        exit()

    # Sending Email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("✅ Email sent successfully with the resume attached!")
    except Exception as e:
        print("❌ Error sending email:", e)
