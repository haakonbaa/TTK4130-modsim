clear all
close all
clc

% Parameters and initial states
tf = 15;
J = 1;      % Rotational inertia of beam
M = 10;     % Mass of ball
R = 0.25;   % Radius of ball
g = 9.81;   % Gravity
parameters = [J M R g]'

% (x theta dx theta)
state = [1 0 0 0]';

% Simulation
[tsim,xsim] = ode45(@(t,x)BallAndBeamDynamics(t, x, parameters),[0:0.05:tf],state);
data{1} = tsim;
data{2} = xsim;
save("sim.mat", 'data');