from docx import Document
from docxcompose.composer import Composer
import os
import glob
import sys

#cambiar por tu directorios donde esten los .docx
OUTPUT_PATH = '.\Ouputs'
files_list = glob.glob(OUTPUT_PATH+'\\'+'*.docx')
#tu archivo final tendra el nombre de
composed = ".\Final.docx"

result = Document(files_list[0])
result.add_page_break()
composer = Composer(result)

for i in range(1, len(files_list)):
	
    doc = Document(files_list[i])

    if i != len(files_list) - 1:
        doc.add_page_break()

    composer.append(doc)

composer.save(composed)