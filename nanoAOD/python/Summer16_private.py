import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
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

# Redirector
try:
    redirector = sys.modules['__main__'].redirector
except:
    if "clip" in os.getenv("HOSTNAME").lower():
        from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+"/DB_Summer16_private.sql"

logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_MLM_FS_S16_80X_priv  = Sample.nanoAODfromDAS("DYJetsToLL_M50_MLM_FS_S16_80X_priv", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1_METSig_v1-874c0b83f53e95cd92fa366b95b462ff/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03", xSection=2075.14*3)
DYJetsToLL_M50_MLM_S16_80X_priv     = Sample.nanoAODfromDAS("DYJetsToLL_M50_MLM_S16_80X_priv", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2_METSig_v1-95163dc1655e9579f2e671fa6cceb399/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03", xSection=2075.14*3)

DY = [
    DYJetsToLL_M50_MLM_FS_S16_80X_priv,
    DYJetsToLL_M50_MLM_S16_80X_priv,
    ]

TTJets_MLM_FS_S16_80X_priv  = Sample.nanoAODfromDAS("TTJets_MLM_FS_S16_80X_priv", "/TTJets_13TeV-madgraphMLM/dspitzba-crab_RunIISummer16MiniAODv2-LHE_PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_METSig_v1-874c0b83f53e95cd92fa366b95b462ff/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03", xSection=831.76)
TTJets_MLM_S16_80X_priv     = Sample.nanoAODfromDAS("TTJets_MLM_S16_80X_priv", "/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/dspitzba-crab_RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_METSig_v1-874c0b83f53e95cd92fa366b95b462ff/USER", dbFile=dbFile, overwrite=ov, redirector=redirector, instance="phys03", xSection=831.76)

top = [
    TTJets_MLM_FS_S16_80X_priv,
    TTJets_MLM_S16_80X_priv,
    ]


#TTGNoFullyHad_priv  = Sample.nanoAODfromDAS("TTGNoFullyHad_priv",  "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v4/Summer16_private_TTGamma_nofullyhad_LO_S16_private/", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.056*1.994+1.495*1.616, maxN=1)
TTGHad_priv         = Sample.nanoAODfromDAS("TTGHad_priv",         "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v4/Summer16_private_TTGamma_had_LO_S16_private/",        dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=4.149*2.565)
TTGSemi_priv        = Sample.nanoAODfromDAS("TTGSemi_priv",        "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v4/Summer16_private_TTGamma_semilep_LO_S16_private/",    dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.056*1.994)
TTGLep_priv         = Sample.nanoAODfromDAS("TTGLep_priv",         "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v4/Summer16_private_TTGamma_dilep_LO_S16_private/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=1.495*1.616)

TTGNoFullyHad_fnal  = Sample.nanoAODfromDAS("TTGNoFullyHad_fnal",  "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v6/ttgamma_noFullyHad_fnal_2016/", dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=5.056*1.994+1.495*1.616)

TTX = [
#    TTGNoFullyHad_priv,
    TTGHad_priv,
    TTGSemi_priv,
    TTGLep_priv,
    TTGNoFullyHad_fnal,
    ]

# LO xsec
#ZGToLLG_LO_priv = Sample.nanoAODfromDAS("ZGToLLG_LO_priv", "/dpm/oeaw.ac.at/home/cms/store/user/llechner/nanoAOD/legacy_nano_v3/Summer16_private_ZGToLLG_LO_S16_private/",      dbFile=dbFile, redirector=redirector, overwrite=ov, xSection=445.8)


VGamma = [
#    ZGToLLG_LO_priv,
]

## Signals
#T2tt_mStop_850_mLSP_100 = Sample.nanoAODfromDAS("T2tt_mStop_850_mLSP_100", "/SMS-T2tt_mStop-850_mLSP-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)
#T2tt_mStop_650_mLSP_350 = Sample.nanoAODfromDAS("T2tt_mStop_650_mLSP_350", "/SMS-T2tt_mStop-650_mLSP-350_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)
#T2tt_mStop_500_mLSP_325 = Sample.nanoAODfromDAS("T2tt_mStop_500_mLSP_325", "/SMS-T2tt_mStop-500_mLSP-325_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)
#T2tt_mStop_325_mLSP_150 = Sample.nanoAODfromDAS("T2tt_mStop_325_mLSP_150", "/SMS-T2tt_mStop-325_mLSP-150_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=1)

signals = [
#    T2tt_mStop_850_mLSP_100,
#    T2tt_mStop_650_mLSP_350,
#    T2tt_mStop_500_mLSP_325,
#    T2tt_mStop_325_mLSP_150,

    ]


tWZ_LO = Sample.nanoAODfromDAS("tWZ_LO", "/tOrtbar_WZ01j_OLRLL_LO_ext5/schoef-crab_schoef-Summer16-mAOD949-v3-bd3e7bcff6c9bcad356ea4ed7e4f08b4_nano_v6_2-88146d75cb10601530484643de5f7795/USER",  instance="phys03", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.1312)
tWZ_NLO = Sample.nanoAODfromDAS("tWZ_NLO", "/tWZ_NLO_v16_ext3/schoef-crab_schoef-Summer16-mAOD949-v3-bd3e7bcff6c9bcad356ea4ed7e4f08b4_nano_v6_2-88146d75cb10601530484643de5f7795/USER",  instance="phys03", dbFile=dbFile, overwrite=ov, redirector=redirector, xSection=0.1312)

other = [
    tWZ_LO,
    tWZ_NLO,
    ]

allSamples = DY + other + signals + top + TTX + VGamma

for s in allSamples:
    s.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 )

