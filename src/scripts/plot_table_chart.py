import numpy as np
import paths
import matplotlib.pyplot as plt
from astropy.io import ascii
from astropy.table import Table

import astropy.coordinates as coord
import astropy.units as u
from astropy.coordinates import SkyCoord

###t = Table.read(paths.data / "YSES_paper - targets.csv")
t = Table.read(paths.static / "YSES_paper - targets.csv")

eq = SkyCoord(t[1:]['RA'], t[1:]['Dec'], unit=(u.hourangle, u.deg))
gal = eq.galactic

fig = plt.figure()
ax = fig.add_subplot(111, projection="aitoff")
plt.grid(True)
#plt.plot(gal.l.wrap_at(180*u.deg), gal.b.wrap_at(180*u.deg), linestyle='None')
#ax.scatter(gal.l, gal.b, linestyle='None')
ax.scatter(gal.l.wrap_at(180*u.deg).radian, gal.b.wrap_at(180.*u.deg).radian, linestyle='None')
plt.savefig('_check_table_chart0.pdf')

fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid(True)

ax.scatter(gal.l.wrap_at(180*u.deg).deg, gal.b.wrap_at(180.*u.deg).deg, linestyle='None')
ax.set_xlim(-85,-40)
ax.set_ylim(-10,25)
ax.set_xlabel('Galactic longitude l [deg]')
ax.set_ylabel('Galactic latitude b [deg]')
plt.savefig(paths.figures / 'table_chart.pdf')

#plt.show()
