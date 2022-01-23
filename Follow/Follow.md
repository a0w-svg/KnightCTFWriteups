# Follow - Steganography
>***Follow the rules ?***
points: 25
in this file, I found the flag exactly in the text extracted from it 
the script I used for this 
```
    # pip install pdfplumber
    import pdfplumber
    path = 'Follow.pdf'
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            print(page.extract_text())
```
flag: 
```
KCTF{This_is_the_real_flag}
```