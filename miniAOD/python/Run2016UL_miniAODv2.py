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
dbFile = dbDir+"DB_Run2016UL_miniAODv2.sql"

logger.info("Using db file: %s", dbFile)

# MET
MET_Run2016B_ULHIPM_ver1  =   FWLiteSample.fromDAS("MET_Run2016B_ULHIPM_ver1",  "/MET/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016B_ULHIPM_ver2  =   FWLiteSample.fromDAS("MET_Run2016B_ULHIPM_ver2",  "/MET/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016C_ULHIPM       =   FWLiteSample.fromDAS("MET_Run2016C_ULHIPM",	"/MET/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016D_ULHIPM       =   FWLiteSample.fromDAS("MET_Run2016D_ULHIPM",   	"/MET/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016E_ULHIPM       =   FWLiteSample.fromDAS("MET_Run2016E_ULHIPM",   	"/MET/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016F_UL       	  =   FWLiteSample.fromDAS("MET_Run2016F_UL",	    	"/MET/Run2016F-UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016F_ULHIPM  	  =   FWLiteSample.fromDAS("MET_Run2016F_ULHIPM",   	"/MET/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016G_UL       	  =   FWLiteSample.fromDAS("MET_Run2016G_UL",	    	"/MET/Run2016G-UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016H_UL       	  =   FWLiteSample.fromDAS("MET_Run2016H_UL",	    	"/MET/Run2016H-UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [\
    MET_Run2016B_ULHIPM_ver1,
    MET_Run2016B_ULHIPM_ver2,
    MET_Run2016C_ULHIPM,
    MET_Run2016D_ULHIPM,
    MET_Run2016E_ULHIPM,
    MET_Run2016F_UL,
    MET_Run2016F_ULHIPM,
    MET_Run2016G_UL,
    MET_Run2016H_UL,
]

JetHT_Run2016B_ULHIPM_ver1 = FWLiteSample.fromDAS("JetHT_Run2016B_ULHIPM_ver1",  "/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016B_ULHIPM_ver2 = FWLiteSample.fromDAS("JetHT_Run2016B_ULHIPM_ver2",  "/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016C_ULHIPM	   = FWLiteSample.fromDAS("JetHT_Run2016C_ULHIPM",  	 "/JetHT/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016D_ULHIPM	   = FWLiteSample.fromDAS("JetHT_Run2016D_ULHIPM",  	 "/JetHT/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016E_ULHIPM	   = FWLiteSample.fromDAS("JetHT_Run2016E_ULHIPM",  	 "/JetHT/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016F_ULHIPM	   = FWLiteSample.fromDAS("JetHT_Run2016F_ULHIPM",  	 "/JetHT/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016F_UL	   = FWLiteSample.fromDAS("JetHT_Run2016F_UL",  	 "/JetHT/Run2016F-UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016G_UL	   = FWLiteSample.fromDAS("JetHT_Run2016G_UL",  	 "/JetHT/Run2016G-UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2016H_UL	   = FWLiteSample.fromDAS("JetHT_Run2016H_UL",  	 "/JetHT/Run2016H-UL2016_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

JetHT = [\
	JetHT_Run2016B_ULHIPM_ver1,
	JetHT_Run2016B_ULHIPM_ver2,
	JetHT_Run2016C_ULHIPM,
	JetHT_Run2016D_ULHIPM,
	JetHT_Run2016E_ULHIPM,
	JetHT_Run2016F_ULHIPM,
	JetHT_Run2016F_UL,
	JetHT_Run2016G_UL,
	JetHT_Run2016H_UL,
	]

DoubleEG_Run2016B_ULHIPM_ver1 = FWLiteSample.fromDAS("DoubleEG_Run2016B_ULHIPM_ver1",  "/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v1/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016B_ULHIPM_ver2 = FWLiteSample.fromDAS("DoubleEG_Run2016B_ULHIPM_ver2",  "/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v3/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016C_ULHIPM      = FWLiteSample.fromDAS("DoubleEG_Run2016C_ULHIPM",       "/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016D_ULHIPM      = FWLiteSample.fromDAS("DoubleEG_Run2016D_ULHIPM",       "/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016E_ULHIPM      = FWLiteSample.fromDAS("DoubleEG_Run2016E_ULHIPM",       "/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016F_ULHIPM      = FWLiteSample.fromDAS("DoubleEG_Run2016F_ULHIPM",       "/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016F_UL	      = FWLiteSample.fromDAS("DoubleEG_Run2016F_UL",  	       "/DoubleEG/Run2016F-UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016G_UL	      = FWLiteSample.fromDAS("DoubleEG_Run2016G_UL",	       "/DoubleEG/Run2016G-UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2016H_UL	      = FWLiteSample.fromDAS("DoubleEG_Run2016H_UL",  	       "/DoubleEG/Run2016H-UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleEG = [\
	DoubleEG_Run2016B_ULHIPM_ver1,
	DoubleEG_Run2016B_ULHIPM_ver2,
	DoubleEG_Run2016C_ULHIPM,
	DoubleEG_Run2016D_ULHIPM,
	DoubleEG_Run2016E_ULHIPM,
	DoubleEG_Run2016F_ULHIPM,
	DoubleEG_Run2016F_UL,
	DoubleEG_Run2016G_UL,
	DoubleEG_Run2016H_UL,
	]

DoubleMuon_Run2016B_ULHIPM_ver1 = FWLiteSample.fromDAS("DoubleMuon_Run2016B_ULHIPM_ver1",  		"/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v1/MINIAOD",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016B_ULHIPM_ver2 = FWLiteSample.fromDAS("DoubleMuon_Run2016B_ULHIPM_ver2",  		"/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v1/MINIAOD",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016C_ULHIPM      = FWLiteSample.fromDAS("DoubleMuon_Run2016C_ULHIPM",       		"/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v1/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016D_ULHIPM      = FWLiteSample.fromDAS("DoubleMuon_Run2016D_ULHIPM",       		"/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v1/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016E_ULHIPM      = FWLiteSample.fromDAS("DoubleMuon_Run2016E_ULHIPM",       		"/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v1/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016F_ULHIPM      = FWLiteSample.fromDAS("DoubleMuon_Run2016F_ULHIPM",       		"/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v1/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016F_UL	        = FWLiteSample.fromDAS("DoubleMuon_Run2016F_UL",  	       		"/DoubleMuon/Run2016F-UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016G_UL	        = FWLiteSample.fromDAS("DoubleMuon_Run2016G_UL",	       		"/DoubleMuon/Run2016G-UL2016_MiniAODv2-v1/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2016H_UL	        = FWLiteSample.fromDAS("DoubleMuon_Run2016H_UL",  	       		"/DoubleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleMuon = [\
	DoubleMuon_Run2016B_ULHIPM_ver1,
	DoubleMuon_Run2016B_ULHIPM_ver2,
	DoubleMuon_Run2016C_ULHIPM,
	DoubleMuon_Run2016D_ULHIPM,
	DoubleMuon_Run2016E_ULHIPM,
	DoubleMuon_Run2016F_ULHIPM,
	DoubleMuon_Run2016F_UL,
	DoubleMuon_Run2016G_UL,
	DoubleMuon_Run2016H_UL,
	]

SingleMuon_Run2016B_ULHIPM_ver1 = FWLiteSample.fromDAS("SingleMuon_Run2016B_ULHIPM_ver1",  		"/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2-v2/MINIAOD",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016B_ULHIPM_ver2 = FWLiteSample.fromDAS("SingleMuon_Run2016B_ULHIPM_ver2",  		"/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2/MINIAOD",   dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016C_ULHIPM      = FWLiteSample.fromDAS("SingleMuon_Run2016C_ULHIPM",       		"/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2-v2/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016D_ULHIPM      = FWLiteSample.fromDAS("SingleMuon_Run2016D_ULHIPM",       		"/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2-v2/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016E_ULHIPM      = FWLiteSample.fromDAS("SingleMuon_Run2016E_ULHIPM",       		"/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2-v2/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016F_ULHIPM      = FWLiteSample.fromDAS("SingleMuon_Run2016F_ULHIPM",       		"/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2-v2/MINIAOD", 	dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016F_UL	        = FWLiteSample.fromDAS("SingleMuon_Run2016F_UL",  	       		"/SingleMuon/Run2016F-UL2016_MiniAODv2-v2/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016G_UL	        = FWLiteSample.fromDAS("SingleMuon_Run2016G_UL",	       		"/SingleMuon/Run2016G-UL2016_MiniAODv2-v2/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2016H_UL	        = FWLiteSample.fromDAS("SingleMuon_Run2016H_UL",  	       		"/SingleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD", 		dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SingleMuon = [\
	SingleMuon_Run2016B_ULHIPM_ver1,
	SingleMuon_Run2016B_ULHIPM_ver2,
	SingleMuon_Run2016C_ULHIPM,
	SingleMuon_Run2016D_ULHIPM,
	SingleMuon_Run2016E_ULHIPM,
	SingleMuon_Run2016F_ULHIPM,
	SingleMuon_Run2016F_UL,
	SingleMuon_Run2016G_UL,
	SingleMuon_Run2016H_UL,
	]
## add up all samples
allSamples = MET + JetHT + DoubleEG + DoubleMuon + SingleMuon

for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
