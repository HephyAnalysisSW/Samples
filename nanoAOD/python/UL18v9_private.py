import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',          action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',             action='store_true',    help="Update current entry in db?")
    argParser.add_argument('--check_completeness', action='store_true',    help="Check competeness?")
    return argParser
# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
       ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

DYJetsToLL_M50_LO             =   Sample.fromDirectory("DYJetsToLL_M50_LO",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211215_225210/",	xSection=2075.14*3)
DYJetsToLL_M50_LO.normalization = 96233328.0 
DYJetsToLL_M50_LO_ext	      =	  Sample.fromDirectory("DYJetsToLL_M50_LO_ext",	 "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1_ext1-v1_privateUL18nanov9/211215_225231/",		xSection=2075.14*3)
DYJetsToLL_M50_LO_ext.normalization = 101415750.0 
DYJetsToLL_M10to50_LO         =   Sample.fromDirectory("DYJetsToLL_M10to50_LO", "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211215_225256/",	xSection=18610)
DYJetsToLL_M10to50_LO.normalization = 99288125.0

### x-sections for DY M50 HT bins taken from, after a correction in official M50 inclusive sample (https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z)  : CMS AN-22-057
#DYJetsToLL_M50_HT70to100      =   Sample.fromDirectory("DYJetsToLL_M50_HT70to100",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210222/",	 xSection=141.1*1.23)
#DYJetsToLL_M50_HT70to100.normalization =  
DYJetsToLL_M50_HT100to200     =   Sample.fromDirectory("DYJetsToLL_M50_HT100to200",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210242/",	 xSection=140.4*1.23)
DYJetsToLL_M50_HT100to200.normalization = 26202328.0 
DYJetsToLL_M50_HT200to400     =   Sample.fromDirectory("DYJetsToLL_M50_HT200to400",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210302/",	xSection=38.67*1.23)
DYJetsToLL_M50_HT200to400.normalization = 18455718.0
DYJetsToLL_M50_HT400to600     =   Sample.fromDirectory("DYJetsToLL_M50_HT400to600",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210321/",	xSection=5.221*1.23)
DYJetsToLL_M50_HT400to600.normalization = 8908406.0
DYJetsToLL_M50_HT600to800     =   Sample.fromDirectory("DYJetsToLL_M50_HT600to800",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210343/",	xSection=1.264*1.23 )
DYJetsToLL_M50_HT600to800.normalization = 7035971.0
DYJetsToLL_M50_HT800to1200    =   Sample.fromDirectory("DYJetsToLL_M50_HT800to1200",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210403/",	xSection=0.5669*1.23 )
DYJetsToLL_M50_HT800to1200.normalization = 6678036.0
DYJetsToLL_M50_HT1200to2500   =   Sample.fromDirectory("DYJetsToLL_M50_HT1200to2500",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210428/",xSection=0.1344*1.23 )
DYJetsToLL_M50_HT1200to2500.normalization = 6166852.0
DYJetsToLL_M50_HT2500toInf    =   Sample.fromDirectory("DYJetsToLL_M50_HT2500toInf",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210449/",	xSection=0.003011*1.23 )
DYJetsToLL_M50_HT2500toInf.normalization = 1978203.0
DYJetsM50HT = [
		#DYJetsToLL_M50_HT70to100,
		DYJetsToLL_M50_HT100to200,
		DYJetsToLL_M50_HT200to400,
		DYJetsToLL_M50_HT400to600,
		DYJetsToLL_M50_HT600to800,
		DYJetsToLL_M50_HT800to1200,
		DYJetsToLL_M50_HT1200to2500,
		DYJetsToLL_M50_HT2500toInf,
		]
### x-sections for DY M4-50 samples taken from : https://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2019/276 
##DYJetsToLL_M4to50_HT70to100      = Sample.fromDirectory("DYJetsToLL_M4to50_HT70to100"     , "",         xSection=303.4) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT100to200     = Sample.fromDirectory("DYJetsToLL_M4to50_HT100to200"    , "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220524_122219/",         xSection=202.8) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT100to200.normalization = 14442189.0 
DYJetsToLL_M4to50_HT200to400     = Sample.fromDirectory("DYJetsToLL_M4to50_HT200to400"    , "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3_privateUL18nanov9/",         xSection=53.7) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT200to400.normalization = 14305796.0
DYJetsToLL_M4to50_HT400to600     = Sample.fromDirectory("DYJetsToLL_M4to50_HT400to600"    , "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/",         xSection=5.66) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT400to600.normalization = 15537383.0
DYJetsToLL_M4to50_HT600toInf     = Sample.fromDirectory("DYJetsToLL_M4to50_HT600toInf"    , "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220524_122242/",         xSection=1.852) #LO without 1.23 k-factor
DYJetsToLL_M4to50_HT600toInf.normalization = 14597795.0
DYJetsM4to50HT = [
##    DYJetsToLL_M4to50_HT70to100,
    DYJetsToLL_M4to50_HT100to200,
    DYJetsToLL_M4to50_HT200to400,
    DYJetsToLL_M4to50_HT400to600,
    DYJetsToLL_M4to50_HT600toInf,
]

# x-secs using runXSecAnalyzer
DYJetsToNuNu_HT100to200       = Sample.fromDirectory("DYJetsToNuNu_HT100to200",	      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205750/",	       xSection=280.35*1.23)
DYJetsToNuNu_HT100to200.normalization = 28876062.0 
DYJetsToNuNu_HT200to400       = Sample.fromDirectory("DYJetsToNuNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_205810/",         xSection=77.67*1.23)
DYJetsToNuNu_HT200to400.normalization = 22749608.0 
DYJetsToNuNu_HT400to600       = Sample.fromDirectory("DYJetsToNuNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205829/",         xSection=10.73*1.23)
DYJetsToNuNu_HT400to600.normalization = 19810491.0
DYJetsToNuNu_HT600to800       = Sample.fromDirectory("DYJetsToNuNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205849/",         xSection=2.559*1.23)
DYJetsToNuNu_HT600to800.normalization = 5968910.0
DYJetsToNuNu_HT800to1200      = Sample.fromDirectory("DYJetsToNuNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205911/",         xSection=1.1796*1.23)
DYJetsToNuNu_HT800to1200.normalization = 2129122.0
DYJetsToNuNu_HT1200to2500     = Sample.fromDirectory("DYJetsToNuNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205930/",         xSection=0.28833*1.23)
DYJetsToNuNu_HT1200to2500.normalization = 381695.0
DYJetsToNuNu_HT2500toInf      = Sample.fromDirectory("DYJetsToNuNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205950/",         xSection=0.006945*1.23)
DYJetsToNuNu_HT2500toInf.normalization = 268224.0

DYJetsNuNuHT = [
   DYJetsToNuNu_HT100to200,
   DYJetsToNuNu_HT200to400,
   DYJetsToNuNu_HT400to600,
   DYJetsToNuNu_HT600to800,
   DYJetsToNuNu_HT800to1200,
   DYJetsToNuNu_HT1200to2500,
   DYJetsToNuNu_HT2500toInf,
]


DY = [
	DYJetsToLL_M50_LO,
	DYJetsToLL_M50_LO_ext,
	DYJetsToLL_M10to50_LO,
	] + DYJetsM50HT  + DYJetsNuNuHT  + DYJetsM4to50HT

# ttbar
TTLep_pow_CP5       = Sample.fromDirectory("TTLep_pow_CP5",            "/eos/vbc/experiments/cms/store/user/prhussai/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205341/",            xSection=831.762*((3*0.108)**2))
TTLep_pow_CP5.normalization = 10528968535.6 
TTSingleLep_pow_CP5 = Sample.fromDirectory("TTSingleLep_pow_CP5",      "/eos/vbc/experiments/cms/store/user/prhussai/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_205531/",            xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTSingleLep_pow_CP5.normalization = 144128770267.0 
#TTbar               = Sample.fromDirectory("TTbar",                "",        xSection=831.762)
#TTJets_amcatnlo     = Sample.fromDirectory("TTJets_amcatnlo",                "",        xSection=831.762)

## single top
#
T_tch_pow           = Sample.fromDirectory("T_tch_pow",        "/eos/vbc/experiments/cms/store/user/prhussai/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210509/",         xSection=136.02) 
T_tch_pow.normalization = 19000619395.3 
TBar_tch_pow        = Sample.fromDirectory("TBar_tch_pow",     "/eos/vbc/experiments/cms/store/user/prhussai/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/220329_094304/",     xSection=80.95)
TBar_tch_pow.normalization = 6128118195.24 
#
T_tWch_ext          = Sample.fromDirectory("T_tWch_ext",       "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210550/",         xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
T_tWch_ext.normalization = 365675749.161 
TBar_tWch_ext       = Sample.fromDirectory("TBar_tWch_ext",    "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210529/",     xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch_ext.normalization = 358102373.391

## ttV
TTWToLNu_CP5        = Sample.fromDirectory("TTWToLNu_CP5" ,    "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210631/",   xSection=0.2043)
TTWToLNu_CP5.normalization = 3525043.51753
TTWToQQ             = Sample.fromDirectory("TTWToQQ",          "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210654/",         xSection=0.40620)
TTWToQQ.normalization = 656374.27741
TTZ_LO              = Sample.fromDirectory("TTZ_LO",           "/eos/vbc/experiments/cms/store/user/prhussai/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_210732/",                                   xSection=0.5297/0.692)
TTZ_LO.normalization = 32793815.0
TTW_LO              = Sample.fromDirectory("TTW_LO",            "/eos/vbc/experiments/cms/store/user/prhussai/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_210713/",  xSection=0.6105)        
TTW_LO.normalization =  27686862.0 
TTGJets             = Sample.fromDirectory("TTGJets",          "/eos/vbc/experiments/cms/store/user/prhussai/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210610/",             xSection=3.697)
TTGJets.normalization = 28272835.839 

TTV = [TTWToLNu_CP5, TTWToQQ , TTZ_LO, TTW_LO, TTGJets ]

top = [
    
#    #TTbar,
    TTLep_pow_CP5,
    TTSingleLep_pow_CP5,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch_ext,
    TBar_tWch_ext,
    ] + TTV 

## di/multiboson
WWTo2L2Nu           = Sample.fromDirectory("WWTo2L2Nu",        "/eos/vbc/experiments/cms/store/user/prhussai/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_210010/",   xSection=12.178)
WWTo2L2Nu.normalization = 110795280.393 
WWTo1L1Nu2Q         = Sample.fromDirectory("WWTo1L1Nu2Q",        "/eos/vbc/experiments/cms/store/user/prhussai/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220524_122006/",         xSection=49.997)
WWTo1L1Nu2Q.normalization = 3928644883.74 
WW                  = Sample.fromDirectory("WW",               "/eos/vbc/experiments/cms/store/user/prhussai/WW_TuneCP5_13TeV-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/220329_093526/",                  xSection=63.21 * 1.82)
WW.normalization = 15679122.7146 
ZZTo2L2Nu           = Sample.fromDirectory("ZZTo2L2Nu",        "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_210121/",                     xSection=0.564)
ZZTo2L2Nu.normalization = 55393059.2321 

ZZTo2Q2L            = Sample.fromDirectory("ZZTo2Q2L",             "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220524_122117/",                           xSection=3.28)
ZZTo2Q2L.normalization = 161924458.071
ZZTo2Nu2Q           = Sample.fromDirectory("ZZTo2Nu2Q",            "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3_privateUL18nanov9/220524_122141/",            xSection=4.04)
ZZTo2Nu2Q.normalization = 37590252.0159

#ZZTo2Q2Nu           = Sample.fromDirectory("ZZTo2Q2Nu",            "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo2Q2Nu_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_210143/",            xSection=4.04) ## old version from central production, discontinued now
#ZZTo2Q2Nu.normalization = 137620490.177
ZZTo4L              = Sample.fromDirectory("ZZTo4L",               "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_210202/",                             xSection=1.256*1.1)
ZZTo4L.normalization = 131414241.629 

WZTo1L3Nu           = Sample.fromDirectory("WZTo1L3Nu"  ,          "/eos/vbc/experiments/cms/store/user/prhussai/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v3_privateUL18nanov9/",            xSection=(47.13)*(3*0.108)*(0.2) )
WZTo1L3Nu.normalization = 14066954.0056
WZTo1L1Nu2Q         = Sample.fromDirectory("WZTo1L1Nu2Q",          "/eos/vbc/experiments/cms/store/user/prhussai/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220524_122028/",          xSection=10.71)
WZTo1L1Nu2Q.normalization = 144265704.572
#WZTo1L1Nu2Q         = Sample.fromDirectory("WZTo1L1Nu2Q",          "/eos/vbc/experiments/cms/store/user/prhussai/WZTo1L1Nu2Q_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_210100/",          xSection=10.71)  ## old version from central production, discontinued now
#WZTo1L1Nu2Q.normalization = 365545828.006
WZTo2Q2L            = Sample.fromDirectory("WZTo2Q2L"   ,          "/eos/vbc/experiments/cms/store/user/prhussai/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220524_122051/",             xSection=5.60)
WZTo2Q2L.normalization = 274146237.028
#WZTo3LNu            = Sample.fromDirectory("WZTo3LNu",             "/WZTo3LNu",         xSection=4.42965)
WZTo3LNu_amcatnlo   = Sample.fromDirectory("WZTo3LNu_amcatnlo",    "/eos/vbc/experiments/cms/store/user/prhussai/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211124_210040/",        xSection=4.666)
WZTo3LNu_amcatnlo.normalization = 83145977.5623


boson = [
    WWTo2L2Nu,
    WWTo1L1Nu2Q,
    WW,
    ZZTo2L2Nu,
    ZZTo2Q2L,
    ZZTo2Nu2Q,
    ZZTo4L,
    WZTo1L3Nu,
    WZTo1L1Nu2Q,
    WZTo2Q2L,
#    #WZTo3LNu,
    WZTo3LNu_amcatnlo,
    ]


# HT-binned
WJetsToLNu_HT70to100        = Sample.fromDirectory("WJetsToLNu_HT70to100",        "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205550/",        xSection=1596)
WJetsToLNu_HT70to100.normalization = 66569448.0 
WJetsToLNu_HT100to200       = Sample.fromDirectory("WJetsToLNu_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094143/",       xSection=1627.45)
WJetsToLNu_HT100to200.normalization = 51541593.0  
WJetsToLNu_HT200to400       = Sample.fromDirectory("WJetsToLNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205628/",       xSection=435.237)
WJetsToLNu_HT200to400.normalization = 58331446.0 
WJetsToLNu_HT400to600       = Sample.fromDirectory("WJetsToLNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205651/",       xSection=59.1811)
WJetsToLNu_HT400to600.normalization = 7444030.0
WJetsToLNu_HT600to800       = Sample.fromDirectory("WJetsToLNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205710/",       xSection=14.5805)
WJetsToLNu_HT600to800.normalization = 7718765.0
WJetsToLNu_HT800to1200      = Sample.fromDirectory("WJetsToLNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211124_205730/",      xSection=6.65621)
WJetsToLNu_HT800to1200.normalization = 7306187.0
WJetsToLNu_HT1200to2500     = Sample.fromDirectory("WJetsToLNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094211/", 	xSection=1.60809)
WJetsToLNu_HT1200to2500.normalization = 6481518.0 
WJetsToLNu_HT2500toInf      = Sample.fromDirectory("WJetsToLNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094237/",     xSection=0.0389136)
WJetsToLNu_HT2500toInf.normalization = 2097648.0 


wjets_ht = [
    WJetsToLNu_HT70to100,
    WJetsToLNu_HT100to200,
    WJetsToLNu_HT200to400,
    WJetsToLNu_HT400to600,
    WJetsToLNu_HT600to800,
    WJetsToLNu_HT800to1200,
    WJetsToLNu_HT1200to2500,
    WJetsToLNu_HT2500toInf,
    ]

#wjets += wjets_ht


signals = [
    ]



### QCD

## QCD HT bins (cross sections from McM)
QCD_HT50to100        = Sample.fromDirectory("QCD_HT50to100",        "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211126_152333/",           xSection=246400000.0)
QCD_HT50to100.normalization = 38599389.0 
QCD_HT100to200       = Sample.fromDirectory("QCD_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/220329_094328/",          xSection=27850000.0)
QCD_HT100to200.normalization = 84461486.0 
QCD_HT200to300       = Sample.fromDirectory("QCD_HT200to300",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211126_152354/",          xSection=1717000)
QCD_HT200to300.normalization = 57336623.0 
QCD_HT300to500       = Sample.fromDirectory("QCD_HT300to500",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/220329_094353/",          xSection=351300)
QCD_HT300to500.normalization = 61705174.0
QCD_HT500to700       = Sample.fromDirectory("QCD_HT500to700",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/211126_152420/",          xSection=31630)
QCD_HT500to700.normalization = 49184771.0 
QCD_HT700to1000      = Sample.fromDirectory("QCD_HT700to1000",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/211126_152446/",         xSection=6802)
QCD_HT700to1000.normalization = 48506751.0
QCD_HT1000to1500     = Sample.fromDirectory("QCD_HT1000to1500",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/220329_094420/",        xSection=1206)
QCD_HT1000to1500.normalization = 14527915.0 
QCD_HT1500to2000     = Sample.fromDirectory("QCD_HT1500to2000",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/220329_094446/",        xSection=120.4)
QCD_HT1500to2000.normalization = 10871473.0
QCD_HT2000toInf      = Sample.fromDirectory("QCD_HT2000toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/220329_094513/",         xSection=25.25)
QCD_HT2000toInf.normalization = 5374711.0

QCD_HT = [
    QCD_HT50to100,
    QCD_HT100to200,
    QCD_HT200to300,
    QCD_HT300to500,
    QCD_HT500to700,
    QCD_HT700to1000,
    QCD_HT1000to1500,
    QCD_HT1500to2000,
    QCD_HT2000toInf,
    ]
SMS_T2tt_mStop_500_mLSP_420      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_420",  "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094539/",  xSection=1.)
SMS_T2tt_mStop_500_mLSP_420.normalization = 985170.0 
SMS_T2tt_mStop_500_mLSP_450      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_450",  "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-450_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094603/",  xSection=1.)
SMS_T2tt_mStop_500_mLSP_450.normalization = 953022.0
SMS_T2tt_mStop_500_mLSP_470      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_470",  "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094629/",  xSection=1.)
SMS_T2tt_mStop_500_mLSP_470.normalization = 963822.0 

SMS_T2tt_LL_mStop_400_mLSP_380      = Sample.fromDirectory("SMS_T2tt_LL_mStop_400_mLSP_380",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094745/",             xSection=1.)
SMS_T2tt_LL_mStop_400_mLSP_380.normalization = 970219.0 
SMS_T2tt_LL_mStop_350_mLSP_335      = Sample.fromDirectory("SMS_T2tt_LL_mStop_350_mLSP_335",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-350_mLSP-335_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094719/",             xSection=1.)
SMS_T2tt_LL_mStop_350_mLSP_335.normalization = 957571.0 
SMS_T2tt_LL_mStop_300_mLSP_290      = Sample.fromDirectory("SMS_T2tt_LL_mStop_300_mLSP_290",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-300_mLSP-290_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/220329_094655/",             xSection=1.)
SMS_T2tt_LL_mStop_300_mLSP_290.normalization = 969691.0 

SMS_T2tt_mStop_500_mLSP_420_FS  = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_420_FS",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/230505_102038/",	xSection=1.)
SMS_T2tt_mStop_500_mLSP_420_FS.normalization = 1005259.0 
SMS_T2tt_mStop_500_mLSP_450_FS  = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_450_FS",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-450_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/230505_102105/",	xSection=1.)
SMS_T2tt_mStop_500_mLSP_450_FS.normalization = 1022738.0
SMS_T2tt_mStop_500_mLSP_470_FS  = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_470_FS",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/230505_102130/",	xSection=1.)
SMS_T2tt_mStop_500_mLSP_470_FS.normalization = 991031.0

SMS_T2tt_LL_mStop_400_mLSP_380_FS  = Sample.fromDirectory("SMS_T2tt_LL_mStop_400_mLSP_380_FS",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/230505_102012/",	xSection=1.)
SMS_T2tt_LL_mStop_400_mLSP_380_FS.normalization = 961969.0
SMS_T2tt_LL_mStop_350_mLSP_335_FS  = Sample.fromDirectory("SMS_T2tt_LL_mStop_350_mLSP_335_FS",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-350_mLSP-335_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/230505_101947/",	xSection=1.)
SMS_T2tt_LL_mStop_350_mLSP_335_FS.normalization = 999335.0
SMS_T2tt_LL_mStop_300_mLSP_290_FS  = Sample.fromDirectory("SMS_T2tt_LL_mStop_300_mLSP_290_FS",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-300_mLSP-290_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2_privateUL18nanov9/230505_100810/",	xSection=1.)
SMS_T2tt_LL_mStop_300_mLSP_290_FS.normalization = 961930.0

SMS_T2tt_mStop_250to1100_dM_10to30  = Sample.fromDirectory("SMS_T2tt_mStop_250to1100_dM_10to30",        "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_mStop-250To1100_dM-10to30_genHT-200_genMET-100_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/230505_102155/", xSection=1.)
SMS_T2tt_mStop_250to1100_dM_10to30.normalization = 46568476.0 

SMS_T2tt_mStop_250to1100_dM_10to30_LL  = Sample.fromDirectory("SMS_T2tt_mStop_250to1100_dM_10to30_LL",  "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-250To1100_dM-10To30_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v1_privateUL18nanov9/230505_102223/", xSection=1.)
SMS_T2tt_mStop_250to1100_dM_10to30_LL.normalization = 76581113.0 

compSUSY = [
		SMS_T2tt_mStop_500_mLSP_420,
		SMS_T2tt_mStop_500_mLSP_450,
		SMS_T2tt_mStop_500_mLSP_470,
		SMS_T2tt_LL_mStop_400_mLSP_380,
		SMS_T2tt_LL_mStop_350_mLSP_335,
		SMS_T2tt_LL_mStop_300_mLSP_290,
		SMS_T2tt_mStop_500_mLSP_420_FS,
		SMS_T2tt_mStop_500_mLSP_450_FS,
		SMS_T2tt_mStop_500_mLSP_470_FS,
		SMS_T2tt_LL_mStop_400_mLSP_380_FS,
		SMS_T2tt_LL_mStop_350_mLSP_335_FS,
		SMS_T2tt_LL_mStop_300_mLSP_290_FS,
		SMS_T2tt_mStop_250to1100_dM_10to30,
		SMS_T2tt_mStop_250to1100_dM_10to30_LL,
		]

allSamples = DY + top + boson + wjets_ht + signals + QCD_HT + compSUSY 

for s in allSamples:
    
    s.isData = False
    for i_f, f in enumerate(s.files):
	    if f.startswith('/eos/'):
		    s.files[i_f] = 'root://eos.grid.vbc.ac.at/'+f

