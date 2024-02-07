![The Harmony Project logo](https://raw.githubusercontent.com/harmonydata/brand/main/Logo/PNG/%D0%BB%D0%BE%D0%B3%D0%BE%20%D1%84%D1%83%D0%BB-05.png)

<a href="https://harmonydata.ac.uk"><span align="left">🌐 harmonydata.ac.uk</span></a>
<a href="https://www.linkedin.com/company/harmonydata"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/linkedin.svg" alt="Harmony | LinkedIn" width="21px"/></a>
<a href="https://twitter.com/harmony_data"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/x.svg" alt="Harmony | X" width="21px"/></a>
<a href="https://www.instagram.com/harmonydata/"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/instagram.svg" alt="Harmony | Instagram" width="21px"/></a>
<a href="https://www.facebook.com/people/Harmony-Project/100086772661697/"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/fb.svg" alt="Harmony | Facebook" width="21px"/></a>
<a href="https://www.youtube.com/channel/UCraLlfBr0jXwap41oQ763OQ"><img align="left" src="https://raw.githubusercontent.com//harmonydata/.github/main/profile/yt.svg" alt="Harmony | YouTube" width="21px"/></a>

 [![Harmony on Twitter](https://img.shields.io/twitter/follow/harmony_data.svg?style=social&label=Follow)](https://twitter.com/harmony_data) 


# Harmony PDF extraction

<!-- badges: start -->
[![PyPI package](https://img.shields.io/badge/pip%20install-harmonydata-brightgreen)](https://pypi.org/project/harmonydata/) ![my badge](https://badgen.net/badge/Status/In%20Development/orange) [![License](https://img.shields.io/github/license/harmonydata/harmony)](https://github.com/harmonydata/harmony/blob/main/LICENSE)
[![tests](https://github.com/harmonydata/harmony/actions/workflows/test.yml/badge.svg)](https://github.com/harmonydata/harmony/actions/workflows/test.yml)
[![Current Release Version](https://img.shields.io/github/release/harmonydata/harmony.svg?style=flat-square&logo=github)](https://github.com/harmonydata/harmony/releases)
[![pypi Version](https://img.shields.io/pypi/v/harmonydata.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/harmonydata/)
 [![version number](https://img.shields.io/pypi/v/harmonydata?color=green&label=version)](https://github.com/harmonydata/harmony/releases) [![PyPi downloads](https://static.pepy.tech/personalized-badge/harmonydata?period=total&units=international_system&left_color=grey&right_color=orange&left_text=pip%20downloads)](https://pypi.org/project/harmonydata/)
[![forks](https://img.shields.io/github/forks/harmonydata/harmony)](https://github.com/harmonydata/harmony/forks)
[![docker](https://img.shields.io/badge/docker-pull-blue.svg?logo=docker&logoColor=white)](https://hub.docker.com/r/harmonydata/harmonywithtika)


# How PDFs are extracted

Harmony relies on two libraries to extract questionnaire items from PDFs:

1. Apache Tika - to get plain text
2. [PDF Table Extractor](https://github.com/ronnywang/pdf-table-extractor) Node.js library by Ronny Wang - to get tabular data

This repo contains the training scripts.

# Preprocessing all the PDFs

Some raw PDFs have been provided.

1. Install all the requirements: `pip install -r requirements.txt`
2. Download and start Apache Tika in a command line: `java -jar tika-server-standard-2.8.0.jar`
3. In folder `notebooks`, run `python preprocess_pdf_to_text.py`
4. In folder `notebooks`, run `python preprocess_pdf_to_tables.py`

This will populate `data/preprocessed_text` and `data/preprocessed_tables`, which can be used to train the model.

## ‎😃💁 Who worked on Harmony?

Harmony is a collaboration project between [Ulster University](https://ulster.ac.uk/), [University College London](https://ucl.ac.uk/), the [Universidade Federal de Santa Maria](https://www.ufsm.br/), and [Fast Data Science](http://fastdatascience.com/).  Harmony is funded by [Wellcome](https://wellcome.org/) as part of the [Wellcome Data Prize in Mental Health](https://wellcome.org/grant-funding/schemes/wellcome-mental-health-data-prize).

The core team at Harmony is made up of:

* [Dr Bettina Moltrecht, PhD](https://profiles.ucl.ac.uk/60736-bettina-moltrecht) (UCL)
* [Dr Eoin McElroy](https://www.ulster.ac.uk/staff/e-mcelroy) (University of Ulster)
* [Dr George Ploubidis](https://profiles.ucl.ac.uk/48171-george-ploubidis) (UCL)
* [Dr Mauricio Scopel Hoffmann](https://ufsmpublica.ufsm.br/docente/18264) (Universidade Federal de Santa Maria, Brazil)
* [Thomas Wood](https://freelancedatascientist.net/) ([Fast Data Science](https://fastdatascience.com))

## 📜 License

MIT License. Copyright (c) 2023 Ulster University (https://www.ulster.ac.uk)

## 📜 How do I cite Harmony?

McElroy, E., Moltrecht, B., Ploubidis, G.B., Scopel Hoffman, M., Wood, T.A., Harmony [Computer software], Version 1.0, accessed at https://harmonydata.ac.uk/app. Ulster University (2023)
