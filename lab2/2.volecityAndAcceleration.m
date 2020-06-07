
%default: length should be 770
vx_LI = [];
vy_LI = [];
v_LI = [];
vx_CSI  = [];
vy_CSI  = [];
v_CSI  = [];
%default: length should be 769
ax_LI = [];
ay_LI = [];
a_LI = [];
ax_CSI  = [];
ay_CSI  = [];
a_CSI  = [];

t1= [];
t2= [];

% volecity
for i=1:770
    vx_LI(i) = (traj_x_LI(i+1)-traj_x_LI(i))/0.1;
    vy_LI(i) = (traj_y_LI(i+1)-traj_y_LI(i))/0.1;
    vx_CSI(i) = (traj_x_CSI(i+1)-traj_x_CSI(i))/0.1;
    vy_CSI(i) = (traj_y_CSI(i+1)-traj_y_CSI(i))/0.1;
    v_LI(i) = sqrt(vx_LI(i)^2+vy_LI(i)^2);
    v_CSI(i) = sqrt(vx_CSI(i)^2+vy_CSI(i)^2);
    t1(i) = i/10;
end

plot(t1,v_LI,'r',t1,v_CSI,'b');
ylabel('volecity');
xlabel('time');
grid on;

% acceleration
for i=1:769
    ax_LI(i) = (vx_LI(i+1)-vx_LI(i))/0.1;
    ay_LI(i) = (vy_LI(i+1)-vy_LI(i))/0.1;
    ax_CSI(i) = (vx_CSI(i+1)-vx_CSI(i))/0.1;
    ay_CSI(i) = (vy_CSI(i+1)-vy_CSI(i))/0.1;
    if v_LI(i+1)> v_LI(i)
        a_LI(i) = sqrt(ax_LI(i)^2+ay_LI(i)^2);
    else
        a_LI(i) = -sqrt(ax_LI(i)^2+ay_LI(i)^2);
    end
    if v_CSI(i+1)> v_CSI(i)
        a_CSI(i) = sqrt(ax_CSI(i)^2+ay_CSI(i)^2);
    else
        a_CSI(i) = -sqrt(ax_CSI(i)^2+ay_CSI(i)^2);
    end
    t2(i) = i/10;
end

plot(t2,a_LI,'r',t2,a_CSI,'b');
ylabel('acceleration');
xlabel('time');
grid on;
