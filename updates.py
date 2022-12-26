#!/bin/env python3
import os

# add your git folders that will 
git_folders = [
        '/home/user/software/my-scripts',
]

cmds = [
    'rustup update',
]

for folder in git_folders:
    print(f'% cd {folder}')
    os.chdir(folder)
    print(f'% git pull')
    os.system('git pull')
    print()

for cmd in cmds:
    print('%', cmd)
    os.system(cmd)
    print()
