# Assignment 5 problem 1

## Usage
- Generate ```PendulumPosition.m``` and ```PendulumODEMatrices``` by running ```PendulumSymbolic.m```
- run ``PendulumSimulation.m`` to generate data ```sim.mat```
- run ```doublependulum.py``` to visualize data

## Example
This example uses [matex](https://github.com/haakonbaa/matex) to run matlab scripts in terminal
```bash
matex PendulumSymbolic.m
matex PendulumSimulation.m
python3 doublependulum.py
```

make sure you have installed the correct python packages
```bash
python3 -m pip install pygame scipy
```