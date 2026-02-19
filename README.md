# CMSE 202 Jupyter Book (Spring 2025)

## Intro

Welcome to the CMSE 202 Jupyter Book repository!

This repository is intended to replace the previous CMSE 202 course website with a Jupyter Book.

## Required Software

### **Jupyter Book**: https://jupyterbook.org/intro.html

Installed with `pip install -U jupyter-book`

#### Important note about Jupyter Book from Fall 2023
It was discovered in Fall of 2023 that using the newest version of Jupyter Book broke many of the self-reference links within things like the Software Setup Guide.  This was fixed by downgrading to version 0.13.2. You can install this version with:

`pip install jupyter-book==0.13.2`

(or, it might be preferable to just set up a separate conda environment for building the book to avoid messing with your Python installation).

### **ghp-import**: https://pypi.org/project/ghp-import/

Installed with `pip install ghp-import`

### Setting up a conda environment (if desired)

You can easily create an environment with all the required packages via 

`conda create -f teaching_conda_env.yaml`

This command will create a conda environment called `cmse202` with all the required packages.


## Contents

`_build` - Jupyter Book build (automatically managed). **DO NOT COMMIT THE CONTENTS OF THIS FOLDER TO THE REPO**.

`course_materials` - Directory containing important course documents that are not assignments (syllabus, software set up guide, etc.).

`daily` - Directory containing the student and instructor versions of pre-class assignments, in-class assignments, and supplementary files.

`section files` - Directory containing the markdown files required to organize the book with collapsible days (files could be moved into `daily` to declutter?).

`_config.yml` - Used to configure Jupyter Book settings. If there are book wide changes to be made they are likely done here. See https://jupyterbook.org/customize/config.html.

`_toc.yml` - Used to manage the content of the Jupyter Book. This is where the structure and files are changed. As a sidenote, the book is currently configured to only build files included in the table of contents without executing. See https://jupyterbook.org/customize/toc.html and https://jupyterbook.org/structure/configure.html.

`index.md` - File used as the website homepage.

`logo.png` - CMSE logo used in the upper left corner of the book and as the favicon. (If moved please update `_config.yml`)

`teaching_conda_env.yaml` - Environment file for conda. See above

### Supplemental RISE Slide Decks

In addition to all of the standard content, there are also a set of slides used by Devin Silvia during the Fall 2023 semester and they are accessible via the `rise-slides` branch of this repo. The slides work with the RISE extension for Jupyter Notebooks. See https://rise.readthedocs.io/en/latest/ for more information. If you want to create PDFs from your slide notebooks, follow the instructions at https://rise.readthedocs.io/en/latest/exportpdf.html.

## Updating the Jupyter Book

**Step 1** - Make some awesome changes

**Step 2** - Build the book

Execute the following command in the root directory of the repository to clean the existing build:

`jupyter-book clean .`

(you can also use the short-hand "`jb`" in place of "`jupyter-book`")

Execute the following command in the root directory of the repository to rebuild the book with updated content:

`jupyter-book build .`

(or, as indicated above, `jb build .`)

See https://jupyterbook.org/basics/build.html.

**Step 3** - Upload the book

Execute the following command in the root directory of the repository to push a branch to the repository that will host the book in GitHub Pages:

`ghp-import -n -p -f _build/html`

See https://jupyterbook.org/publish/gh-pages.html.



---
[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://jupyterbook.org/intro.html)
