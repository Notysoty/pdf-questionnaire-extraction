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

# Convert all PDFs in folder to tables using RonnyWang library.

import os
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://ronnywang.github.io/pdf-table-extractor/")
file_upload = driver.find_element(By.XPATH, value='//input[@id="pdf-file"]')

sleep(2)

input_folder = os.getcwd() + "/raw_pdfs"
output_folder_tables = "preprocessed_tables"

try:
    os.stat(input_folder)
except:
    print("Please place the PDFs in ", input_folder)

try:
    os.stat(output_folder_tables)
except:
    os.mkdir(output_folder_tables)

for root, folder, files in os.walk(input_folder):
    for file_name in files:
        if not file_name.endswith("pdf"):
            continue
        full_file = input_folder + "/" + file_name
        print(full_file)

        file_upload.send_keys(full_file)

        sleep(5)

        parse_result_element = driver.find_element(By.XPATH, value='//textarea[@id="json-result"]')
        parse_result_json = parse_result_element.get_attribute("value")

        if "Parsing PDF, progress" in parse_result_json:
            for ctr in range(4):
                sleep(5)
                parse_result_json = parse_result_element.get_attribute("value")
                if "Parsing PDF, progress" not in parse_result_json:
                    break

        output_file = output_folder_tables + "/" + re.sub(r"\.(?:pdf|docx?)$", ".json", file_name)
        with open(output_file, 'w', encoding="utf-8") as fo:
            fo.write(parse_result_json)
