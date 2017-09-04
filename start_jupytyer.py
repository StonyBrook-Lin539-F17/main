#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess as sp

my_env = os.environ.copy()
my_env["JUPYTER_CONFIG_DIR"] = "./jupyter/"
notebook_dir = "./notebooks/"
sp.call(["jupyter", "notebook", "--notebook-dir=", notebook_dir], env=my_env)
