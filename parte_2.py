"""
Script que realiza a parte dois do nosso artigo
"""

import re
import pytesseract
import nltk
import pandas as pd
from unidecode import unidecode

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# Lendo a imagem
data = pytesseract.image_to_string('./images/image_2.PNG')

# Retirando as quebras de linha
data = data.replace("\n", " ")

# Transformando String em lista de palavras
# Passando tudo para "caixa baixa"
# Retirando os acentos
data = [unidecode(x.upper()) for x in data.split(' ') if len(x) > 0]

# Removendo stop words
data = [word for word in data if not word in nltk.corpus.stopwords.words('portuguese')]

# Regex para classificacao de cpf
cpf_regex = re.compile(r'^(\d{3}.){2}\d{3}-\d{2}$')

# Regex para classificacao de email
email_regex = re.compile(r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w+$')

# Constantes criadas apenas para contarmos quantos cpfs e emails foram encontrados
QTD_CPF = 0
QTD_EMAIL = 0

# Para cada palavra na nossa imagem
for x in data:
    # Aplicar regex ede cpf e email
    regex_result_cpf = re.search(cpf_regex, x)
    regex_result_email = re.search(email_regex, x)
    # Se encontramos um cpf somar 1 na nossa contagem de cpf
    if regex_result_cpf:
        QTD_CPF += 1
    # Se encontramos um email somar 1 na nossa contagem de cpf
    if regex_result_email:
        QTD_EMAIL += 1

# Iniciando a keyword research
# lendo nosso arquivo csv contendo nomes
df = pd.read_csv('./files/nomes.csv')

# Selecionando apenas nossa lista de nomes
names = df.group_name.values

# Aplicando keyword research
names = [word for word in data if word in names]

print(f'{QTD_CPF} CPFs encontrados')
print(f'{QTD_EMAIL} E-mails encontrados')
print(f'{len(names)} Nomes encontrados')
