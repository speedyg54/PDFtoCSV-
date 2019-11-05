#.py
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:03:31 2019

@author: OBar

Script Purpose: parse pdfs and convert them to txt files.
"""

from tika import parser
import os
import pandas as pd


root = ''
tgt_dir = root + ''
out_dir = root + ''


dir_list = os.listdir(tgt_dir)

for idx, i in enumerate(dir_list):
    path = tgt_dir + dir_list[idx].replace("'",'')
    print('This is the current path \n{}\n'.format(path))
    if path.find('.pdf') == -1:
        continue
    
    pdfFileObj = parser.from_file(path)
    text_list = pdfFileObj["content"].split('\n')
    text_list2 = [j for j in text_list if j] #removes null rows
    outp = pd.Series(text_list2)
    outp.to_csv(out_dir + '{}'.format(dir_list[idx]) + '.csv', index=False)