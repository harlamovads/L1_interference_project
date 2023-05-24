!pip install "spacy~=3.4.0"
!pip install spacy-transformers==1.2.1
import spacy
from spacy import displacy

text = '' #в переменную text надо передать текст для разбора
nlp1 = spacy.load('path-to-model') #надо вставить путь к одной из двух моделей в скачанной с Google Disk папке, например, /content/drive/MyDrive/general_model/model-best
doc = nlp1(text)
displacy.render(doc, style='span', jupyter=True)
