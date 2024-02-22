'''
MIT License

Copyright (c) 2023 Ulster University (https://www.ulster.ac.uk).
Project: Harmony (https://harmonydata.ac.uk)
Maintainer: Thomas Wood (https://fastdatascience.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

import os
import re
from harmony.schemas.requests.text import RawFile, Instrument
from harmony.parsing.pdf_parser import convert_pdf_to_instruments


MODEL_NO = "02"

output_folder = "output/" + MODEL_NO

try:
    os.stat(output_folder)
except:
    os.mkdir(output_folder)

for file_name in os.listdir("../data/annotations/"):
    orig_file = "../data/preprocessed_text/" + file_name
    with open(orig_file, "r", encoding="utf-8") as f:
        file_contents = f.read()
    raw_file = RawFile(file_name="test", text_content=file_contents, tables= [], file_type="pdf", content=file_contents)
    instruments = convert_pdf_to_instruments(raw_file)
      
    with open(f"output/{MODEL_NO}/" + file_name, "w", encoding="utf-8") as fo:            
        for instr in instruments:
             for question in instr.questions:
                 fo.write(str(question.question_no) + "\t" + question.question_text + "\t" + "/".join(question.options) + "\n")
