# Workout planner

[![Python](https://img.shields.io/pypi/pyversions/workoutizer.svg?style=plastic)](https://badge.fury.io/py/workoutizer)
[![Build Status](https://github.com/fgebhart/workoutizer/actions/workflows/matrix_test.yml/badge.svg)](https://github.com/fgebhart/workoutizer/actions/workflows/matrix_test.yml)
[![Setup on Raspberry Pi](https://github.com/fgebhart/workoutizer/actions/workflows/raspberry_pi_test.yml/badge.svg)](https://github.com/fgebhart/workoutizer/actions/workflows/raspberry_pi_test.yml)
[![Coverage Badge](https://raw.githubusercontent.com/fgebhart/workoutizer/master/.github/badges/coverage.svg)](https://raw.githubusercontent.com/fgebhart/workoutizer/master/.github/badges/coverage.svg)
[![Downloads](https://pepy.tech/badge/workoutizer/month)](https://pepy.tech/project/workoutizer)

Workoutizer is a simple python application for organizing your workouts races for sports activities. It is designed to work locally on any UNIX-like system running Python.

The file allows you to visualize the training volume and to program your season while preferring a progressive staircase to limit injuries and over-training.
I use the "[Trimps](https://blog.nolio.io/post/utiliser-la-charge-dentrainement-pour-mieux-sentrainer)" method.
The load is calculated for each session as a function of the time spent in the different heart rate zones (Z1=50%-60% fcmax, ..., Z5=90%-100% fcmax) in arbitrary units. Then the acute load over the week and the monotonicity index are calculated.According to the work of Foster, 1998: "decrease in performance capacity and appearance of fatigue beyond an index of 2, occurrence of injuries beyond 2.5". This monotonicity index should therefore be monitored. The chronic loads over 4 and 8 weeks are then calculated, as well as the load variation over these periods. An index below 1.0 indicates that the body is recovering (before a race, or after a training cycle). An index above 1.3 indicates an increase in load of more than 30%, which can be difficult to tolerate and usually leads to injury if several weeks in a row are loaded. The ideal is to remain between 1.0 and 1.3, in order to create an overcompensation on the part of the body, and thus an adaptive response. However, this variation should be kept to a minimum and the body should be given time to recover. This index should therefore be monitored.

I have deliberately left some examples for visualization. 


## Features

* Organisation of a full sports season taking into account the upstream load.
* Calculation of objective sports data. 
* Adapting the sessions to the training. 
* Keeping an eye on the goals. 
* Avoiding injuries !

## To do

## Status

This app is still in developpement. Things will be added, modified in the future. I would be happy to receive bug reports and opinions.

## Getting Started

TODO

## Gallery

TODO

## Changelog

See [Changelog](https://github.com/fgebhart/workoutizer/blob/main/CHANGELOG.md).

## Papers and thesis

