'''
miniAOD samples of Summer20UL16 campaign, miniAOD (106X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer20UL16MiniAOD*106X*/MINIAODSIM"
'''
                                                                                                                                                                                                            
import copy, os, sys
from RootTools.fwlite.FWLiteSample import FWLiteSample
import ROOT

def get_parser():
	import argparse
	argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
	argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
	return argParser

# Logging
if __name__=="__main__":
	import Samples.Tools.logger as logger
	logger = logger.get_logger("INFO", logFile = None )
	import RootTools.core.logger as logger_rt
	logger_rt = logger_rt.get_logger("INFO", logFile = None )
	options = get_parser().parse_args()
	ov = options.overwrite

else:
	import logging
	logger = logging.getLogger(__name__)
	ov = False

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"Summer20UL16_miniAODAPVv2.sql"

logger.info("Using db file: %s", dbFile)


##WJets_HT
WJetsToLNu_HT70To100             = FWLiteSample.fromDAS("WJetsToLNu_HT70To100",    "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT100To200            = FWLiteSample.fromDAS("WJetsToLNu_HT100To200",   "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200To400            = FWLiteSample.fromDAS("WJetsToLNu_HT200To400",   "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT400To600            = FWLiteSample.fromDAS("WJetsToLNu_HT400To600",   "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT600To800            = FWLiteSample.fromDAS("WJetsToLNu_HT600To800",   "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT800To1200           = FWLiteSample.fromDAS("WJetsToLNu_HT800To1200",  "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT1200To2500          = FWLiteSample.fromDAS("WJetsToLNu_HT1200To2500", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT2500ToInf           = FWLiteSample.fromDAS("WJetsToLNu_HT2500ToInf",  "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsToLNu                              = FWLiteSample.fromDAS("WJetsToLNu",	   "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsToLNu_HT = [
		WJetsToLNu,
		WJetsToLNu_HT70To100,
		WJetsToLNu_HT100To200,
		WJetsToLNu_HT200To400,
		WJetsToLNu_HT400To600,
		WJetsToLNu_HT600To800,
		WJetsToLNu_HT800To1200,
		WJetsToLNu_HT1200To2500,
		WJetsToLNu_HT2500ToInf,
]
##TTJets
TTLep_pow			= FWLiteSample.fromDAS("TTLep_pow", 	  "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTSingleLep_pow			= FWLiteSample.fromDAS("TTSingleLep_pow", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#TTbar                                  = FWLiteSample.fromDAS("TTbar",                 "",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets = [ TTLep_pow, TTSingleLep_pow ]#,TTbar]

###ZInv
ZJetsToNuNu_HT100To200		= FWLiteSample.fromDAS("ZJetsToNuNu_HT100To200",   "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT200To400		= FWLiteSample.fromDAS("ZJetsToNuNu_HT200To400",   "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT400To600		= FWLiteSample.fromDAS("ZJetsToNuNu_HT400To600",   "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT600To800		= FWLiteSample.fromDAS("ZJetsToNuNu_HT600To800",   "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT800To1200		= FWLiteSample.fromDAS("ZJetsToNuNu_HT800To1200",  "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT1200To2500	= FWLiteSample.fromDAS("ZJetsToNuNu_HT1200To2500", "/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT2500ToInf		= FWLiteSample.fromDAS("ZJetsToNuNu_HT2500ToInf",  "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZJetsToNuNu = [
		ZJetsToNuNu_HT100To200,
		ZJetsToNuNu_HT200To400,
		ZJetsToNuNu_HT400To600,
		ZJetsToNuNu_HT600To800,
		ZJetsToNuNu_HT800To1200,
		ZJetsToNuNu_HT1200To2500,
		ZJetsToNuNu_HT2500ToInf,
		]

###DiBoson
WWTo2L2Nu		= FWLiteSample.fromDAS("WWTo2L2Nu", 	 "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WW                      = FWLiteSample.fromDAS("WW",	   	 "/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WWTo1L1Nu2Q_4f		= FWLiteSample.fromDAS("WWTo1L1Nu2Q_4f", "/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WZTo1L1Nu2Q_4f_NLO	= FWLiteSample.fromDAS("WZTo1L1Nu2Q_4f_NLO", "/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo1L3Nu_4f_NLO	= FWLiteSample.fromDAS("WZTo1L3Nu_4f_NLO",   "/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo2Q2L_NLO		= FWLiteSample.fromDAS("WZTo2Q2L_NLO",   "/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_NLO		= FWLiteSample.fromDAS("WZTo3LNu_NLO",   "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZZTo2L2Nu		= FWLiteSample.fromDAS("ZZTo2L2Nu", 	"/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2Q2L		= FWLiteSample.fromDAS("ZZTo2Q2L", 	"/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo2Nu2Q_5f		= FWLiteSample.fromDAS("ZZTo2Q2Nu_5f", 	"/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZZTo4L			= FWLiteSample.fromDAS("ZZTo4L", 	"/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

diBoson = [
	   WWTo2L2Nu,
	   WW,
	   WWTo1L1Nu2Q_4f,
	   WZTo1L1Nu2Q_4f_NLO,
	   WZTo1L3Nu_4f_NLO,
	   WZTo2Q2L_NLO,
	   WZTo3LNu_NLO,
	   ZZTo2L2Nu,
	   ZZTo2Q2L,
	   ZZTo2Nu2Q_5f,
	   ZZTo4L,
	   ]

###DY
DYJetsToLL_M50_LO                      = FWLiteSample.fromDAS("DYJetsToLL_M50_LO",     "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M10to50_LO                  = FWLiteSample.fromDAS("DYJetsToLL_M10to50_LO", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)


DYJetsToLL_M4to50_HT100to200		= FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT100to200", "/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT200to400		= FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT200to400", "/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT400to600		= FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT400to600", "/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M4to50_HT600toInf		= FWLiteSample.fromDAS("DYJetsToLL_M4to50_HT600toInf", "/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)


DYJetsToLL_M50_HT70to100		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT70to100", 	"/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200", 	"/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT200to400		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400", 	"/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600", 	"/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT600to800		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT600to800", 	"/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT800to1200		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT800to1200", 	"/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT1200to2500		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT1200to2500", 	"/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT2500toInf		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT2500toInf", 	"/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY_HT= [
	DYJetsToLL_M50_LO,
	DYJetsToLL_M10to50_LO,
	DYJetsToLL_M4to50_HT100to200,
	DYJetsToLL_M4to50_HT200to400,
	DYJetsToLL_M4to50_HT400to600,
	DYJetsToLL_M4to50_HT600toInf,

	DYJetsToLL_M50_HT70to100,
	DYJetsToLL_M50_HT100to200,
	DYJetsToLL_M50_HT200to400,
	DYJetsToLL_M50_HT400to600,
	DYJetsToLL_M50_HT600to800,
	DYJetsToLL_M50_HT800to1200,
	DYJetsToLL_M50_HT1200to2500,
	DYJetsToLL_M50_HT2500toInf,
	]

###singleTop
ST_tchannel_top_4f_pow		= FWLiteSample.fromDAS("ST_tchannel_top_4f_pow", 	  "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tchannel_antitop_4f_pow	= FWLiteSample.fromDAS("ST_tchannel_antitop_4f_pow", 	  "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow 	= FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow",     "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 			dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_NoFullyHad_5f_pow = FWLiteSample.fromDAS("ST_tW_antitop_NoFullyHad_5f_pow", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

singleTop = [
	     ST_tchannel_top_4f_pow,
	     ST_tchannel_antitop_4f_pow,
	     ST_tW_top_NoFullyHad_5f_pow,
	     ST_tW_antitop_NoFullyHad_5f_pow,
		]

##ttX
TTGJets_NLO			= FWLiteSample.fromDAS("TTGJets_NLO", 	    "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttWJetsToLNu_NLO		= FWLiteSample.fromDAS("ttWJetsToLNu_NLO",  "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttWJetsToQQ_NLO			= FWLiteSample.fromDAS("ttWJetsToQQ_NLO",   "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttWJets_LO			= FWLiteSample.fromDAS("ttWJets_LO", 	    "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttZJets_LO			= FWLiteSample.fromDAS("ttZJets_LO", 	    "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttX = [TTGJets_NLO, ttWJetsToLNu_NLO , ttWJetsToQQ_NLO ,ttWJets_LO, ttZJets_LO, ]
#
###QCD
QCD_HT50to100			= FWLiteSample.fromDAS("QCD_HT50to100",     	     "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT50to100_madgraph		= FWLiteSample.fromDAS("QCD_HT50to100_madgraph",     "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT100to200			= FWLiteSample.fromDAS("QCD_HT100to200",    	     "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT100to200_madgraph		= FWLiteSample.fromDAS("QCD_HT100to200_madgraph",    "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT200to300_madgraph		= FWLiteSample.fromDAS("QCD_HT200to300_madgraph",    "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT300to500			= FWLiteSample.fromDAS("QCD_HT300to500",    	     "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT300to500_madgraph		= FWLiteSample.fromDAS("QCD_HT300to500_madgraph",    "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT500to700			= FWLiteSample.fromDAS("QCD_HT500to700",    	     "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT500to700_madgraph		= FWLiteSample.fromDAS("QCD_HT500to700_madgraph",    "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT700to1000			= FWLiteSample.fromDAS("QCD_HT700to1000",   "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT700to1000_madgraph	= FWLiteSample.fromDAS("QCD_HT700to1000_madgraph",   "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT1000to1500		= FWLiteSample.fromDAS("QCD_HT1000to1500",  	     "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT1000to1500_madgraph	= FWLiteSample.fromDAS("QCD_HT1000to1500_madragph",  "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT1500to2000		= FWLiteSample.fromDAS("QCD_HT1500to2000",  	     "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT1500to2000_madgraph	= FWLiteSample.fromDAS("QCD_HT1500to2000_madgraph",  "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT2000toInf			= FWLiteSample.fromDAS("QCD_HT2000toInf",   	     "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT2000toInf_madgraph	= FWLiteSample.fromDAS("QCD_HT2000toInf_madgraph",   "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

QCD_HT = [
	QCD_HT50to100,
	QCD_HT50to100_madgraph,
	QCD_HT100to200,
	QCD_HT100to200_madgraph,
	QCD_HT200to300_madgraph,
	QCD_HT300to500,
	QCD_HT300to500_madgraph,
	QCD_HT500to700,
	QCD_HT500to700_madgraph,
	QCD_HT700to1000,
	QCD_HT700to1000_madgraph,
	QCD_HT1000to1500,
	QCD_HT1000to1500_madgraph,
	QCD_HT1500to2000,
	QCD_HT1500to2000_madgraph,
	QCD_HT2000toInf,
	QCD_HT2000toInf_madgraph,
	]
###QCD_Pt

QCD_pt15to30                            = FWLiteSample.fromDAS("QCD_pt15to30",          "/QCD_Pt_15to30_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt30to50                            = FWLiteSample.fromDAS("QCD_pt30to50",          "/QCD_Pt_30to50_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt50to80                            = FWLiteSample.fromDAS("QCD_pt50to80",          "/QCD_Pt_50to80_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt80to120                           = FWLiteSample.fromDAS("QCD_pt80to120",         "/QCD_Pt_80to120_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",    dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt120to170                          = FWLiteSample.fromDAS("QCD_pt120to170",        "/QCD_Pt_120to170_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt170to300                          = FWLiteSample.fromDAS("QCD_pt170to300",        "/QCD_Pt_170to300_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt300to470                          = FWLiteSample.fromDAS("QCD_pt300to470",        "/QCD_Pt_300to470_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt470to600                          = FWLiteSample.fromDAS("QCD_pt470to600",        "/QCD_Pt_470to600_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt600to800                          = FWLiteSample.fromDAS("QCD_pt600to800",        "/QCD_Pt_600to800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt800to1000                         = FWLiteSample.fromDAS("QCD_pt800to1000",       "/QCD_Pt_800to1000_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt1000to1400                        = FWLiteSample.fromDAS("QCD_pt1000to1400",      "/QCD_Pt_1000to1400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",         dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt1400to1800                        = FWLiteSample.fromDAS("QCD_pt1400to1800",      "/QCD_Pt_1400to1800_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",         dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt1800to2400                        = FWLiteSample.fromDAS("QCD_pt1800to2400",      "/QCD_Pt_1800to2400_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",         dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt2400to3200                        = FWLiteSample.fromDAS("QCD_pt2400to3200",      "/QCD_Pt_2400to3200_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",         dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_pt3200toInf                         = FWLiteSample.fromDAS("QCD_pt3200toInf",       "/QCD_Pt_3200toInf_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)


#QCD_Mu_pt15to20                         = FWLiteSample.fromDAS("QCD_Mu_pt15to20",       "",       dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt20to30                         = FWLiteSample.fromDAS("QCD_Mu_pt20to30",       "",       dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt30to50                         = FWLiteSample.fromDAS("QCD_Mu_pt30to50",       "",       dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_Mu_pt50to80                         = FWLiteSample.fromDAS("QCD_Mu_pt50to80",       "/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",       dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt80to120                        = FWLiteSample.fromDAS("QCD_Mu_pt80to120",      "",      dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt120to170                       = FWLiteSample.fromDAS("QCD_Mu_pt120to170",     "",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt170to300                       = FWLiteSample.fromDAS("QCD_Mu_pt170to300",     "",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt300to470                       = FWLiteSample.fromDAS("QCD_Mu_pt300to470",     "",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt470to600                       = FWLiteSample.fromDAS("QCD_Mu_pt470to600",     "",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt600to800                       = FWLiteSample.fromDAS("QCD_Mu_pt600to800",     "",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_Mu_pt800to1000                      = FWLiteSample.fromDAS("QCD_Mu_pt800to1000",    "",    dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

#QCD_EMEnriched_pt30to50                         = FWLiteSample.fromDAS("QCD_EMEnriched_pt30to50",       "",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_EMEnriched_pt50to80                         = FWLiteSample.fromDAS("QCD_EMEnriched_pt50to80",       "",  dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_EMEnriched_pt80to120                        = FWLiteSample.fromDAS("QCD_EMEnriched_pt80to120",      "",         dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_EMEnriched_pt120to170                       = FWLiteSample.fromDAS("QCD_EMEnriched_pt120to170",     "",        dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_EMEnriched_pt170to300                       = FWLiteSample.fromDAS("QCD_EMEnriched_pt170to300",     "",        dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#QCD_EMEnriched_pt300toInf                       = FWLiteSample.fromDAS("QCD_EMEnriched_pt300toInf",     "",        dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
    

#QCD_bcToE_pt15to20                     = FWLiteSample.fromDAS("QCD_bcToE_pt15to20",    "",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bcToE_pt20to30                      = FWLiteSample.fromDAS("QCD_bcToE_pt20to30",    "/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",       dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bcToE_pt30to80                      = FWLiteSample.fromDAS("QCD_bcToE_pt30to80",    "/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",       dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bcToE_pt80to170                     = FWLiteSample.fromDAS("QCD_bcToE_pt80to170",   "/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",      dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bcToE_pt170to250                    = FWLiteSample.fromDAS("QCD_bcToE_pt170to250",  "/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_bcToE_pt250toInf                    = FWLiteSample.fromDAS("QCD_bcToE_pt250toInf",  "/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",     dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

QCD_Pt = [
	QCD_bcToE_pt20to30,
	QCD_bcToE_pt30to80,
	QCD_bcToE_pt80to170,
        QCD_bcToE_pt170to250,
        QCD_bcToE_pt250toInf,
        #QCD_EMEnriched_pt30to50,
        #QCD_EMEnriched_pt50to80,
	#QCD_EMEnriched_pt80to120,
	#QCD_EMEnriched_pt120to170,
	#QCD_EMEnriched_pt170to300,
	#QCD_EMEnriched_pt300toInf,
	#QCD_Mu_pt15to20,
	#QCD_Mu_pt20to30,
	#QCD_Mu_pt30to50,
	QCD_Mu_pt50to80,
	#QCD_Mu_pt80to120,
	#QCD_Mu_pt120to170,
	#QCD_Mu_pt170to300,
	#QCD_Mu_pt300to470,
	#QCD_Mu_pt470to600,
	#QCD_Mu_pt600to800,
	#QCD_Mu_pt800to1000,
	QCD_pt15to30,
	QCD_pt30to50,
	QCD_pt50to80,
	QCD_pt80to120,
	QCD_pt120to170,
	QCD_pt170to300,
	QCD_pt300to470,
	QCD_pt470to600,
	QCD_pt600to800,
	QCD_pt800to1000,
	QCD_pt1000to1400,
	QCD_pt1400to1800,
	QCD_pt1800to2400,
	QCD_pt2400to3200,
	QCD_pt3200toInf,
	]       
SMS_T2tt_mStop_500_mLSP_420	= FWLiteSample.fromDAS("SMS_T2tt_mStop_500_mLSP_420",	"/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_500_mLSP_450	= FWLiteSample.fromDAS("SMS_T2tt_mStop_500_mLSP_450",	"/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-450_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SMS_T2tt_mStop_500_mLSP_470	= FWLiteSample.fromDAS("SMS_T2tt_mStop_500_mLSP_470",	"/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM",	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

compSUSY = [
        SMS_T2tt_mStop_500_mLSP_420,
        SMS_T2tt_mStop_500_mLSP_450,
        SMS_T2tt_mStop_500_mLSP_470,
                ]


allSamples = WJetsToLNu_HT + TTJets + ZJetsToNuNu + diBoson + DY_HT + singleTop + ttX + QCD_HT + QCD_Pt + compSUSY
for sample in allSamples:
	sample.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )

