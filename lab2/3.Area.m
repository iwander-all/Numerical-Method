

Sa_LI = 0;
Sa_CSI = 0;
Sb_LI = 0;
Sb_CSI = 0;

% calculate top area
for i=181:400
    Sa_LI = Sa_LI + abs((traj_x_LI(i+1)-traj_x_LI(i)) * (traj_y_LI(i+1)+traj_y_LI(i)) / 2);
    Sa_CSI = Sa_CSI + abs((traj_x_CSI(i+1)-traj_x_CSI(i)) * (traj_y_CSI(i+1)+traj_y_CSI(i)) / 2);
end

% calculate bottom area
for i=1:180
    Sb_LI = Sb_LI + abs((traj_x_LI(i+1)-traj_x_LI(i)) * (traj_y_LI(i+1)+traj_y_LI(i)) / 2);
    Sb_CSI = Sb_CSI + abs((traj_x_CSI(i+1)-traj_x_CSI(i)) * (traj_y_CSI(i+1)+traj_y_CSI(i)) / 2);
end
for i=401:770
    Sb_LI = Sb_LI + abs((traj_x_LI(i+1)-traj_x_LI(i)) * (traj_y_LI(i+1)+traj_y_LI(i)) / 2);
    Sb_CSI = Sb_CSI + abs((traj_x_CSI(i+1)-traj_x_CSI(i)) * (traj_y_CSI(i+1)+traj_y_CSI(i)) / 2);
end

% area
S_LI =  Sa_LI - Sb_LI;
S_CSI = Sa_CSI - Sb_CSI;
