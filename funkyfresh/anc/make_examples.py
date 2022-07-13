import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np
from funkyfresh import set_agu_style

theta = np.linspace(0, 360, 3601) * u.degree

fig, axis = plt.subplots(constrained_layout=True)
axis.plot(theta, np.sin(theta))
axis.set_xlabel(r'$\theta$ [degrees]')
axis.set_ylabel(r'$\sin(\theta)$')
plt.savefig('matplotlib_default.png')
plt.close(fig)

style = set_agu_style()
fig, axis = plt.subplots(figsize=(style.column_width, 2),
                         constrained_layout=True)
axis.plot(theta, np.sin(theta), color=style.blue)
axis.set_xlabel(r'$\theta$ [degrees]')
axis.set_ylabel(r'$\sin(\theta)$')
plt.savefig('funkyfresh.png')
plt.close(fig)
