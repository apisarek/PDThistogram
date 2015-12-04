This program makes histogram of particles by their masses and saves it into a .root file.

You need to pass the arguments (bin sizes in MeV) in the command.

Example usage:
python histogram.py 20 40 60

If you want to open this histogram, you need to (example):
>>> f = TFile('15-12-04_08:22:27.root')
>>> h = f.Get('bin_size:20MeV')

If you don't have pyPDT installed, the particle masses will be imported from the text file.
You can overwrite this file if pyPDT is installed by importing histogram.py and running save_masses()

