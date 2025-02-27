pos = [
0 0 0;
1 25 50;
2 45 75;
3 70 86;
4 90 100;
5 110 90;
6 155 70;
7 190 85;
8 220 90;
9 285 105
10 325 120;
11 390 165;
12 460 205;
13 560 320;
14 610 400;
15 655 485;
16 675 555;
17 705 640;
18 720 740;
19 710 860;
20 705 1005;
21 670 1155;
22 625 1300;
23 560 1465;
24 485 1650;
25 320 1750;
26 160 1820;
27 -10 1755;
28 -155 1605;
29 -340 1545;
30 -565 1470;
31 -795 1430;
32 -980 1380;
33 -1165 1340;
34 -1330 1335;
35 -1495 1350;
36 -1620 1325;
37 -1720 1250;
38 -1770 1160;
39 -1805 1070;
40 -1810 985;
41 -1805 910;
42 -1780 855;
43 -1750 830;
44 -1720 810;
45 -1705 800;
46 -1690 790;
47 -1680 785;
48 -1675 770;
49 -1665 760;
50 -1640 755;
51 -1610 740;
52 -1580 720;
53 -1540 705;
54 -1505 670;
55 -1445 650;
56 -1360 625;
57 -1245 590;
58 -1120 570;
59 -990 555;
60 -860 505;
61 -775 460;
62 -700 410;
63 -665 380;
64 -625 355;
65 -580 325;
66 -550 300;
67 -515 295;
68 -480 320;
69 -445 340;
70 -400 395;
71 -355 380;
72 -290 350;
73 -245 305;
74 -200 225;
75 -175 100;
76 -100 0;
77 0 0;
];

%build equations
% b1/A1->x b2/A2->y
b1 = [];
b2 = [];
b1(1) = 0;
b2(1) = 0;
for i = 2:77
	b1(i) = 6 * (pos(i+1,2)-pos(i,2)) / (pos(i+1,1)-pos(i,1)) + 6 * (pos(i-1,2)-pos(i,2)) / (pos(i,1)-pos(i-1,1));
	b2(i) = 6 * (pos(i+1,3)-pos(i,3)) / (pos(i+1,1)-pos(i,1)) + 6 * (pos(i-1,3)-pos(i,3)) / (pos(i,1)-pos(i-1,1));
end
b1(78) = 0;
b2(78) = 0;

A1(1,1) = 1;
A2(1,1) = 1;
for i = 2:77
	A1(i,i-1) = pos(i,1)-pos(i-1,1);
	A1(i,i) = 2 * (pos(i+1,1)-pos(i-1,1));
	A1(i,i+1) = pos(i+1,1)-pos(i,1);
	A2(i,i-1) = pos(i,1)-pos(i-1,1);
	A2(i,i) = 2 * (pos(i+1,1)-pos(i-1,1));
	A2(i,i+1) = pos(i+1,1)-pos(i,1); 
end
A1(78,78) = 1;
A2(78,78) = 1;

%use special case of LU decomposition
for i = 2:78
    A1(i,i-1) = A1(i,i-1) / A1(i-1,i-1);
    A1(i,i) = A1(i,i) - A1(i,i-1) * A1(i-1,i);
    A2(i,i-1) = A2(i,i-1) / A2(i-1,i-1);
    A2(i,i) = A2(i,i) - A2(i,i-1) * A2(i-1,i);
end
for i=2:78
    b1(i) = b1(i) - A1(i,i-1)*b1(i-1);
    b2(i) = b2(i) - A2(i,i-1)*b2(i-1);
end
d1 = zeros(1,78);
d1(78) = b1(78) / A1(78,78);
d2 = zeros(1,78);
d2(78) = b2(78) / A2(78,78);
for i=77:-1:1
   d1(i) = (b1(i)-A1(i,i+1)*d1(i+1))/A1(i,i);
   d2(i) = (b2(i)-A2(i,i+1)*d2(i+1))/A2(i,i);
end

% get trajectory
traj_x_CSI = [];
traj_y_CSI = [];
len = 0;
for i = 1:77
    t0 = pos(i,1);
    t1 = pos(i+1,1);
    x0 = pos(i,2);
    x1 = pos(i+1,2);
    y0 = pos(i,3);
    y1 = pos(i+1,3);
    traj_x_CSI(end+1) = x0;
    traj_y_CSI(end+1) = y0;
    slip = (t1 - t0) / 10;
    delta_t = t1 - t0;
    for t = (t0+slip):slip:(t1-slip)
        traj_x_CSI(end+1)=d1(i)*(t1-t)^3/delta_t/6+d1(i+1)*(t-t0)^3/delta_t/6+(x0/delta_t-d1(i)*delta_t/6)*(t1-t)+(x1/delta_t-d1(i+1)*delta_t/6)*(t-t0);
        traj_y_CSI(end+1)=d2(i)*(t1-t)^3/delta_t/6+d2(i+1)*(t-t0)^3/delta_t/6+(y0/delta_t-d2(i)*delta_t/6)*(t1-t)+(y1/delta_t-d2(i+1)*delta_t/6)*(t-t0);
    end
end
traj_x_CSI(end+1) = 0;
traj_y_CSI(end+1) = 0;

num = length(traj_x_CSI);
for i = 1:(num-1)
    len  = len + sqrt((traj_x_CSI(i+1)-traj_x_CSI(i))^2 + (traj_y_CSI(i+1)-traj_y_CSI(i))^2);
end

plot(traj_x_CSI, traj_y_CSI, 'r', pos(:,2), pos(:,3), 'b');
ylabel('y');
xlabel('x');
grid on;
