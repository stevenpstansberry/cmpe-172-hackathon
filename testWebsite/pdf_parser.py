import PyPDF2


topics = [
    'List major Food insecurity reason in 2023',
    'Explain malnutrition in war zones',
    'Explain increase prices impact on food security'
]

# Parse pdf and format it, removing white space
def parse_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        full_text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            full_text += page.extract_text()
    
    formatted_text = full_text.replace('\n', ' ')  

    return formatted_text
