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
dbFile = dbDir+"DB_Run2018UL_miniAODv2.sql"

logger.info("Using db file: %s", dbFile)

# MET
MET_Run2018A_UL  =   FWLiteSample.fromDAS("MET_Run2018A_UL",  "/MET/Run2018A-UL2018_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018B_UL  =   FWLiteSample.fromDAS("MET_Run2018B_UL",  "/MET/Run2018B-UL2018_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018C_UL  =   FWLiteSample.fromDAS("MET_Run2018C_UL",  "/MET/Run2018C-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018D_UL  =   FWLiteSample.fromDAS("MET_Run2018D_UL",  "/MET/Run2018D-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [\
    MET_Run2018A_UL,
    MET_Run2018B_UL,
    MET_Run2018C_UL,
    MET_Run2018D_UL,
]

JetHT_Run2018A_UL  =   FWLiteSample.fromDAS("JetHT_Run2018A_UL",  "/JetHT/Run2018A-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018B_UL  =   FWLiteSample.fromDAS("JetHT_Run2018B_UL",  "/JetHT/Run2018B-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018C_UL  =   FWLiteSample.fromDAS("JetHT_Run2018C_UL",  "/JetHT/Run2018C-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2018D_UL  =   FWLiteSample.fromDAS("JetHT_Run2018D_UL",  "/JetHT/Run2018D-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

JetHT = [\
    JetHT_Run2018A_UL,
    JetHT_Run2018B_UL,
    JetHT_Run2018C_UL,
    JetHT_Run2018D_UL,
]

EGamma_Run2018A_UL  =   FWLiteSample.fromDAS("EGamma_Run2018A_UL",  "/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018B_UL  =   FWLiteSample.fromDAS("EGamma_Run2018B_UL",  "/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018C_UL  =   FWLiteSample.fromDAS("EGamma_Run2018C_UL",  "/EGamma/Run2018C-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
EGamma_Run2018D_UL  =   FWLiteSample.fromDAS("EGamma_Run2018D_UL",  "/EGamma/Run2018D-UL2018_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

EGamma = [\
    EGamma_Run2018A_UL,
    EGamma_Run2018B_UL,
    EGamma_Run2018C_UL,
    EGamma_Run2018D_UL,
]

DoubleMuon_Run2018A_UL  =   FWLiteSample.fromDAS("DoubleMuon_Run2018A_UL",  "/DoubleMuon/Run2018A-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018B_UL  =   FWLiteSample.fromDAS("DoubleMuon_Run2018B_UL",  "/DoubleMuon/Run2018B-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018C_UL  =   FWLiteSample.fromDAS("DoubleMuon_Run2018C_UL",  "/DoubleMuon/Run2018C-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2018D_UL  =   FWLiteSample.fromDAS("DoubleMuon_Run2018D_UL",  "/DoubleMuon/Run2018D-UL2018_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleMuon = [\
    DoubleMuon_Run2018A_UL,
    DoubleMuon_Run2018B_UL,
    DoubleMuon_Run2018C_UL,
    DoubleMuon_Run2018D_UL,
]

SingleMuon_Run2018A_UL  =   FWLiteSample.fromDAS("SingleMuon_Run2018A_UL",  "/SingleMuon/Run2018A-UL2018_MiniAODv2-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018B_UL  =   FWLiteSample.fromDAS("SingleMuon_Run2018B_UL",  "/SingleMuon/Run2018B-UL2018_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018C_UL  =   FWLiteSample.fromDAS("SingleMuon_Run2018C_UL",  "/SingleMuon/Run2018C-UL2018_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2018D_UL  =   FWLiteSample.fromDAS("SingleMuon_Run2018D_UL",  "/SingleMuon/Run2018D-UL2018_MiniAODv2-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SingleMuon = [\
    SingleMuon_Run2018A_UL,
    SingleMuon_Run2018B_UL,
    SingleMuon_Run2018C_UL,
    SingleMuon_Run2018D_UL,
]
## add up all samples
allSamples = MET + JetHT + EGamma + DoubleMuon + SingleMuon

for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
