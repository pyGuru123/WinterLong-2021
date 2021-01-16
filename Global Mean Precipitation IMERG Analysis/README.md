# Global Mean Precipitation Visualization with NASA IMERG Data

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

IMERG, the Integrated Multi-satellitE Retrievals for GPM, is a unified satellite precipitation product produced by NASA to estimate surface precipitation over most of the globe. With IMERG, precipitation estimates from the GPM core satellite are used to calibrate precipitation estimates from microwave and IR sensors on other satellites. By then merging the estimates from multiple satellites, surface precipitation maps can be produced half-hourly at 0.1o horizontal resolution.

## Aim & Observations

Reading and visualizing Integrated Multi-satellitE Retrievals for Global Precipitation Measurement (GPM) missions dataset using Python

The case study is divied into 4 parts:

1. Downloading & Reading hdf5 data with h5py package.
2. Processing datasets
3. Visualizing global mean precipitation for Globe
4. Visualizing global mean precipitation for India

![Alt text](GPM_3IMERGP_WORLD.png?raw=true "GPM IMERG WORLD")

## Dataset 

There are two ways to download the dataset

First way : The Hard way

1. Downloading from NASA Earth Data website for which an account is required at Earth Data website. One can register for a free account from here : [EarthData](https://uui-test.gesdisc.eosdis.nasa.gov/uui/data-access)
2. Once registered, follow the steps at [this page](https://urs.earthdata.nasa.gov/approve_app?client_id=e2WVk8Pw6weeLUKZYOxvTQ) to authorize NASA GESDISC DATA ARCHIVE
3. Click this link to reach official dataset page  : [GPM IMERG DATASET](https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGM.06/)
4. Select year for which you want the dataset for.
5. Download the dataset by clicking the appropriate month hdf5 file link.
6. The file used here has following name : 	*3B-MO.MS.MRG.3IMERG.20200701-S000000-E235959.07.V06B.HDF5*. Here 07.V06B states that its the file for July month

Second way : Easy way \
I have already provided the dataset used in this notebook in the github repo.


## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following packages :-
* Numpy
* Matplotlib
* h5py

```bash
pip install Numpy
pip install Matplotlib
pip install h5py
```

To install cartopy using pip, follow this tutorial

[install cartopy on win10](https://youtu.be/PGNzs1I6tf0)


To make most out of this project run it in google colab

## How to Download

Download this project from here [Download GPM IMERG ANALYSIS](https://downgit.github.io/#/home?url=https://github.com/pyGuru123/Data-Analysis-and-Visualization/tree/main/Global%20Mean%20Precipitation%20IMERG%20Analysis)

![Alt text](GPM_3IMERGP_INDIA.png?raw=true "GPM IMERG INDIA")