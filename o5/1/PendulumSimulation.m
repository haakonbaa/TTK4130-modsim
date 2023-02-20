clear all; close all; clc;

% Parameters and initial states
tf = 45; % simulation time

m = 1;
M = 1;
g = 9.81;
L = 1;
F = 0;
parameters = [m M L g]';

state = [0 pi/4 pi/2 0 0 0];

% Simulation
try
    [tsim,xsim] = ode45(@(t,x)PendulumDynamics(t, x, parameters),[0,tf],state);
    data{1} = tsim;
    data{2} = xsim;
    save("sim.mat", 'data');
catch message
    display('Simulation failed with the following message:')
    display(message.message)
    display(' ')
end