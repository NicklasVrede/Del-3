import os

def set_wd():
    current_dir = os.path.dirname(__file__)
    os.chdir(current_dir)