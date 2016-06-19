# -*- coding: utf-8 -*-

import os

CONST_PATH_FILE = 'gleilson.txt'

def delete(path):
    if os.path.isfile(path):
        os.remove(path)