# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SUS-RunIISummer20UL17NanoAODv9-FS_cfg.py -s NANO --eventcontent NANOAODSIM --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False))) --datatier NANOAODSIM --fileout file:SUS-RunIISummer20UL17NanoAODv9-00164.root --conditions 106X_mc2017_realistic_v9 --filein dbs:/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-FSUL17_106X_mc2017_realistic_v9-v2/MINIAODSIM --era Run2_2017,run2_nanoAOD_106Xv2 --fast --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2017_cff import Run2_2017
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2
from Configuration.Eras.Modifier_fastSim_cff import fastSim
from PhysicsTools.NanoAOD.common_cff import *
process = cms.Process('NANO',Run2_2017,run2_nanoAOD_106Xv2,fastSim)

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
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/30000/315D4899-7660-D340-ABBC-8A1870F5519F.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/30000/84E72632-D7FF-824B-B053-DD7F28AC72E3.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/30000/C3737D81-4768-004C-93D7-BC0A7A014905.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/0C884AB2-5E86-E849-B39B-06ABF110E1F5.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/379EECA4-824D-4240-B8DF-F9F7B186566C.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/41643684-6B98-C046-8E45-452113EC6FB6.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/541F8727-75B1-A94A-9730-2263884452A0.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/54A860CB-7490-7C4A-9A84-5742CA080771.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/55DD040D-3AFE-4F41-80B8-18A5C363D4D0.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/63D44634-8DAD-CA40-A075-85030FFDB9E3.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/74202A63-90F7-A54D-A0A1-F12306DED889.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/7F55AE2E-7056-1C4E-8E2D-EF81733CCEE2.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/7FCB236B-F9AC-A045-8E22-2F1AA98263EE.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/84970807-BC8C-E240-91D3-27EA2A3712A0.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/9BA4FAF8-BDC7-324B-974C-C4861D7D963B.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/A162FE66-EC61-7D4F-82A9-B8EA33C5E93E.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/B233BCF3-7137-FB47-97ED-16D509E52287.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/B76BC2C0-B8DC-3341-B282-25F621AE99B8.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/C524D563-6658-FF4D-82DA-5C6DAB6D5874.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/D2C66E4F-6662-2348-BE59-894CA8A4E900.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/EC48ACBF-7DC8-CC41-BF56-962CD1EEFF6C.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/F8132E37-B5EB-8B4A-9D87-9EF7ABBE3C63.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/FE65207E-C948-B541-A2EF-670CB44DD298.root', 
        '/store/mc/RunIISummer20UL17MiniAODv2/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL17_106X_mc2017_realistic_v9-v2/40000/FFD060FA-690E-1044-90E7-7F8A79D33DB0.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SUS-RunIISummer20UL17NanoAODv9-FS_cfg.py nevts:100'),
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
    #fileName = cms.untracked.string('file:SUS-RunIISummer20UL17NanoAODv9-00164.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mc2017_realistic_v9', '')

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
