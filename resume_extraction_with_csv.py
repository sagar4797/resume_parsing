import nltk
import spacy
import csv
import docx2txt
import os
from pyresparser import ResumeParser
from multiprocessing import Pool, cpu_count

# Download the stopwords resource
nltk.download('stopwords')

# Load the spaCy model
spacy_model_name = 'en_core_web_sm'
spacy.load(spacy_model_name)

resume_directory = 'resumes/'
output_csv_path = 'extracted_data.csv'

def process_resume(resume_path):
    try:
        if resume_path.endswith('.pdf'):
            data = ResumeParser(resume_path).get_extracted_data()
            return data
            
        elif resume_path.endswith('.docx'):
            data = ResumeParser(resume_path).get_extracted_data()
            return data
        
    except Exception as e:
        print(f"Error processing {resume_path}: {e}")
        return None

if __name__ == '__main__':
    extracted_data_list = []
    
    files_to_process = []
    for filename in os.listdir(resume_directory):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            resume_path = os.path.join(resume_directory, filename)
            files_to_process.append(resume_path)
    
    with Pool(cpu_count()) as pool:
        extracted_data_list = pool.map(process_resume, files_to_process)
    
    # Remove None values (failed processed files)
    extracted_data_list = [data for data in extracted_data_list if data is not None]
    
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Email', 'Phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for data in extracted_data_list:
            name = data['name']
            email = data['email']
            phone = data['mobile_number']
            
            writer.writerow({'Name': name, 'Email': email, 'Phone': phone})

    for data in extracted_data_list:
        name = data['name']
        email = data['email']
        phone = data['mobile_number']

        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print()
