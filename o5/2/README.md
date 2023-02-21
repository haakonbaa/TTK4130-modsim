# Assignment 5 problem 2

Note that the solution proposed here uses another reference frame than the one in the exercise!

## Usage
- Generate ```BallAndBeamODEMatrices.m``` and ```BallPosition.m``` by running ```BallAndBeamSymbolic.m```
- run ``BallAndBeamSimulation.m`` to generate data ```sim.mat```
- run ```ballandbeam.py``` to visualize data

## Example
This example uses [matex](https://github.com/haakonbaa/matex) to run matlab scripts in terminal
```bash
matex BallAndBeamSymbolic.m 
matex BallAndBeamSimulation.m
python3 ballandbeam.py
```

make sure you have installed the correct python packages
```bash
python3 -m pip install pygame scipy
```