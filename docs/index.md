# HEAL Data Utilities

The HEAL Data Utilities python package provides data packaging tools for the HEAL Data Ecosystem to facilitate data discovery, sharing, and harmonization on the [HEAL Platform](https://healdata.org).
 
Currently, the focus of this repository is generating standardized variable level metadata (VLMD) in the form of data dictionaries. See the [quick start section](#quick-start) to get started without installing any of the prerequisites. ([Click here](./vlmd/index.md) for the Variable-level Metadata documentation section).

However, in the future, this will be expanded for all HEAL-specific data packaging functions (e.g., study- and file-level metadata and data).

!!! important

    See the README for the HEAL VLMD specifications, conventions, and rules [here](https://github.com/HEAL/heal-metadata-schemas/tree/main/variable-level-metadata-schema#readme). The `vlmd` tool is intended to be an implementation of these specifications. 

## Quick start

!!! note

    If using the quick start option, no prerequisites are required.

**Double click** on the `vlmd` (or `vlmd.exe`) executable or **run** the `vlmd` executable without any arguments to quickly start using this tool. This "quick start" will take walk you through step by step by prompting you of the various options.

!!! important

    Stand alone applications for different operating systems are available [here](https://github.com/HEAL/healdata-utils/releases/latest). These allow you to run the `vlmd` tool without
    needing to install anything else. Just (1) download (by clicking on your computer's operating system), (2) unzip, and (3) double click on the `vlmd` application icon.


## Prerequisites

### Python

While the HEAL Data Utilities should be compatible with most versions of Python, you can download the latest version of Python [here](https://www.python.org/downloads/) and install it on your local computer. We recommend installing Python version 3.10.

## Installation

To install the latest official release of healdata-utils, from your computer's command prompt, run:

`pip install healdata-utils`

OR for the most up-to-date unreleased version run: 

`pip install git+https://github.com/norc-heal/healdata-utils.git`

!!! note

    Installing the unreleased version requires having [`git` software
    installed](https://git-scm.com/downloads).

