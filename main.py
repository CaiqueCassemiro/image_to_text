import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
data = pytesseract.image_to_string('./images/image.PNG')

data = data.replace("\n"," ")
data = data.split(' ')
data = [x for x in data if len(x) > 0]

regex = re.compile(r'^(\d{3}.){2}\d{3}-\d{2}$')

qtd_cpf = 0
for x in data:
    regex_result = re.search(regex, x)
    if regex_result:
        qtd_cpf+=1

print(f'{qtd_cpf} CPFs encontrados')

del qtd_cpf