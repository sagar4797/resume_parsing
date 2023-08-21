from pyresparser import ResumeParser

# Provide the path to the resume file you want to parse
resume_path = 'resumes/resume1.pdf'

# Parse the resume and get the extracted data
data = ResumeParser(resume_path).get_extracted_data()

# Extract name, email, and phone
name = data['name']
email = data['email']
phone = data['mobile_number']

# Print the extracted information
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
