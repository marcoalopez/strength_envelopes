![header](https://raw.githubusercontent.com/marcoalopez/strength_envelopes/master/figures/header.webp)

_This project is maintained by [Marco A. Lopez-Sanchez](https://marcoalopez.github.io/)_ - Last update: 2023-11-14  

**Strength envelopes** is a series of free open-source multi-platform [Jupyter notebooks](https://jupyter.org/) aimed at building strength envelopes for the earth's lithosphere. The notebooks are primarily intended for educational purposes (hands-on courses) but are easily adaptable for more advanced modelling. The programming language used is [Python](https://www.python.org/) but **no prior knowledge of Python is required for use**. All the notebooks are intended to be self-explanatory and with a smooth learning curve.

> **Disclaimer**: The project is currently under development. As a pet project, I develop it in my spare time and without specific deadlines. Stay tuned in https://fediscience.org/@marcoalopez 

## The notebooks
To visualize the content of the notebooks as a website just click on the topic you are interested in (the list may increase or decrease without notice over time)

- [Python basics](https://deepnote.com/viewer/github/marcoalopez/strength_envelopes/blob/master/notebooks/Python_basics.ipynb) (status: _in progress_)
- [Brittle faults (part 1): understanding shear fractures](https://nbviewer.org/github/marcoalopez/strength_envelopes/blob/master/notebooks/brittle_faults.ipynb) (status: _in progress_)
- [Brittle faults (part 2): the role of pore pressure]() (status: TODO)
- [Brittle faults (part 3): the Anderson model](https://nbviewer.org/github/marcoalopez/strength_envelopes/blob/master/notebooks/brittle_faults_2.ipynb) (status: _in progress_)
- [Estimate a stable geotherm](https://nbviewer.org/github/marcoalopez/strength_envelopes/blob/master/notebooks/stable_geotherm.ipynb) (status: _mostly done_)
- [A gentle introduction to flow laws and power-law creep](https://nbviewer.org/github/marcoalopez/strength_envelopes/blob/master/notebooks/creep_flow_laws.ipynb) (status: _in progress_)
- [Power-law creep envelopes (part 1)]() (status: TODO)
- [Power-law creep envelopes (part 2)]() (status: TODO)
- [Estimate a full lithosphere strength envelope](https://nbviewer.jupyter.org/github/marcoalopez/strength_envelopes/blob/master/notebooks/Full_strength_envelope.ipynb?flush_cache=true) (status: TODO)

## What is a Jupyter notebook and how to use it?

A Jupyter notebook is a document that supports mixing executable code ( **Ju**lia, **Pyt**hon, **R**, etc.), equations, visualizations, and narrative text, known as [literate computing](https://osf.io/h9gsd/). There are two main options to interact with a Jupyter notebook:

- Open the notebook locally on your computer, i.e. the notebook is stored on your hard disk. This is the fastest way to open and interact with a notebook and always have access to it. This requires, however, installing a Python distribution that includes Jupyter and several Python scientific libraries (see _Requirements & Python installation_ below) and download the notebooks. _A link to download all the notebooks available soon!_
- Open the notebook on remote servers as a web application (e.g. in [mybinder.org](https://mybinder.org/) or [Google Colab](https://colab.research.google.com/)). The process of loading the notebook in this way can be quite slow, depending on its size, but it has the advantage of requiring nothing more than a browser and an internet connection. _More details on this modality coming soon!_

Lastly, there are exceptional Jupyter notebook video tutorials on the web (others not so much). For example, this one: https://www.youtube.com/watch?v=HW29067qVWk

> 🚨**Are you an educator interested in using Jupyter notebooks as an educational tool?** Check the superb free book [Teaching and Learning with Jupyter](https://jupyter4edu.github.io/jupyter-edu-book/).

## Requirements & Python installation

A popular software distribution that includes the Jupyter notebook is the [Anaconda distribution (individual edition)](https://www.anaconda.com/products/individual), which is free, includes all the necessary scientific packages (> 5 GB disk space), and is ready to install on Windows, Mac, and Linux. Pick the installer with the newest version of Python and voila! Another option is to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html), which is a free minimal Python & Conda installation. If you are not sure whether you should install it, read [this](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda). If you installed Miniconda, open the _Anaconda prompt_ and use the following command to install the minimum necessary dependencies to interact locally with the notebooks.

```shell
>>> conda install numpy scipy pandas matplotlib jupyterlab 
```

Jupyter notebooks can be launched by open the Anaconda navigator (if you installed Anaconda) and launching the _Jupyter lab_ (preferred option) or the _Jupyter notebook_ or, more quickly, from the terminal (_Anaconda prompt_) typing ``jupyter lab`` or  ``jupyter notebook``. Then, you'll see the application opening in your browser. If you prefer a standalone application to interact with the notebooks you can install https://code.visualstudio.com/ and add the *Python* and *Jupyter* plug-ins.

## How to contribute to this project?

The GitHub website hosting the project provides several options (you will need a GitHub account, it’s free!):

- Open a [discussion](https://github.com/marcoalopez/strength_envelopes/discussions): This is a place to:
  - Ask questions you are wondering about.
  - Share ideas.
  - Engage with the developers (still just me).
- Open and [issue](https://github.com/marcoalopez/strength_envelopes/issues): This is a place to track bugs or requests for specific features on the notebooks.
- Create a [pull request](https://github.com/marcoalopez/strength_envelopes/pulls): You modified, corrected or added a feature to one of the notebooks and send it for one of the developers to review it and add it to the main page.

For a quick explanation see https://www.youtube.com/watch?v=R8OAwrcMlRw. Besides, if you want to contribute to the project, you might want to glimpse at the [code of conduct](https://github.com/marcoalopez/strength_envelopes/blob/master/CODE_OF_CONDUCT.md) (TLDR: be nice to others 😉).  



---

*Copyright © 2023 Marco A. Lopez-Sanchez*  

_Information presented on this website and the notebooks is provided without any express or implied warranty and may include technical inaccuracies or typing errors; the author reserve the right to modify or enhance the content of this website as well as the notebooks at any time without previous notice. This webpage and the notebooks are not liable for the content of external links. Notebook contents under [Creative Commons Attribution license CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) and codes under [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/)._

_Hosted on GitHub Pages — This website was created with [Typora](https://typora.io/)_