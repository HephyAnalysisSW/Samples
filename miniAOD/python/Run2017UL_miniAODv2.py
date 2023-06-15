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
dbFile = dbDir+"DB_Run2017UL_miniAODv2.sql"

logger.info("Using db file: %s", dbFile)

# MET
MET_Run2017B_UL  =   FWLiteSample.fromDAS("MET_Run2017B_UL",  "/MET/Run2017B-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017C_UL  =   FWLiteSample.fromDAS("MET_Run2017C_UL",  "/MET/Run2017C-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017D_UL  =   FWLiteSample.fromDAS("MET_Run2017D_UL",  "/MET/Run2017D-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017E_UL  =   FWLiteSample.fromDAS("MET_Run2017E_UL",  "/MET/Run2017E-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017F_UL  =   FWLiteSample.fromDAS("MET_Run2017F_UL",  "/MET/Run2017F-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [\
    MET_Run2017B_UL,
    MET_Run2017C_UL,
    MET_Run2017D_UL,
    MET_Run2017E_UL,
    MET_Run2017F_UL,
]

JetHT_Run2017B_UL	= FWLiteSample.fromDAS("JetHT_Run2017B_UL",  "/JetHT/Run2017B-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2017C_UL	= FWLiteSample.fromDAS("JetHT_Run2017C_UL",  "/JetHT/Run2017C-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2017D_UL	= FWLiteSample.fromDAS("JetHT_Run2017D_UL",  "/JetHT/Run2017D-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2017E_UL	= FWLiteSample.fromDAS("JetHT_Run2017E_UL",  "/JetHT/Run2017E-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
JetHT_Run2017F_UL	= FWLiteSample.fromDAS("JetHT_Run2017F_UL",  "/JetHT/Run2017F-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

JetHT = [\
        JetHT_Run2017B_UL,
        JetHT_Run2017C_UL,
        JetHT_Run2017D_UL,
        JetHT_Run2017E_UL,
        JetHT_Run2017F_UL,
        ]


DoubleEG_Run2017B_UL	= FWLiteSample.fromDAS("DoubleEG_Run2017B_UL",  "/DoubleEG/Run2017B-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2017C_UL	= FWLiteSample.fromDAS("DoubleEG_Run2017C_UL",  "/DoubleEG/Run2017C-UL2017_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2017D_UL	= FWLiteSample.fromDAS("DoubleEG_Run2017D_UL",  "/DoubleEG/Run2017D-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2017E_UL	= FWLiteSample.fromDAS("DoubleEG_Run2017E_UL",  "/DoubleEG/Run2017E-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleEG_Run2017F_UL	= FWLiteSample.fromDAS("DoubleEG_Run2017F_UL",  "/DoubleEG/Run2017F-UL2017_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleEG = [\
        DoubleEG_Run2017B_UL,
        DoubleEG_Run2017C_UL,
        DoubleEG_Run2017D_UL,
        DoubleEG_Run2017E_UL,
        DoubleEG_Run2017F_UL,
        ]

DoubleMuon_Run2017B_UL	= FWLiteSample.fromDAS("DoubleMuon_Run2017B_UL",  "/DoubleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2017C_UL	= FWLiteSample.fromDAS("DoubleMuon_Run2017C_UL",  "/DoubleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2017D_UL	= FWLiteSample.fromDAS("DoubleMuon_Run2017D_UL",  "/DoubleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2017E_UL	= FWLiteSample.fromDAS("DoubleMuon_Run2017E_UL",  "/DoubleMuon/Run2017E-UL2017_MiniAODv2-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DoubleMuon_Run2017F_UL	= FWLiteSample.fromDAS("DoubleMuon_Run2017F_UL",  "/DoubleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DoubleMuon = [\
        DoubleMuon_Run2017B_UL,
        DoubleMuon_Run2017C_UL,
        DoubleMuon_Run2017D_UL,
        DoubleMuon_Run2017E_UL,
        DoubleMuon_Run2017F_UL,
        ]

SingleMuon_Run2017B_UL	= FWLiteSample.fromDAS("SingleMuon_Run2017B_UL",  "/SingleMuon/Run2017B-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2017C_UL	= FWLiteSample.fromDAS("SingleMuon_Run2017C_UL",  "/SingleMuon/Run2017C-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2017D_UL	= FWLiteSample.fromDAS("SingleMuon_Run2017D_UL",  "/SingleMuon/Run2017D-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2017E_UL	= FWLiteSample.fromDAS("SingleMuon_Run2017E_UL",  "/SingleMuon/Run2017E-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
SingleMuon_Run2017F_UL	= FWLiteSample.fromDAS("SingleMuon_Run2017F_UL",  "/SingleMuon/Run2017F-UL2017_MiniAODv2-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

SingleMuon = [\
        SingleMuon_Run2017B_UL,
        SingleMuon_Run2017C_UL,
        SingleMuon_Run2017D_UL,
        SingleMuon_Run2017E_UL,
        SingleMuon_Run2017F_UL,
        ]
## add up all samples
allSamples = MET + JetHT + DoubleEG + DoubleMuon + SingleMuon

for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
