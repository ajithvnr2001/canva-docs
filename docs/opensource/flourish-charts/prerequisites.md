---
url: https://www.canva.dev/opensource/flourish-charts/prerequisites/
title: Set up Flourish Charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:58.515166+00:00
---

# Set up Flourish Charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/prerequisites/

Getting started

[Overview](https://www.canva.dev/opensource/flourish-charts/)[Set up Flourish Charts](https://www.canva.dev/opensource/flourish-charts/prerequisites/)[Creating Flourish graphs](https://www.canva.dev/opensource/flourish-charts/quickstart/)[Extending the Flourish base visualization ID](https://www.canva.dev/opensource/flourish-charts/base-visualization-id/)[Changelog](https://www.canva.dev/opensource/flourish-charts/changelog/)

API reference

[Flourish](https://www.canva.dev/opensource/flourish-charts/api/flourish/)[flourish-api-documentation](https://www.canva.dev/opensource/flourish-charts/api/flourish-api-documentation/)[gapminder](https://www.canva.dev/opensource/flourish-charts/api/gapminder/)

Binding additional data sources

Add extra details to charts

# Set up Flourish Charts

Copy page

Getting started with Flourish Charts requires downloading from PyPi or CRAN (or alternatively, our GitHub repository) and setting up a Flourish API key.

## Python package installation

If installing to a virtual environment, you can install Flourish Charts using `pipenv`:
    
    
    pipenv install flourishcharts

SH

Copy

If using a local machine Python installation, install Flourish Charts to your global Python installation with `pip`:
    
    
    python3 -m pip install --upgrade flourishcharts

SH

Copy

## R package installation

To install from CRAN, run:
    
    
    install.packages("flourishcharts")

R

Copy

To install the latest R package version from GitHub (as the CRAN package will only be updated on a quarterly basis instead of every two weeks):
    
    
    remotes::install_github("canva-public/flourishcharts", subdir = "R_package")

R

Copy

## Flourish API key

The Flourish Charts package is dependent on the Flourish Live API, an enterprise bolt-on allowing users to programatically create Flourish visualizations. To use this package, you must have access to the API.

PythonPython

RR

  1. The first step is to create an API key. This can be generated from your Flourish [account page⁠(opens in a new tab or window)](https://app.flourish.studio/settings).

  2. Python users can store their Flourish API key in one of the three potential places:

     * Inside the `Flourish()` function, which has a parameter called `api_key`. Pass a string to this argument.
     * If you install a global copy of the package: in a `~/.zshrc` or `~/.bashrc` file where you can store sensitive bits of information or, alternatively, information you want accessible. This is safer as the API key cannot be accessed if you decide to share the Python file containing Flourish Charts code.
     * If you install to a virtual environment: in a `.envrc` file where you can store sensitive bits of information or, alternatively, information you want accessible every time you run Python code within the environment. This is safer as the information cannot be accessed if you decide to share the Python file containing Flourish Charts code.

If you choose one of the latter two options, store your key in the file as follows:
    
    export FLOURISH_API_KEY="..."

SH

Copy

  3. Restart your terminal after saving the variable for it to take effect or (if using a virtual environment) run `direnv allow` in your directory.




  1. The first step is to create an API key. This can be generated from your Flourish [account page⁠(opens in a new tab or window)](https://app.flourish.studio/settings).

  2. R users can store their Flourish API key in one of two places:

     * Inside the `flourish()` function which has a parameter called `api_key`. Pass a string to this argument.
     * In your `~/.Renviron` file where you can store sensitive bits of information or, alternatively, information you want available every time you run R code. This is safer as the API key cannot be accessed if you decide to share the R file containing Flourish Charts code.

If you choose the latter, please store your key in the file as follows:
    
    FLOURISH_API_KEY="..."

Copy

The `flourish()` function will recognize this variable, grabbing the API key without the end-user needing to specify every single time.

  3. If you do not have an `~/.Renviron` file, create one from your terminal by running `touch ~/.Renviron && open ~/.Renviron`.

  4. Restart R after saving the variable for it to take effect.



