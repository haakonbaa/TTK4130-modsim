function [x_dot] = PendulumDynamics(t, x, parameters)
    % Use this one to apply a force:
    % [W RHS] = PendulumODEMatrices(x, -10*x(1)-x(4), parameters);
    [W RHS] = PendulumODEMatrices(x, 0, parameters);
    x_dot = [x(4:6);
            inv(W)*RHS];
end
