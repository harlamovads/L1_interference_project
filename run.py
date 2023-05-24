!pip install "spacy~=3.4.0"
!pip install spacy-transformers==1.2.1
import spacy
from spacy import displacy

text = '' #в переменную text надо передать текст для разбора
nlp1 = spacy.load('path-to-model') #надо вставить путь к скачанной с Google Disk папке
doc = nlp1(text)
displacy.render(doc, style='span', jupyter=True)
