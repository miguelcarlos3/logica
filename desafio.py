import os 
import json
from datetime import datetime
from collections import Counter

print (os.getcwd())

with open("test1","r") as arquivo:
    dados = json.load(arquivo)
 
resultado = sum(map(int,dados))
print (resultado)

with open ("test2_text1.txt","r", encoding="utf-8") as arquivo:
    texto1 = arquivo.read()
    
with open ("test2_text2.txt","r", encoding="utf-8") as arquivo:
    texto2 = arquivo.read()
caracteres1 = Counter(texto1)
caracteres2 = Counter(texto2)
if caracteres1 == caracteres2:
    print("Os arquivos possuem os mesmos caracteres.")
else:
    print("Os arquivos possuem caracteres diferentes.")

