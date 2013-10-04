#!/usr/bin/python

# Branching Ratios:  From PDG

# Assumes mH=120 GeV
BR_H_ZZ = 1.59E-02 
BR_H_WW = 1.41E-01
BR_H_BB = 6.48E-01

# Z->l+l-  : 3.37 * 2%  = 0.0674
BR_Z_LL = 0.0674

# Z->v v~  : 20.0%      = 0.200
BR_Z_VV = 0.200

# Z->j j   : 69.9%      = 0.699
BR_Z_JJ = 0.699

# Z-> b b~ : 15.12%    = 0.1512
BR_Z_BB = 0.1512

# Non-b hadronic:
BR_Z_JJ_NOT_BB = (BR_Z_JJ - BR_Z_BB)

# W->l v   : 10.8 * 2%  = 0.216
BR_W_LV = 0.216

# W->j j   : 67.60%     = 0.676
BR_W_JJ = 0.6760

# Cross-sections:  From Madgraph
# Note:  for processes including decays, use only in ratios...
#
# Madgraph reports xsec in **pb**
PB_TO_FB = 1E3

MG_Z   = 4.819E4
MG_ZJJ = 5857
MG_ZBB = 860.7
MG_ZJJ_MLL_GT_80 = 194.8
MG_ZJJ_MLL_LT_80 = 4.792
MG_ZJJ_MLL_TOT   = MG_ZJJ_MLL_GT_80 + MG_ZJJ_MLL_LT_80

MG_ZZ   = 10.53
MG_ZW   = 27.73
MG_WW   = 72.52
MG_WWJJ = 29.75

#
# K-Factors (Needed!)
#

K_Z    = 1
K_ZZ   = 1
K_ZW   = 1
K_WW   = 1

#
# Cross-sections derived from MG plus K-Factors:
#

SIGMA_ZJJ           = MG_ZJJ * K_Z * PB_TO_FB
SIGMA_ZJJ_MLL_LT_80 = SIGMA_ZJJ * MG_ZJJ_MLL_LT_80 / MG_ZJJ_MLL_TOT;
SIGMA_ZJJ_MLL_GT_80 = SIGMA_ZJJ * MG_ZJJ_MLL_GT_80 / MG_ZJJ_MLL_TOT;

SIGMA_ZZ            = MG_ZZ   * K_ZZ * PB_TO_FB
SIGMA_ZW            = MG_ZW   * K_ZW * PB_TO_FB
SIGMA_WWJJ          = MG_WWJJ * K_WW * PB_TO_FB


# From Daniel, in pb
#
# Proc    8tev 14tev
# gg->H   20.9   53.5
# Wh       1.0   1.5
# Zh       0.1   0.9
# ttbar    135   554

SIGMA_H   =  53500
SIGMA_WH  =   1500
SIGMA_ZH  =    900
SIGMA_TT  = 554000

# Signal cross section is taken to be 100 pb:

SIGMA_HXX = 1E5

#Missing Backgrounds:
#VBF Higgs,
#ttH,
#H->WW + jets,
#ZH->llbb
#Fakes,

print "Sigma x BR in fb at at 14 TeV"
print ""
print "Backgrounds:  "
print ""
print "Zjj  -> lljj     ........................", SIGMA_ZJJ * BR_Z_LL
print "  mll < 80 GeV   ........................", SIGMA_ZJJ_MLL_LT_80 * BR_Z_LL
print "  mll > 80 GeV   ........................", SIGMA_ZJJ_MLL_GT_80 * BR_Z_LL
print ""
print "tt   -> lvlvbb ........................", SIGMA_TT * BR_W_LV *  BR_W_LV
print ""
print "ZW   -> lljj   ........................", SIGMA_ZW   * BR_Z_LL * BR_W_JJ
print "ZZ   -> lljj   ........................", SIGMA_ZZ   * BR_Z_LL * BR_Z_JJ_NOT_BB * 2
print "ZZ   -> llbb   ........................", SIGMA_ZZ   * BR_Z_LL * BR_Z_BB * 2
print ""
print "WWjj -> lvlvjj ........................", SIGMA_WWJJ * BR_W_LV * BR_W_LV
print ""
print "H -> ZZ -> lljj .......................", SIGMA_H * BR_H_ZZ * BR_Z_LL * BR_Z_JJ_NOT_BB * 2
print "H -> ZZ -> llbb .......................", SIGMA_H * BR_H_ZZ * BR_Z_LL * BR_Z_BB * 2
print ""
print "ZH, Z->VV, H -> ZZ -> lljj ............", SIGMA_ZH * BR_H_ZZ * BR_Z_VV * BR_Z_LL * BR_Z_JJ_NOT_BB * 2
print "ZH, Z->VV, H -> ZZ -> llbb ............", SIGMA_ZH * BR_H_ZZ * BR_Z_VV * BR_Z_LL * BR_Z_BB * 2
print ""
print "WH, W->LV, H -> ZZ -> lljj ............", SIGMA_WH * BR_H_ZZ * BR_W_LV * BR_Z_LL * BR_Z_JJ_NOT_BB * 2
print "WH, W->LV, H -> ZZ -> llbb ............", SIGMA_WH * BR_H_ZZ * BR_W_LV * BR_Z_LL * BR_Z_BB * 2
print ""
print "Signal:  "
print ""
print "Hxx            ........................", SIGMA_HXX 
print "Hxx, H->ZZ->lljj ......................", SIGMA_HXX * BR_H_ZZ * BR_Z_LL * BR_Z_JJ * 2
print ""
print "Missing Backgrounds:  "
print ""
print "ZH->llbb ..............................", SIGMA_ZH * BR_H_BB * BR_Z_LL





