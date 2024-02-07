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

# BEFORE RUNNING THIS FILE, DOWNLOAD AND RUN APACHE TIKA ON YOUR COMPUTER
# e.g. java -jar tika-server-standard-2.8.0.jar 


import os
import re

from lxml import html
from tika import parser

input_folder = "raw_pdfs"
output_folder_text = "preprocessed_text"

try:
    os.stat(input_folder)
except:
    print("Please place the PDFs in ", input_folder)

try:
    os.stat(output_folder_text)
except:
    os.mkdir(output_folder_text)


def extract_text_from_pdf(file_path):
    parsed = parser.from_file(file_path, xmlContent=True)
    parsed_xml = parsed["content"]

    et = html.fromstring(parsed_xml)
    pages = et.getchildren()[1].getchildren()

    return [str(page.text_content()) for page in pages]


for root, folder, files in os.walk(input_folder):
    for file_name in files:
        if not file_name.endswith("pdf") and not file_name.endswith("docx"):
            continue
        full_file = input_folder + "/" + file_name
        print(full_file)

        try:
            texts = extract_text_from_pdf(full_file)
        except:
            print("Error processing", full_file, ". Skipping")
            continue

        output_file = output_folder_text + "/" + re.sub(r"\.(?:pdf|docx?)$", ".txt", file_name)
        with open(output_file, 'w', encoding="utf-8") as fo:
            for t in texts:
                fo.write(t + "\n")
