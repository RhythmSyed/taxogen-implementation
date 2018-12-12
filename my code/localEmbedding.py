# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 08:11:48 2018

@author: gaoha
"""

import os
import subprocess

input_f = 'text.txt'
output_f = 'embeddings.txt'
print(input_f)
print(output_f)

canshu = "word2vec.exe " + "-threads" + " " + "1" + " " + "-train" + " " + input_f + " " + "-output" + " " + output_f

print(canshu)

os.system(canshu)
#subprocess.run(["./word2vec.exe", "-threads", "1", "-train", input_f, "-output", output_f])