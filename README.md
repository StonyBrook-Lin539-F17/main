Mathematical Methods in Linguistics
===================================


**Attention:** To get access to the [private course repository][private], you must email me your github username. 

**A friendly plug:** If you are interested in this class, also consider attending the department's [Mathematical Linguistics Reading Group](http://complab-stonybrook.github.io/mlrg/).

Course Outline
--------------

This course is an introduction to mathematics in linguistics.
It aims to help students familiarize themselves with mathematical concepts and applications that are widely relevant to theoretical and\slash or computational linguistics. 
This covers a wide range of topics, mostly from *discrete mathematics*.
The course is also very different from what you did in high school, there's precious few numbers here and we don't care much about integrals or calculating compound interest.
In contrast to a proper mathematics course, we also focus more on techniques and tools rather than theorems and proofs.
This means that you will learn how to work with things like matrices, semirings, and lattices, but you won't have to prove things about them.
So this is more like a CS methods course than a proper math class.

For more information about the content, see the syllabus.

Using the Lecture Notes
-----------------------

The lecture notes are made available as [Jupyter notebooks](http://jupyter.org/) in the [main github repository](https://github.com/StonyBrook-Lin539-F17/main).
A Jupyter notebook is a mixture of text and Python code, which allows for a more interactive learning environment.
There are multiple ways you can view the notebooks:

1.  Use Stony Brook's [Virtual SINC site](https://it.stonybrook.edu/services/virtual-sinc-site), which already has Jupyter installed. 
1.  Use our virtual machine image for VirtualBox, available at Stony Brook's [Softweb](https://softweb.cc.stonybrook.edu/).
1.  Install [Anaconda](https://www.continuum.io/downloads), a Python distro that also installs Jupyter.
1.  If you already have a working Python setup, install Jupyter separately.
1.  If you can live without the interactive Python demonstrations, you can just read the notebooks directly on github.

For all options except the last one, you should use the supplied `start_jupyter.py` script to start the Jupyter server.
Proceed as follows:

1.  Clone or download the git repository (green button at the top of the page).
1.  If you downloaded the repository as a zip archive, extract it.
1.  Run the `start_jupyter.py` script.
    The Jupyter notebook server will start and open a new tab in your browser.
1.  Navigate to the notebook you want to read.
    They are all in the notebooks folder.


Link List
---------

### Using git

I recommend that you clone this repository to your computer and issue `git pull -s recursive -X theirs` on a regular basis to keep your clone up-to-date.

- Our department's [git tutorial](https://github.com/CompLab-StonyBrook/git_training)
- [Github app for Windows](http://windows.github.com); supports only Windows 7 or later
- [Github app for Mac](http://mac.github.com); supports only OS X 10.9 or later
- List of alternative [GUI clients for git](http://git-scm.com/downloads/guis)
- Tutorials for using [git via the command line](https://www.atlassian.com/git/tutorials)
- Official [documentation for git](http://git-scm.com/doc)


### Markdown

You can use Markdown syntax when authoring github issues or wiki entries.

- Interactive tutorial to [markdown basics](http://markdowntutorial.com/)
- [Complete markdown syntax](http://daringfireball.net/projects/markdown/syntax)
- Overview of [Github's markdown dialect](https://help.github.com/categories/writing-on-github/)


### LaTeX

If you need to write mathematical formulas, use LaTeX commands, e.g. `$f(x) = \frac{x}{2}$` to typeset the fraction.

- [Overleaf](https://www.overleaf.com/) (formerly writeLaTeX) is an online LaTeX editor with live preview
- List of [commonly used math symbols](http://web.ift.uib.no/Teori/KURS/WRK/TeX/symALL.html)
- Andrew Roberts' [Getting to Grips with LaTeX](http://www.andy-roberts.net/writing/latex)


### Python

The notebooks contain Python code that you can run and edit on your own.
This way you can check some of your own calculations with Python or play around with parameters to see how they affect the output of a computation.

- A succinct yet extensive [tutorial for Python 3](http://www.python-course.eu/python3_course.php)
- The official [Python 3 documentation](https://docs.python.org/3/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) is an excellent introduction that covers the basics of Python and applies them to real-world tasks.


[private]: ../../../private
