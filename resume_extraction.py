import nltk
import spacy
from pyresparser import ResumeParser

# Download the stopwords resource
nltk.download('stopwords')

# Load the spaCy model
spacy_model_name = 'en_core_web_sm'  # Use the model name
spacy.load(spacy_model_name)

# Provide the path to the resume file you want to parse
resume_path = 'docxfiles/chNagarjunareddy[4_0].docx'  # Update with your file path

# Parse the resume and get the extracted data
data = ResumeParser(resume_path).get_extracted_data()

# Print the extracted data
print(data)
name = data['name']
email = data['email']
phone = data['mobile_number']
skills = data['skills']
# Print the extracted information
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print(f"Skills: {skills}")

