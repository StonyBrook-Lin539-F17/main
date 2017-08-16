#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess as sp

my_env = os.environ.copy()
my_env["JUPYTER_CONFIG_DIR"] = "./jupyter/"
sp.Popen(["jupyter", "notebook"], env=my_env)
