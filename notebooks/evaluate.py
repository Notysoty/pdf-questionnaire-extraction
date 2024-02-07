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
import sys

import numpy as np

COMMAND_LINE_PARAM = f"Usage: python evaluate.py MODEL_NO\n\twhere MODEL_NO could be 00, 01, etc"

if len(sys.argv) != 2:
    print(COMMAND_LINE_PARAM)
    exit()

MODEL_NO = sys.argv[1]

precisions = []
recalls = []

total_num_intersections = []
total_num_predictions = []
total_num_ground_truths = []

for file_name in os.listdir("../data/annotations/"):
    ground_truth_file = f"../data/annotations/{file_name}"
    predictions_file = f"output/{MODEL_NO}/{file_name}"
    ground_truths = []
    with open(ground_truth_file, "r", encoding="utf-8") as f:
        for l in f:
            l = re.sub(r'\n', '', l)
            c = l.split("\t")
            ground_truths.append(re.sub(r'\W', '', c[1]))
    predictions = []

    if not os.path.exists(predictions_file):
        print("\tmissing", predictions_file)
        continue
    with open(predictions_file, "r", encoding="utf-8") as f:
        for l in f:
            l = re.sub(r'\n', '', l)
            if l == "" or l == " ":
                continue
            c = l.split("\t")
            predictions.append(re.sub(r'\W', '', c[1]))

    size_of_intersection = len(set(ground_truths).intersection(set(predictions)))
    if len(predictions) > 0:
        precision = size_of_intersection / len(set(predictions))
    else:
        precision = 0
    if len(ground_truths) > 0:
        recall = size_of_intersection / len(set(ground_truths))
    else:
        recall = 0
    print(f"Precision = {precision:.2f}, recall = {recall:.2f}\t{file_name}")

    precisions.append(precision)
    recalls.append(recall)

    total_num_intersections.append(size_of_intersection)
    total_num_predictions.append(len(set(predictions)))
    total_num_ground_truths.append(len(set(ground_truths)))

precision = np.mean(precisions)
recall = np.mean(recalls)
print(f"Mean precision = {precision:.2f}, mean recall = {recall:.2f}")
precision = np.sum(total_num_intersections) / np.sum(total_num_predictions)
recall = np.sum(total_num_intersections) / np.sum(total_num_ground_truths)
print(f"\tPrecision over all instances = {precision:.2f}, recall over all instances = {recall:.2f}")
