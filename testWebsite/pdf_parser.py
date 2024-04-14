import PyPDF2
import re

def parse_pdf(pdf_path, max_tokens=4096):
    # Function to clean and reduce the text
    def clean_text(text):
        # Replace unwanted characters
        text = text.replace('\n', ' ')
        # Remove excessive whitespace
        text = ' '.join(text.split())
        return text
    
    # Function to truncate text to fit token limit
    def truncate_text(text, token_limit):
        # Estimate the average token size and use it to calculate a safe character limit
        avg_token_size = 12  
        char_limit = token_limit * avg_token_size
        
        if len(text) > char_limit:
            return text[:char_limit] + '...'  # Truncate and add ellipsis
        return text
    
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        full_text = ''
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            full_text += page.extract_text()
    
    formatted_text = clean_text(full_text)
        
    # Truncate the text to fit within the token limit for GPT-3.5
    truncated_text = truncate_text(formatted_text, max_tokens)
    
    return truncated_text

pdf_path = 'SOFI-2023.pdf'  # Replace with your actual PDF path
formatted_text = parse_pdf(pdf_path, max_tokens=4096)  # Adjust the max_tokens as needed
print(formatted_text)

