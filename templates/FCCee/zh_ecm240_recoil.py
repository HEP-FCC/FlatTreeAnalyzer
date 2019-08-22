import ROOT
import collections

ana_tex = "ZH #rightarrow #mu^{+}#mu^{-} + recoil"

### variable list
variables = {
    "ptz":{"name":"zed_pt","title":"p_{T}^{Z} [GeV]","bin":100,"xmin":0,"xmax":300},
    "mz":{"name":"zed_m","title":"m_{Z} [GeV]","bin":100,"xmin":0,"xmax":150},
    "ptmu_1":{"name":"mu1_pt","title":"p_{T}^{#mu, max} [GeV]","bin":100,"xmin":0,"xmax":100},
    "ptmu_2":{"name":"mu2_pt","title":"p_{T}^{#mu, min} [GeV]","bin":100,"xmin":0,"xmax":100},

    "mrecoil":{"name":"recoil_m","title":"m_{Recoil} [GeV]","bin":100,"xmin":50,"xmax":150},
    "ptrecoil":{"name":"recoil_m","title":"p_{T}^{Recoil} [GeV]","bin":100,"xmin":0,"xmax":100},

    "met_pt":{"name":"met_pt","title":"met p_{T} [GeV]","bin":100,"xmin":0,"xmax":100},
    "met_sumet":{"name":"met_sumet","title":"met sum E_{T} [GeV]","bin":100,"xmin":0,"xmax":100},

}

variables2D = {}


colors = {}
colors['ZH'] = ROOT.kRed
colors['ZZ'] = ROOT.kGreen+2
colors['WW'] = ROOT.kBlue+1

signal_groups = collections.OrderedDict()
signal_groups['ZH'] = ['p8_ee_ZH_ecm240']

background_groups = collections.OrderedDict()
background_groups['ZZ'] = ['p8_ee_ZZ_ecm240']
background_groups['WW'] = ['p8_ee_WW_ecm240']

# global parameters
intLumi = 5.0e+06
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = True

# base pre-selections
selbase = 'recoil_m>10.'
sel_met = '&& met_pt<20.'
# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
selections['ZH'] = []
selections['ZH'].append(selbase)
selections['ZH'].append(selbase+sel_met)

