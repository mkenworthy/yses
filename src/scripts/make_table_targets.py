import numpy as np
import paths
from astropy.io import ascii
from astropy.table import Table

### t = Table.read(paths.data / "YSES_paper - targets.csv")
### TODO ultimately the csv should be in the Zenodo but with the regular updates we'll put it in static/ instead

t = Table.read(paths.static / "YSES_paper - targets.csv")

def write_aa_longtable(t, tout='long.tex', capt='Table caption'):
    ascii.write(t[1:],paths.data / 'tmp',overwrite=True,
        Writer=ascii.Latex)

    with open(paths.data / 'tmp') as f:
        lines = f.readlines()

    colformat = lines[1][15:].strip() # remove \tabular and get {cclll...}
    colhead = lines[2]

    fh = open(paths.output / tout, 'w')
    fh.write(r'\begin{longtable}'+f'{colformat}'+'\n')
    fh.write(r'\caption{'+capt+r'}\\'+'\n')
    fh.write(r'\hline\hline'+'\n')
    fh.write(colhead)
    fh.write('\hline\n\endfirsthead\n\caption{continued.}\\\\\n')
    fh.write(r'\hline\hline'+'\n')
    fh.write(colhead)
    fh.write('\hline\n\endhead\n\hline\n\endfoot\n')

    # add table data
    for element in lines[3:-2]:
        fh.write(element)
    fh.write('\end{longtable}\n')
    fh.close()

write_aa_longtable(t,'table_targets.tex','\label{tab:targets}Star targets and their properties')
# \begin{longtable}{lllrrr}
# \caption{\label{kstars} Sample stars with absolute magnitude}\\
# \hline\hline
# Catalogue& $M_{V}$ & Spectral & Distance & Mode & Count Rate \\
# \hline
# \endfirsthead
# \caption{continued.}\\
# \hline\hline
# Catalogue& $M_{V}$ & Spectral & Distance & Mode & Count Rate \\
# \hline
# \endhead
# \hline
# \endfoot
# %%
# Gl 33    & 6.37 & K2 V & 7.46 & S & 0.043170\\
# Gl 66AB  & 6.26 & K2 V & 8.15 & S & 0.260478\\
# Gl 68    & 5.87 & K1 V & 7.47 & P & 0.026610\\
#          &      &      &      & H & 0.008686\\
# Gl 86
# \footnote{Source not included in the HRI catalog. See Sect.~5.4.2 for details.}
#          & 5.92 & K0 V & 10.91& S & 0.058230\\
# \end{longtable}
