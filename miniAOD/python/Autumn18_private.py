'''
miniAOD samples of TTGamma private production (Tom)
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

from Samples.Tools.config import dbDir, redirector_BE, redirector
dbFile = dbDir+"Autumn18_private.sql"

logger.info("Using db file: %s", dbFile) 

## TTGamma private new samples
TTGamma_dilep_LO_A18_private         = FWLiteSample.fromDPMDirectory("TTGamma_dilep_LO_A18_private",      "/store/user/tomc/heavyNeutrinoMiniAOD/Autumn18/prompt/ttGamma_Dilept_5f_ckm_LO_1line",     dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_semilep_LO_A18_private       = FWLiteSample.fromDPMDirectory("TTGamma_semilep_LO_A18_private",    "/store/user/tomc/heavyNeutrinoMiniAOD/Autumn18/prompt/ttGamma_SemiLept_5f_ckm_LO_1line",   dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_had_LO_A18_private           = FWLiteSample.fromDPMDirectory("TTGamma_had_LO_A18_private",        "/store/user/tomc/heavyNeutrinoMiniAOD/Autumn18/prompt/ttGamma_Had_5f_ckm_LO_1line",        dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)
TTGamma_nofullyhad_LO_A18_private    = FWLiteSample.fromDPMDirectory("TTGamma_nofullyhad_LO_A18_private", "/store/user/tomc/heavyNeutrinoMiniAOD/Autumn18/prompt/ttGamma_NoFullyHad_5f_ckm_LO_1line", dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)

TTX = [
       TTGamma_dilep_LO_A18_private,
       TTGamma_semilep_LO_A18_private,
       TTGamma_had_LO_A18_private,
       TTGamma_nofullyhad_LO_A18_private,
]


ttZ01j_3l_EFT_lepWFilter    = FWLiteSample.fromDAS("ttZ01j_3l_EFT_lepWFilter", "/ttZ01j_lepWFilter/schoef-Autumn18-mAODv1-10222-58e8664f142fdf477807c95cd1ce2e2a/USER", instance="phys03", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
tWZtoLL01j_3l_EFT_lepFilter = FWLiteSample.fromDAS("tWZtoLL01j_3l_EFT_lepFilter", "/tWZtoLL01j_lepWFilter/schoef-Autumn18-mAODv1-10222-58e8664f142fdf477807c95cd1ce2e2a/USER", instance="phys03", dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)
#TTGamma_had_LO_A18_private           = FWLiteSample.fromDPMDirectory("TTGamma_had_LO_A18_private",        "/store/user/tomc/heavyNeutrinoMiniAOD/Autumn18/prompt/ttGamma_Had_5f_ckm_LO_1line",        dbFile=dbFile, overwrite=ov, prefix=redirector_BE, skipCheck=True)

#ZGToLLG_LO_A18_private = FWLiteSample.fromDPMDirectory("ZGToLLG_LO_A18_private",      "/dpm/oeaw.ac.at/home/cms/store/user/llechner/miniAOD/RunIIAutumn18_privProd_miniAODv1/ZAToLLA0123j_5f_LO_MLM/",   dbFile=dbFile, overwrite=ov, prefix=redirector, skipCheck=True)

EFT = [
    ttZ01j_3l_EFT_lepWFilter,
    tWZtoLL01j_3l_EFT_lepFilter,
#    ZGToLLG_LO_A18_private,
]

allSamples = TTX + EFT

for sample in allSamples:
    sample.isData = False
