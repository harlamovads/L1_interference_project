# L1_interference_project
В данном репозитории находятся материалы, относящиеся к курсовой работе на тему "Методы идентификации ошибок под влиянием интерференции с родным русским языком в учебных текстах на английском языке: анализ эффективности обучения нейросети"

Ссылки на модели, разработанные в рамках работы:
Пять трансформеров:
 - https://huggingface.co/Zlovoblachko/L1_Copying_expression
 - https://huggingface.co/Zlovoblachko/L1_Synonyms
 - https://huggingface.co/Zlovoblachko/L1_Tense_semantics
 - https://huggingface.co/Zlovoblachko/L1_Transliteration
 - https://huggingface.co/Zlovoblachko/L1_Word_form_transmission

Единая модель:
 - https://huggingface.co/Zlovoblachko/L1_Interference_6Tags

Для получения доступа к моделям необходимо быть зарегистрированным на сайте huggingface.co. В случае отсутствия регистрации можно загрузить модели с Google Disk:

Пять трансформеров (внутри папки можно выбрать одну из двух моделей: последнюю (model-last) или с наивысшим f-score (model-best). В тексте работы приведены результаты по model-best).

 - https://drive.google.com/drive/folders/10dqFG0AYhsug9aTz4y1bBBck0dbRCZWI?usp=drive_link
 - https://drive.google.com/drive/folders/13rBqFXdF16KlYdjIhEke_gG41ZKEcE9U?usp=drive_link
 - https://drive.google.com/drive/folders/12qWimObQhEvDxaF3EjqekCCtkxm3Rrfb?usp=drive_link
 - https://drive.google.com/drive/folders/16wxgKjBAbr-xeCuXGkTbzsgM_A15Hyt0?usp=drive_link
 - https://drive.google.com/drive/folders/158yK3F4TVRZlFbKinEMI3u9lcv5YEZYz?usp=drive_link

Единая модель:
 - https://drive.google.com/drive/folders/1WdDd03mELjyf6kOu-0jtWgELlheDJrPn?usp=drive_link

После этого можно использовать модели для анализа текста, исполнив в редакторе типа jupyter код из файла run.py.
