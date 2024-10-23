
import os
import re
import re
import os
import docx
import pdfplumber
from pdfminer.high_level import extract_pages, extract_text
import pdfplumber
# Function to extract candidate name from the file name

path = 'C:/Users/Anon Hossain/Downloads/Anon Hossain.pdf'
text = extract_text(path)
#print(text)


def extract_candidate_name_from_filename(file_path):
    # Extract the base name of the file (e.g., 'Anon Hossain.pdf')
    file_name = os.path.basename(file_path)

    # Remove the file extension (e.g., 'pdf')
    candidate_name, _ = os.path.splitext(file_name)

    return candidate_name

# Example usage
candidate_name = extract_candidate_name_from_filename(path)
print("\n")
print("Candidate Name:", candidate_name)



# Function to extract emails from a given text
def extract_emails(text):
    mail_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    mail_matches = mail_pattern.findall(text)
    return mail_matches

# Function to split text based on "Reference" and print emails accordingly
def extract_emails_and_print(text):
    # Define the regular expression pattern for matching email addresses
    mail_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    # Find all matches of the pattern in the entire text
    all_mail_matches = mail_pattern.findall(text)

    # Find references section and extract emails
    reference_pattern = re.compile(r'references?|REFERENCES?', re.IGNORECASE)
    split_text = reference_pattern.split(text, 1)

    if len(split_text) > 1:
        # Extract emails from the text after the "Reference" section
        reference_text = split_text[1]
        reference_mail_matches = mail_pattern.findall(reference_text)
    else:
        reference_mail_matches = []

    total_emails = len(all_mail_matches)
    candidate_emails = all_mail_matches[:1]  # Only the first email
    reference_emails = reference_mail_matches

    print(f"Total Email Extracted: {total_emails}")
    #print("\nCandidate Mail:")
    if candidate_emails:
        print("\nCandidate Mail:")
        print(candidate_emails[0])
    else:
        print("No candidate email found.")

    print("\nReference Mails:")
    for mail in reference_emails:
        print(mail)

# Example usage in Google Colab
if __name__ == "__main__":
    extract_emails_and_print(text)



# Function to extract phone numbers from a given text
def extract_phone_numbers(text):
    phone_pattern = re.compile(r'\+?880[-\s]?\d{4}[-\s]?\d{6}|\d{5}[-\s]?\d{6}')
    phone_matches = phone_pattern.findall(text)
    return phone_matches

# Function to split text based on "Reference" and print phone numbers accordingly
def extract_phone_numbers_and_print(text):
    # Define the regular expression pattern for matching phone numbers
    phone_pattern = re.compile(r'\+?880[-\s]?\d{4}[-\s]?\d{6}|\d{5}[-\s]?\d{6}')

    # Find all matches of the pattern in the entire text
    all_phone_matches = phone_pattern.findall(text)

    # Find references section and extract phone numbers
    reference_pattern = re.compile(r'references?|REFERENCES?', re.IGNORECASE)
    split_text = reference_pattern.split(text, 1)

    if len(split_text) > 1:
        # Extract phone numbers from the text after the "Reference" section
        reference_text = split_text[1]
        reference_phone_matches = phone_pattern.findall(reference_text)
    else:
        reference_phone_matches = []

    total_phone_numbers = len(all_phone_matches)
    candidate_phone_number = all_phone_matches[:1]  # Only the first phone number
    reference_phone_numbers = reference_phone_matches

    print(f"\nTotal Phone Numbers Extracted: {total_phone_numbers}")
    print("\nCandidate Phone:")
    if candidate_phone_number:
        print(candidate_phone_number[0])
    else:
        print("No candidate phone number found.")

    print("\nReference Phone Numbers:")
    for phone in reference_phone_numbers:
        print(phone)

# Example usage in Google Colab
if __name__ == "__main__":
    extract_phone_numbers_and_print(text)