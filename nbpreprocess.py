#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import *
import re
import shutil
import subprocess as sp

# set some subfolder names
source = Path("source")
build = Path("build")
notebooks = Path("notebooks")
templates = Path("templates")

# generator for all standalone files
tex_exts = (".tikz", ".forest")
tex = (f for f in source.glob('**/*') if f.suffix in tex_exts)

# generator for all mdown files
mdown_exts = (".mdown", ".md")
mdown = (f for f in source.glob('**/*') if f.suffix in mdown_exts)

# list of all styling files (list because generator can only be processed once)
style_exts = (".css")
styles = [f for f in templates.glob('**/*') if f.suffix in style_exts]


def change_subfolder(path: Path, subfolder: Path,
                     with_file: bool=False) -> Path:
    return subfolder / Path(*path.parts[1:]) if with_file\
      else subfolder / Path(*path.parts[1:-1])


def mirror_subfolders(path: Path, subfolder: Path) -> None:
    change_subfolder(path, subfolder).mkdir(
            mode=0o755, parents=True, exist_ok=True)


def process_texfile(f: Path) -> None:
    for folder in [build, notebooks]:
        mirror_subfolders(f, folder)

    # where to save pdf, relative path
    pdf = change_subfolder(f, build, with_file=True).with_suffix('.pdf')
    # where to save svg, relative path
    svg = change_subfolder(f, notebooks, with_file=True).with_suffix('.svg')

    # use sp.call so that latexmk gets to finish before we call pdf2svg
    sp.call(["latexmk", "-pdf", "-quiet", str(f.absolute())],
            cwd=str(pdf.parent),  # put compilation files in same subfolder
            stdout=sp.DEVNULL)  # and don't print output to shell
    sp.Popen(["pdf2svg", str(pdf), str(svg)],
             stdout=sp.DEVNULL)


def load_template(file_list: List[str], folder: Path=templates) -> str:
    text = "\n"
    for f in file_list:
        path = folder / Path(f + '.mdown')
        with path.open("r") as template:
            text += template.read()
            text += "\n"
    return text


def regexes(line: str) -> str:
    # replace input tikz/forest by image link to svg
    line = re.sub(r"\\input{([^}]*).(tikz|forest)}",
                  r"![alt text](\1.svg)", line)
    # replace math environments by div containers
    line = re.sub(r"\\begin{([^}]*)}", r"<div class=\1>", line)
    line = re.sub(r"\\end{[^}]*}", r"</div>", line)
    return line


def process_mdfile(f: Path,
                   header: List[str]=[],
                   footer: List[str]=[]) -> None:
    with f.open("r") as text:
        for folder in [build, notebooks]:
            mirror_subfolders(f, folder)
        preproc_path = change_subfolder(f, build, with_file=True)
        preproc = open(str(preproc_path), "w")
        # add header
        if header:
            preproc.write(load_template(header))

        # replace latex by html or markdown
        for line in text:
            preproc.write(regexes(line))

        # add footer
        if footer:
            preproc.write(load_template(footer))

        # clean-up
        preproc.close()

        # run conversion
        target = change_subfolder(
            f, notebooks, with_file=True).with_suffix('.ipynb')
        sp.Popen(["notedown", str(preproc_path), '-o', str(target)],
                 stdout=sp.DEVNULL)

        # copy stylesheets to notebook folder
        for style in styles:
            shutil.copy2(str(style), str(target.parent))


for f in tex:
    process_texfile(f)

for f in mdown:
    process_mdfile(f, header=['loadcss'])
