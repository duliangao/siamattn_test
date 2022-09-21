import os
import shutil

vot = '/data/VOT/VOT2018/'

dirs = [
    dir for dir in os.listdir(vot) if os.path.isdir(os.path.join(vot, dir))
]

for dir in dirs:
    seq = os.path.join(vot, dir, 'color')

    if not os.path.exists(seq):
        os.mkdir(seq)

    files = os.path.join(vot, dir)

    for file in os.listdir(files):
        src = os.path.join(files, file)
        print(src)
        shutil.move(src=src, dst=seq)
