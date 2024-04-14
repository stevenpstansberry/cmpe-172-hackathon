from openai import OpenAI
from pdf_parser import *


pdf_path = 'SOFI-2023.pdf'  

formatted_text = parse_pdf(pdf_path, max_tokens=4096) 
#print(formatted_text_for_gpt)

# Init openAI API session
client = OpenAI()

systemPrompt = f"""
You are an AI assistant that will answer questions related to the following topics:
List major Food insecurity reason in 2023,
 Explain malnutrition in war zones, 
 Explain increase prices impact on food security. 
 Your source of knowledge is from the following text, 
 and you will construct your responses from this text:
{formatted_text} 
"""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": systemPrompt},
    {"role": "user", "content": "tell me about major areas of food insecurity"}
  ]
)

print(completion.choices[0].message)