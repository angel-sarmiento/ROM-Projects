# ROM Projects
 A project exploring POD and other dimensionality reduction methods in many applications

# Project 1: The 1-Dimensional Heat Equation

### Introduction

In this work is a view of a subject that is a bit of a passion of mine as of late. This subject is Model-Order Reduction and the application of this subject on the 1-Dimensional representation of the heat/diffusion equation. The primary methodology of this work is the creation of a reduced-basis representation of this equation, that is then mapped to the full order basis and displaying the metrics like accuracy and computation cost associated with this action. This report details the main ideas behind the mathematics involved in solving a time-depending partial differential equation, the mathematics involved in applying methods like the Proper Orthogonal Decomposition using the singular value decomposition on the resulting state vectors, and the resulting analyses done to understand relationships between parameter and reduced-order basis selection. The entire set of scripts are written in python with all of the code, images, and resulting snapshot matrix data available [here](https://github.com/angel-sarmiento/ROM-Projects/tree/master/1D-Heat_equation).

Report is written in rmarkdown and can be found [here](https://github.com/angel-sarmiento/ROM-Projects/blob/master/1D-Heat_equation/reports/pod-rom-1d-heat-equation.html). It has gifs like this one!

![](https://github.com/angel-sarmiento/ROM-Projects/blob/master/1D-Heat_equation/python/images/mu_plot_1.gif)


### Key Findings

- Higher Dimensionality of reduced-basis yields more accurate results when compared to the FOM

- The further the value of the diffusivity constant calculated from the one used to create snapshots matrices for the ROM, the less accurate the model is. However, the model is computationally faster. 

- There are some key limitations in implementing ROM in this way:
    -  Simulation needs to be modeled to gain the snapshots in the first place
    -  The ROM might not performed better in terms of computation time in every instance, especially instances where the FOM can be computed very fast and the mapping method used to return the reduced vectors to their full-dimensional counterparts is slow

This was a very challenging project which necessitated good python skills, a moderately strong foundation in Partial Differential Equations, and a good foundational understanding of linear algebra and model-order reduction.