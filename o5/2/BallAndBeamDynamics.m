function [x_dot] = BallAndBeamDynamics(t, x, parameters)
    % T = 200(x-theta)+70(dx-dtheta)
    T = 200*(x(1)-x(2))+70*(x(3)-x(4));
    [W RHS] = BallAndBeamODEMatrices(x, T, parameters);
    x_dot = [x(3:4);
            inv(W)*RHS];
end
