# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SUS-RunIISummer20UL16NanoAODv9-FS_cfg.py --eventcontent NANOAODSIM --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False))) --datatier NANOAODSIM --fileout file:SUS-RunIISummer20UL16NanoAODv9-00176.root --conditions 106X_mcRun2_asymptotic_v17 --step NANO --filein dbs:/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-FSUL16_106X_mcRun2_asymptotic_v17-v2/MINIAODSIM --era Run2_2016,run2_nanoAOD_106Xv2 --fast --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2
from Configuration.Eras.Modifier_fastSim_cff import fastSim
from PhysicsTools.NanoAOD.common_cff import *

process = cms.Process('NANO',Run2_2016,run2_nanoAOD_106Xv2,fastSim)

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
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/0CC729ED-69FE-3541-978F-DFA91CCEFCA9.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/145EBB15-50F9-5540-86CE-588F316565FD.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/3179D0A5-7BB5-044F-9958-29A924460733.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/358D93D1-80A1-B741-BF51-65E7CF619CBC.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/3627095C-92E0-1141-AB76-3B03B2370CF0.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/43D02706-C7B7-1441-9BCC-BD7EACA25998.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/4BF0545D-74C6-8746-8750-49621158E50A.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/574F28C9-D7AF-7B44-864C-A1EFB9EB7FE4.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/5B83D1DF-8C3C-F145-BDA1-A20378D0D687.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/66CCDCE2-BA09-C245-9581-6DA454ABA7D1.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/6F9293E0-6666-5A42-9793-D07BEFA9671F.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/717067D7-05F5-9646-A75B-9C9EBBBFB993.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/79AB8054-24AF-D947-9CEC-9536EFF0E4E6.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/7E1DD2CF-D2AC-F941-AA57-4A8AAB46A95C.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/817B5778-F9EA-DB40-A7ED-028FD81B4F3B.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/81E389E9-67DA-8049-88F6-1A9C9BF38446.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/978EB294-D8D6-8945-91B7-08F35EE49E80.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/9A5BF19F-EBB1-F441-80F6-7C9CDABD3A22.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/A17B8512-A396-8B40-93AE-FB355F84669B.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/CF1C262C-1CAD-4B47-8ABE-404B0A23B98E.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/DDADAF69-B228-CD49-9F00-D2BD88007055.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/F393A33E-F453-124F-9A15-A335ECC4A3E6.root', 
        '/store/mc/RunIISummer20UL16MiniAODv2/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL16_106X_mcRun2_asymptotic_v17-v2/40000/FDE849B8-9741-744D-B98E-536B2BB22366.root'
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
    #fileName = cms.untracked.string('file:SUS-RunIISummer20UL16NanoAODv9-00176.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_v17', '')

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
