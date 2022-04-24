import shutil
import sys
import os

"""
Dataset Structure:
images_background
├── Alphabet_of_the_Magi
│   ├── character01
│   │   ├── 0709_01.png
│   │   ├── 0709_01.png
│   │   └── ...
│   ├── character02
│   │   ├── 0710_01.png
│   │   └── ...
│   └── ...
├── Anglo-Saxon_Futhorc
│   ├── character01
│   │   └── ...
│   └── ...
└── ...
"""

data_path_read = sys.argv[1]
data_path_write = sys.argv[2]

for alphabeta in os.listdir(data_path_read):
    alphabeta_path = os.path.join(data_path_read, alphabeta)
    path_write1 = data_path_write[:-2] + '-' + alphabeta
    for charactor in os.listdir(alphabeta_path):
        charactor_path = os.path.join(alphabeta_path, charactor)
        path_write2 = path_write1 + '-' + charactor
        os.makedirs(os.path.join(data_path_write, path_write2))
        for drawer in os.listdir(charactor_path):
            drawer_path = os.path.join(charactor_path, drawer)
            shutil.copyfile(drawer_path, os.path.join(data_path_write, path_write2, drawer))