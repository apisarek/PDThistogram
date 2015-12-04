import argparse
import datetime
import ROOT
from ROOT import TH1F, TFile

#there is some predefined argparse behaviour done by ROOT which is not needed here
ROOT.PyConfig.IgnoreCommandLineOptions = True
parser = argparse.ArgumentParser(description='Makes histogram of masses of all known particles and saves to file')
parser.add_argument('bin_size', metavar='bin_size', type=int, nargs='+',
                   help='bin_size')


def get_masses():
    '''
    Return masses from ParticleDataTable
    If library isnt installed then reads masses from file
    :return: List[float]
    '''
    try:
        from pypdt import PDT
        return [particle.mass*1000 for particle in PDT()]
    except StandardError:
        with open('pdt_mass.txt') as f:
            masses = map(float, f.read().split('\n'))
        return masses

def save_masses():
    '''
    Saves masses from ParticleDataTable into a file
    :return: None
    '''
    with open('pdt_mass.txt', 'w') as f:
        from pypdt import PDT
        f.write('\n'.join(str(particle.mass*1000) for particle in PDT()))


def main():
    masses = get_masses()
    bin_sizes = parser.parse_args().bin_size
    min_mass = 0
    max_mass = max(masses)

    time_now = datetime.datetime.now().strftime("%y-%m-%d_%H:%M:%S")

    f = TFile(time_now + '.root', 'recreate')

    for width in bin_sizes:
        nbins = int(max_mass/width) + 1
        xup = nbins * width
        xlow = min_mass

        title = 'bin_size:' + str(width) + 'MeV'
        hist = TH1F(title, 'Histogram of masses', nbins, xlow, xup)
        for mass in masses:
            hist.Fill(mass)

        f.Write()
    f.Close()

if __name__ == '__main__':
    main()