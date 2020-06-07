clc
clear
f = inline('-x^2 + (20*cos(pi/100*t)+20)*x - (10 + 10*cos(pi/100*t))^2 + 5*sin(pi/100*t) + 5', 'x','t');
%tic
%[xm, fm , iter]=GoldenMethod(-10, 30, 1e-15, f, 125);
%[xm, fm , iter]=NaiveMethod(-10, 30, 1e-15, f, 60);
%toc

f_vec = [];
i = 1;
tic
for t = 0:0.1:150
    [xm, fm , iter]=GoldenMethod(-10, 30, 1e-9, f, t);
    f_vec(i) = fm;
    i = i + 1;
end
toc

f_vec1 = [];
i = 1;
tic
for t = 0:0.1:150
    [xm, fm , iter]=NaiveMethod(-10, 30, 1e-9, f, t);
    f_vec1(i) = fm;
    i = i + 1;
end
toc

t = 0:0.1:150
plot(t,f_vec,'r',t,f_vec1,'b');
ylabel('f(xm)');
xlabel('t');
grid on;
