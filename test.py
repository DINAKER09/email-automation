import re

# Sample Paragraph
paragraph = """
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

# Regular Expression for Email Extraction
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all emails in the paragraph
emails_found = re.findall(email_pattern, paragraph)

# Output the extracted emails
print("Extracted Emails:", emails_found)
