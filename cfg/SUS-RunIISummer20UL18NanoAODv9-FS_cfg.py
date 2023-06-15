# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SUS-RunIISummer20UL18NanoAODv9-FS_cfg.py --eventcontent NANOAODSIM --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False))) --datatier NANOAODSIM --fileout file:SUS-RunIISummer20UL18NanoAODv9-00170.root --conditions 106X_upgrade2018_realistic_v16_L1v1 --step NANO --filein dbs:/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM --era Run2_2018,run2_nanoAOD_106Xv2 --fast --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2
from Configuration.Eras.Modifier_fastSim_cff import fastSim
from PhysicsTools.NanoAOD.common_cff import *

process = cms.Process('NANO',Run2_2018,run2_nanoAOD_106Xv2,fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/22542A17-840B-E141-8D1D-DEB7F3C54BDC.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/367CFB38-764B-464E-8E81-776BCB005941.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/3989A1FD-CFB3-5B4B-9C64-EF57927FC527.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/60947EAA-5AFC-BA4C-92B0-AB74028587B0.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/61EEA099-FB99-5D4E-A385-C5591BCA4DE7.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/6AE888C0-C847-D644-8694-1C4F5E2E4478.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/6C9229BB-412A-8C4E-91F5-6B62A2A7E6B5.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/6DF6A459-CB5A-7C46-A1FD-42CD616C1747.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/7265CEFA-A4B9-0F46-94A2-90373F0A92BA.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/8B30007C-FB96-3449-A0CA-1F4C5039F6CD.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/9843DB33-3B7E-4342-A350-ED344AFD0FB0.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/BAD93D7F-73D1-EB4E-BFE4-8CA2F634AF31.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/C4F25FD7-67B9-F34C-A53A-C2259AE2DAE8.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/CABF4270-FCCB-D84C-9191-602183652543.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/E0D7548A-5554-5E43-B4DC-FF7432EAA4C6.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/F5E208E6-8D9A-5D47-BBFA-3938B4BD0058.root', 
        '/store/mc/RunIISummer20UL18MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v2/30000/FB2F6134-6FD9-9743-960B-F20A5BCAF7B1.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:nanoAOD.root'),
    #fileName = cms.untracked.string('file:SUS-RunIISummer20UL18NanoAODv9-00170.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v16_L1v1', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceFS)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.
process.finalIsolatedTracks.cut = cms.string("((pt>0 && (abs(pdgId) == 11 || abs(pdgId) == 13)) || pt > 0) && (abs(pdgId) < 15 || abs(eta) < 2.5) && ((pfIsolationDR03().chargedHadronIso < 5 && pt < 25) || pfIsolationDR03().chargedHadronIso/pt < 0.2)")
process.isoTrackTable.doc = cms.string("isolated tracks after basic selection (" + process.finalIsolatedTracks.cut.value() + ") and lepton veto")
process.isoTrackTable.variables = cms.PSet(process.isoTrackTable.variables,deltaEta = Var("deltaEta",float,doc="difference in eta between initial track and intersection w/ ecal",precision=12),deltaPhi = Var("deltaPhi",float,doc="difference in phi between initial track and intersection w/ ecal",precision=12),)
process.genParticleTable.variables = cms.PSet(process.genParticleTable.variables, vx = Var("vx",  float,precision=10), vy = Var("vy",  float,precision=10),vz = Var("vz",  float,precision=10),)


# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# End of customisation functions

# Customisation from command line

process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
