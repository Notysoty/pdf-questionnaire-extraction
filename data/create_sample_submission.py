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
import pandas as pd
import sys
import re
import json

def dummy_extract_questions(pdf_plain_text: str, tables_as_dict: dict) -> str:
    '''
    Placeholder function for extracting questionnaire items from a PDF
    '''
    predictions = []
    if len(tables_as_dict) > 0:
        if len(tables_as_dict['pageTables']) == 1:
            for table in tables_as_dict['pageTables'][0]:
                for row in table:
                    col = row[0].strip()
                    if re.findall("[a-z]", col):
                        predictions.append("\t" + col)
    if len(predictions) > 0:
        return "\n".join(predictions)
    else:
        for line in pdf_plain_text.split("\n"):
            line = re.sub(r'\s+', ' ', line).strip()
            line = re.sub(r'\n+', '', line)
            line = re.sub(r'^\d+\.?', '', line).strip()
            predictions.append("\t" + line)
    return "\n".join(predictions)


test_files = ["000_mfqchildselfreportshort.txt",
"001_patienthealthquestionnaire.txt",
"004_newyorklongitudinalstudybythom.txt",
"005_beckdepressioninventorybdi.txt",
"006_apadsm5severitymeasurefordepre.txt",
"007_bhrcsselfreportedscared.txt",
"008_gad7anxietyupdated0.txt",
"009_validationoftheportugueseversi.txt",
"011_bhrcsparentreportsocialaptitud.txt",
"012_hrcw2protocolopsicoconfmenor18.txt",
"013_hrcw2protocolopsicoadultos.txt",
"014_testedeansiedadegad7dranadimme.txt",
"015_hrcw1dom.txt",
"016_hrcw2protocolodomiciliarmenor1.txt",
"019_bhrcsparentreportsocialcohesio.txt",
"021_sdqenglishukpt417single.txt",
"023_hrcw1psico.txt",
"024_bhrcsselfreportedmfq.txt",
"026_sf36.txt",
"030_bhrcsselfreportedwarwickedinbr.txt",
"031_ghq12.txt",
"032_bhrcsparentreportsdqchild.txt",
"034_bhrcsparentreportsocialcohesio.txt",
"037_hrcw0dom.txt",
"039_selfmeasuresforlonelinessandin.txt",
"045_mr0510201tb.txt",
"046_borderlinepersonalityscreener.txt",
"047_bhrcsparentreportsdqadult.txt",
"055_beta_retirement.txt",
"062_eoin_no_numbers.txt",
"064_hrcw1psicoconf.txt"]

COMMAND_LINE_PARAM = f"Usage: python create_sample_submission.py train|test"

if len(sys.argv) < 2:
    DATASET = "train"
else:
    DATASET = sys.argv[1]

if DATASET != "train" and DATASET != "test":
    print(COMMAND_LINE_PARAM)
    exit()

if DATASET == "test":
    txt_files_to_process = test_files
    output_file = "submission.csv"
else:
    txt_files_to_process = os.listdir("preprocessed_text")
    output_file = "train_predictions.csv"
all_json_files = set(os.listdir("preprocessed_tables"))

ids = []
predictions = []
for txt_file in txt_files_to_process:
    json_file = re.sub(r'txt$', 'json', txt_file)
    with open("preprocessed_text/" + txt_file, "r") as f:
        file_in_plain_text = f.read()
    if json_file in all_json_files:
        with open("preprocessed_tables/" + json_file, "r") as f:
            file_in_json = f.read()
        tables_as_dict = json.loads(file_in_json)
    else:
        tables_as_dict = {}
    predictions.append(dummy_extract_questions(file_in_plain_text, tables_as_dict))
    ids.append(txt_file)
df = pd.DataFrame()
df["ID"] = ids
df["predict"] = predictions

print ("Writing predictions to", output_file)
df.to_csv(output_file, index=False)
