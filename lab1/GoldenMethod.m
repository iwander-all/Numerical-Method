function [xm, fm , iter] = GoldenMethod(xlow, xhigh, es, f, t)
% input: 
%     [xlow, xhigh]: initial range
%     es: expected tolerance, length of bracket
%     f: the inline function
%     t: the parameter of f
% output:
%     output = [xm, f(xm), iter]
%     xm: the x value when f(x) is maximum     
%     iter: the number of iterations 
%-----Please enter your codes below------
	xl = xlow;
	xu = xhigh;
	R = (sqrt(5) - 1) / 2;
	iter = 0;
	d = R * (xu - xl);
	x1 = xl + d;
	x2 = xu - d;
	f1 = f(x1,t);
	f2 = f(x2,t);
	while xu - xl >= es
		if f1 > f2
			xm = x1;
			fm = f1;
			xl = x2;
			x2 = x1;
			d = R * (xu - xl);
			x1 = xl +d;
			f2 = f1;
			f1 = f(x1,t);
        else
			xm = x2;
			fm = f2;
			xu = x1;
			x1 = x2;
			d = R * (xu - xl);
			x2 = xu - d; 
			f1 = f2;
			f2 = f(x2,t);
		end
		iter = iter + 1;
    end
end
