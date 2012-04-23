import odespy, numpy as np, matplotlib.pyplot as plt

center_point = 3
s = 0.5

problem = odespy.problems.Gaussian0(c=center_point, s=s)

npoints = 41
tp = np.linspace(0, 2*center_point, npoints)

solver = odespy.Fehlberg(problem.f)
#solver = odespy.Vode(problem.f)
solver.set_initial_condition(problem.U0)

u, t = solver.solve(tp)

method = solver.__class__.__name__
print '%.4f  %s' % (u.max(), method)

if solver.has_u_t_all():
    plt.plot(solver.t_all, solver.u_all, 'bo',
             tp, problem.u_exact(tp))
    print '%s used %d steps (%d specified)' % \
          (method, len(solver.u_all), len(tp))
else:
    plt.plot(tp, solver.u, tp, problem.u_exact(tp))
plt.legend([method, 'exact'])
plt.savefig('tmp.png')
plt.show()
