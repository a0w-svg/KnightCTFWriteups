# you must to install pip package with name pdfplumber
#!/usr/bin/python3
import pdfplumber
path = 'Follow.pdf'
with pdfplumber.open(path) as pdf:
    for page in pdf.pages:
        print(page.extract_text())