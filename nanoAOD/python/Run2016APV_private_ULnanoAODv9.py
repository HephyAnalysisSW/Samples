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
    ROOT.PyConfig.IgnoreCommandLineOptions = True
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


# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    if "clip" in os.getenv("HOSTNAME").lower():
        if __name__ == "__main__" and not options.check_completeness:
            from Samples.Tools.config import redirector_global as redirector
        else:
            from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

## DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Run2016APV_ULnanoAODv2.sql'
logger.info("Using db file: %s", dbFile)


# MET
#MET_Run2016B_ver1_UL  = Sample.fromDirectory("MET_Run2016B_ver1_UL",   "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016B-21Feb2020_ver1_UL2016_HIPM-v1_privateULRun2017v1_nanov2/")
MET_Run2016B_ver2_HIPM_UL  = Sample.fromDirectory("MET_Run2016B_ver2_HIPM_UL",   "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211129_210626/0000/"  )
MET_Run2016C_HIPM_UL       = Sample.fromDirectory("MET_Run2016C_HIPM_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016C-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211129_210644/"  )
MET_Run2016D_HIPM_UL       = Sample.fromDirectory("MET_Run2016D_HIPM_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016D-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211129_210703/"  )
MET_Run2016E_HIPM_UL       = Sample.fromDirectory("MET_Run2016E_HIPM_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016E-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211129_210723/"  )
MET_Run2016F_HIPM_UL  	   = Sample.fromDirectory("MET_Run2016F_HIPM_UL",   	 "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016F-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211129_210806/"  )
#MET_Run2016F_UL       	   = Sample.fromDirectory("MET_Run2016F_UL",        	 "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016F-UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211129_210746/"  )
#MET_Run2016G_UL       	   = Sample.fromDirectory("MET_Run2016G_UL",        	 "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016G-UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211129_210837/"  )
#MET_Run2016H_UL       	   = Sample.fromDirectory("MET_Run2016H_UL",        	 "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016H-UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211129_210859/"  )

MET = [
    MET_Run2016B_ver2_HIPM_UL,
    MET_Run2016C_HIPM_UL,
    MET_Run2016D_HIPM_UL,
    MET_Run2016E_HIPM_UL,
    MET_Run2016F_HIPM_UL,
#    MET_Run2016F_UL,
#    MET_Run2016G_UL,
#    MET_Run2016H_UL,
]

JetHT_Run2016B_ver2_HIPM_UL  = Sample.fromDirectory("JetHT_Run2016B_ver2_HIPM_UL",   "/eos/vbc/experiments/cms/store/user/prhussai/JetHT/crab_Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171458/"  )
JetHT_Run2016C_HIPM_UL       = Sample.fromDirectory("JetHT_Run2016C_HIPM_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/JetHT/crab_Run2016C-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171516/"  )
JetHT_Run2016D_HIPM_UL       = Sample.fromDirectory("JetHT_Run2016D_HIPM_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/JetHT/crab_Run2016D-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171532/"  )
JetHT_Run2016E_HIPM_UL       = Sample.fromDirectory("JetHT_Run2016E_HIPM_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/JetHT/crab_Run2016E-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171547/"  )
JetHT_Run2016F_HIPM_UL	     = Sample.fromDirectory("JetHT_Run2016F_HIPM_UL",	     "/eos/vbc/experiments/cms/store/user/prhussai/JetHT/crab_Run2016F-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171605/"  )


JetHT = [
    JetHT_Run2016B_ver2_HIPM_UL,
    JetHT_Run2016C_HIPM_UL,
    JetHT_Run2016D_HIPM_UL,
    JetHT_Run2016E_HIPM_UL,
    JetHT_Run2016F_HIPM_UL,
    ]


# SingleMuon
SingleMuon_Run2016B_ver2_HIPM_UL	= Sample.fromDirectory("SingleMuon_Run2016B_ver2_HIPM_UL",		"/eos/vbc/experiments/cms/store/user/prhussai/SingleMuon/crab_Run2016B-ver2_HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171244/")
SingleMuon_Run2016C_HIPM_UL	        = Sample.fromDirectory("SingleMuon_Run2016C_HIPM_UL",		    "/eos/vbc/experiments/cms/store/user/prhussai/SingleMuon/crab_Run2016C-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171301/")
SingleMuon_Run2016D_HIPM_UL	        = Sample.fromDirectory("SingleMuon_Run2016D_HIPM_UL",		    "/eos/vbc/experiments/cms/store/user/prhussai/SingleMuon/crab_Run2016D-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171317/")
SingleMuon_Run2016E_HIPM_UL	        = Sample.fromDirectory("SingleMuon_Run2016E_HIPM_UL",		    "/eos/vbc/experiments/cms/store/user/prhussai/SingleMuon/crab_Run2016E-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171334/")
SingleMuon_Run2016F_HIPM_UL	        = Sample.fromDirectory("SingleMuon_Run2016F_HIPM_UL",		    "/eos/vbc/experiments/cms/store/user/prhussai/SingleMuon/crab_Run2016F-HIPM_UL2016_MiniAODv2-v2_privateULRun2016v1_nanov9/211217_171351/")

SingleMuon = [
    SingleMuon_Run2016B_ver2_HIPM_UL,
    SingleMuon_Run2016C_HIPM_UL,
    SingleMuon_Run2016D_HIPM_UL,
    SingleMuon_Run2016E_HIPM_UL,
    SingleMuon_Run2016F_HIPM_UL
]

# DoubleMuon
DoubleMuon_Run2016B_ver2_HIPM_UL  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_ver2_HIPM_UL",   "/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016C_HIPM_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_HIPM_UL",        "/DoubleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016D_HIPM_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_HIPM_UL",        "/DoubleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016E_HIPM_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_HIPM_UL",        "/DoubleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016F_HIPM_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_HIPM_UL",        "/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2016B_ver2_HIPM_UL,
    DoubleMuon_Run2016C_HIPM_UL,
    DoubleMuon_Run2016D_HIPM_UL,
    DoubleMuon_Run2016E_HIPM_UL,
    DoubleMuon_Run2016F_HIPM_UL
]

# SingleElectron from DAS
SingleElectron_Run2016B_ver2_HIPM_UL  = Sample.nanoAODfromDAS("SingleElectron_Run2016B_ver2_HIPM_UL",   "/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016C_HIPM_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016C_HIPM_UL",        "/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016D_HIPM_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016D_HIPM_UL",        "/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016E_HIPM_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016E_HIPM_UL",        "/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016F_HIPM_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016F_HIPM_UL",        "/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleElectron = [
    SingleElectron_Run2016B_ver2_HIPM_UL,
    SingleElectron_Run2016C_HIPM_UL,
    SingleElectron_Run2016D_HIPM_UL,
    SingleElectron_Run2016E_HIPM_UL,
    SingleElectron_Run2016F_HIPM_UL
]

# DoubleEG
DoubleEG_Run2016B_ver2_HIPM_UL  = Sample.nanoAODfromDAS("DoubleEG_Run2016B_ver2_HIPM_UL",   "/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v3/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016C_HIPM_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016C_HIPM_UL",        "/DoubleEG/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016D_HIPM_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016D_HIPM_UL",        "/DoubleEG/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016E_HIPM_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016E_HIPM_UL",        "/DoubleEG/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016F_HIPM_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016F_HIPM_UL",        "/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleEG = [
    DoubleEG_Run2016B_ver2_HIPM_UL,
    DoubleEG_Run2016C_HIPM_UL,
    DoubleEG_Run2016D_HIPM_UL,
    DoubleEG_Run2016E_HIPM_UL,
    DoubleEG_Run2016F_HIPM_UL
]

allSamples =  MET + JetHT + SingleMuon + SingleElectron + DoubleMuon + DoubleEG

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt")
    s.isData    = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 ) 