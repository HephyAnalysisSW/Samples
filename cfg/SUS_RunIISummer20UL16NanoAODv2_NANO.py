# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: SUS_RunIISummer20UL16NanoAODv2 -s NANO --eventcontent NANOAODSIM --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False))) --datatier NANOAODSIM --fileout file:SUS-RunIISummer20UL16NanoAODv2-00003.root --conditions 106X_mcRun2_asymptotic_v15 --filein dbs:/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM --era Run2_2016,run2_nanoAOD_106Xv1 --no_exec --mc -n 100
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv1_cff import run2_nanoAOD_106Xv1
from PhysicsTools.NanoAOD.common_cff import *
process = cms.Process('NANO',Run2_2016,run2_nanoAOD_106Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( (
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/014FC9E7-39F9-5249-B237-B98E5CF5A1F9.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/0680D282-F456-D343-B0BA-608F47ACB073.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/08DA25AB-E733-0D4E-B837-47DB430E5C15.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/11C44EBF-9AE6-DC44-A744-6634EF717DD3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/1B87FD5B-F19C-FA4D-90E8-6A7D46B11411.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/292B4D69-7F74-8F48-9B7D-DF313F4DED24.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/344AD73E-9AF3-6045-97EE-2010D5792D28.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/54766934-0B28-BB4A-8220-14E62DAAB8D2.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/554F7739-865D-6643-A914-8AFCC925B27B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/5BC95BF8-D5A3-F941-AC33-A2E7A0A81B3B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/5C351FF3-337C-F344-9E1D-65005950A712.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/632402FC-39B5-934C-9654-5021655990B8.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/73646070-E387-E54A-9891-C13D3D6BCC9F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/74762F49-B2C3-2E47-9AF4-C870A34EF139.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/7967FD9C-303C-484C-98F6-095A8BE76E8B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/79A491F0-80A2-4744-95F3-A4C9150D112D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/811AEBC7-1D8C-5042-B291-7394E0C7305E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/87CC1091-5339-2C4A-BE04-982253B3F283.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/8E8C7164-9CB2-FB44-9909-46D018CBD591.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/A7987E7A-FA11-984D-92D1-A8ABBA37834B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/A82E0804-5835-C54C-8220-1A1295B3F84B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/AC121996-946E-224F-9D0B-D57E96474C72.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/B5C99C50-A91D-BA42-BFC5-CD7F1978B992.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/BDF48D80-A117-8541-B629-450CF6298497.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/BFB47BD4-2834-5D4C-BE7D-90A7D2CA5CD1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/C8AACC75-1B07-AF42-8017-ED2455A79F90.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/D6A036CD-F2C2-DE4C-82E6-BD5810729F6A.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/DB4077C1-A2F8-CC4C-B608-020E52632A21.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/DE2157C1-6806-3C40-98C2-DC48D1BA87C3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/DEA9CFF4-02D2-CF48-A948-5792DD4E108D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/E83D8654-CBFA-4749-AC4C-119B6D388895.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/EE171C63-3AAB-7742-80B1-6F2F7A2A8D0B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/230000/FEF2D759-A64F-054D-B52D-6231C86F0CC7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/00ED4D5A-B425-5945-AD5B-60C6F7D08316.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/043D8F40-9D3A-D84D-9FE6-0442DC4D495F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/072A0524-BBF0-2C45-997D-8AC6238475E3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0A7A12B6-48EA-664A-B151-F7B918E0AC20.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0AEC8929-5C6E-5C40-BAF1-10EA97973269.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0B37FA59-A825-C446-9ABA-B5E8346533D7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0D07C0BA-92BF-6E4E-9C78-605EB66A58A5.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0D519E43-B120-3244-A30F-D2F0C1D8D5B1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/0FD1D517-F1C8-7F47-9B54-9F0C3134E712.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/113025E2-98E9-0E44-9A51-969C0073FF4D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1189869C-842B-DE4C-8138-6DC7E3526436.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/11B826EF-3935-2246-B28D-33D5017A7585.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1246F3F9-1FAA-144F-A0C6-28780440FBCA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1440EE25-C75D-5F49-B45D-6807974AC5E1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/149ED675-6ACB-194C-933B-20F2EB6F7472.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1561A8FA-BEA1-C540-B3F4-B3EE34055B3B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/16D70D0F-E3FB-3F43-AC38-FC677CB46537.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1876301C-EBF8-7644-AF7A-E82BFBA48395.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/18AD9CBA-935D-254E-ADA1-9430932757AB.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/19326F56-6C9C-6947-829B-55C53D9252EF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/197C9566-6C8C-6640-B428-9BE587E0DCFB.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/19C3DDDD-59B6-5446-A806-073148ED9CE3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1B128E7C-F023-9B48-9818-B17D19B67451.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1B29F810-8867-5D46-9DAD-89FC82DCA142.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1BBFB86B-7E7C-AC47-A391-84FFA0942D22.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/1C59FF75-79C6-A94A-90C8-53E92137A3DE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/21011BE1-5B1A-6B44-A58C-2D7F0E69CDBB.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/271887A6-32D2-524D-A54F-735E1AC7CD59.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/27C2F126-BB4A-7240-80F5-FC0CAB5D9854.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/283C47B9-58A1-174D-BEBD-7BEE39A8B8B2.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/29761C2B-CD77-4D47-91AF-227DC6DEF3B1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/29CEDC54-E969-7A43-B29B-8E089034F074.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2C55BA15-71AA-8147-92F6-1BE620F6F55B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2CB37AF4-269E-1C4F-824A-9B67F6D2A24B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2CEB9F0D-9DFF-3C4B-AE6F-75AA0F79C6AA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/2E94D5B5-D863-F14E-ADED-4E4C5C8BBB87.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/313E03BD-77EF-4A42-A1CF-33A1E563C81A.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/31D591F4-2C73-E54D-9B8F-B978C5CBF52B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/34E7AF79-CC9F-604E-8D0C-07F76AEFCBEA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/34F832A6-A9C6-384C-A8AC-8797A07C55AD.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3555E5B2-E383-D040-B949-F9EF088F78F9.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/35ABC495-841F-0841-B68C-3278BE1EEC2C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/366F9B55-8F0F-A246-9F20-9BFF5FFA52EE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/373B29A4-756A-8A47-9B5C-1ECD30F0B446.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3981A32B-3E1D-7D44-8C75-F3FD9C44274D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/39A32E51-53AD-0F4B-8DD8-C95811C47A51.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3A60FA53-46D7-CD4B-BF43-D210E761B06E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3B039D30-5B55-C743-AD91-955AE20A872D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3B71FC32-A719-B649-BB7C-0CA084333874.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3C279A8D-A899-EE49-A0AA-6EA2450DD0D7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3C2BC47B-C76D-894B-AE3B-557E625FA7B5.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3D6C2D54-DC99-EC45-8B7A-451A14261AE7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3F2EB1C2-37E0-B54C-9186-2FEF57181509.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/3F3AD43A-C254-B043-8699-F8B6E798B49C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/401628FD-14AF-E04F-8820-64C54DAB4EF6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/40938982-42F9-204D-B8F7-F6DE75FB761D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4104FD03-C3E2-9B42-922C-C45FDF01EA93.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/429DAB20-1195-FA4C-8175-86FF72146AD6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/452CD368-AB18-4D4C-937A-B7F9950B4384.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/453CB399-6059-A548-BAB6-FEF26E326660.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4690CE8A-5A4D-3546-B793-2434EE711181.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/475FFCD2-A6AE-BA4C-8B27-6357A83DF82F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/47D3A8C3-DAE6-234F-BE9E-A1AB8527920B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/49356CBC-991A-3D48-9FD4-EFD45B9D6DD6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/49CCC8DF-2A28-9F45-87EF-99481F702CD9.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4AFCAEAC-B216-184F-8C7C-8E75F91890A6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4BD1E370-FE7B-FF44-8EB0-EC1F8047FBDF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4BE2F191-06A7-4540-A4E3-E0438642826D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4C0E64A9-D9D1-FE4A-9776-EEC52B1018BF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/4DD9D5D6-344E-B942-8786-3A1D2782CAC6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/524F9D66-D90E-4A44-A9CA-FDBB819BDBDF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5322698A-0838-3A4A-905E-406FD74BE6F7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/53FFF8B7-B897-2E4A-94DD-E4207C605FD3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5548B004-D7B8-104B-9548-F10F838D5B26.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/55AF787D-F2DF-A44A-9ED5-A939EF08F427.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/567115AB-627C-E244-ADF7-89E13B66681E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/569A1B11-571C-EF4B-B44D-2ADD5025A801.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/59681183-4B7E-2F4D-B5D2-C0EE88E790CE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5A4A982A-4467-8F42-9F87-09C855E91D9E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5ABF7539-82A4-9F46-8777-9FC7D74BBD09.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5AC309A5-99C0-844E-8FF0-EF21C7999579.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5B72DC5B-A438-744E-B1C9-50B55D86E204.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5CA7D676-83A2-9245-BCCE-3E813C51DF66.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5DDA9293-2339-9A4B-B8DF-410F17B9B124.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5E2A592B-CF41-CE47-9812-84C6282EB738.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/5F857B08-2FEE-7E4F-A58D-0B539F069A64.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/60DFF317-9871-3A4E-8034-22952E3F87D7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/64E4A76C-9EC9-F845-A573-A29B6037FC68.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/65FB1A5D-28BE-B644-BDCC-570ACC810031.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/6739E0E7-3588-3646-B738-163464068BF4.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/67D2A438-0D0F-E04C-903D-752C86D0458B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/69C37E6F-4877-F84E-B86A-4791B202A4F2.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/69ECD2D1-C88C-F44B-9D09-5615C327D606.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/6A1B5F95-A1D5-FB46-BC0F-4C2F708D1363.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/6A90E273-2305-204F-A3C5-86A92864A046.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/6F9F4F17-3790-974B-87D1-A60EA042CCE4.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/6FB9F76E-C93F-FD47-9CDE-9585E58867D7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/72EB4C86-469A-EE40-88CC-4DC3F6A898D1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/73533F72-FFCC-2D45-8E38-8B77BF543523.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/73D418B0-1C0B-0840-B415-8F1983B54860.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/746B5C9A-9337-BA47-A805-357A8547DF7A.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/74C172C2-9BBF-8B4B-B0CA-A3C98972966B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7515DF28-C301-F84B-B1F0-E9671387975D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/76D3446A-2AA5-0C44-90B9-6DF6CF3B6214.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/77AB7685-5109-3149-99C7-DFD1286C9DAA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/77ADC87F-0837-0A4F-A7B6-ABB092FEB762.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/77B53B91-2841-4348-AD07-2CDC9674CC28.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7C295E7D-CD16-4841-A6A1-F77F18C57547.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7EAC3041-E0C4-0E47-BDF9-56646457471D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7EB5ADD0-9B2E-9C45-BC54-EE7FA2173692.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7F20A6F6-DFF7-6947-AB6F-8296647C21F7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/7F8D0584-0D1B-7744-8468-14CE9CD01A14.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/820B5F97-1173-EE44-A3A2-83458084A218.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/826EB7FD-0A07-0240-9865-F55B5D0B6F1E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/82DC8802-2FEA-9C42-A5A8-2BE3430B2EAA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/837E699B-1761-214B-84F6-A7C09E5FC21C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/86F35CBA-23CA-A348-A318-A3FCCAE49AF1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/89373CBE-49BF-6E4C-801D-0DBEDF1DC9D5.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8A5D321D-02FE-0449-B546-A744BA15EBCC.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8AF808D8-0E47-7B4F-969D-4E0CA10873F0.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8C76FE68-E824-D14B-AEAE-A75127CB7ADF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8D066B3C-8252-A744-AF8E-CDFEC93487E0.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8DF5204A-04F1-A140-BFCE-58FC4516D28B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8E1DE1F3-D9CF-3A4B-AFB8-AF17CFB0EEB6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8E51F66A-3264-EF44-87BC-2D659C4E3092.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8E976619-FA8A-2A4F-A841-F7F4985654BE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8EAB592F-52A2-2B41-810F-88CE10BADF11.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8F859020-962B-E647-AA57-EADD4EF58EF7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/8FEB9B1F-EB3B-8C4A-883C-391EB68AEB3A.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/900CC4DE-EA76-B649-9CB3-6BB9EFB8CDC3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/90BCFD6B-6F04-C644-8EB7-C8FE97F0393E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/915B01EF-F454-B54E-A635-F461CDB992A5.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/93FFFC33-BC39-0944-A4E1-CABB8FB462EA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/944866AF-168A-FC47-9F6C-E71172303F52.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/956C95D5-5C7E-D548-ABEA-8866FB57533F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9634D081-C4F8-F645-8048-19297EF72E25.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/975484A4-DF04-EB41-BDEF-3E90CBBFE649.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/98284658-B4E3-1545-8F21-08E06C745A9E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/98C95D2B-46D8-8248-8887-6DA812F52E08.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/99C1FF88-E0A5-9843-8BFF-3399BCF8A8FB.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9ADD0944-671E-1E48-B6FF-0F0A2FAA1C9E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9C91DDCB-66DE-044F-9B8B-529AC8915416.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9CBEF7FC-53B4-4B4F-9E76-041D37829822.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9D670D7D-69AA-5643-A5BD-AFE90A4EEB92.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9DA681A4-47C1-754C-A07A-6A48C5B26A57.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9E272E34-CCA0-2841-A073-B521504A7A73.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/9E2B69C9-6494-604B-B928-35707167B3FC.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A15D0357-09CC-9B41-A7B9-022491BD41B0.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A1849D21-D928-ED4C-82B3-A47BD719F7CC.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A226F92E-EC9B-834C-93D9-7C9EF3A99243.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A23F6FF9-73C4-BA40-B59D-4E0E1A9C15D3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A2A456D5-9B8F-6D41-976B-862F754F0A5A.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A6C30E68-B455-E04F-8F0F-E05E73E33B58.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A6FC75CF-BE5C-904A-96FC-BC1610CDB4A3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A76BE9BD-FFC8-D94A-ACD4-FB48DD6BEC15.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A7F1EAD0-E818-E441-9E33-9E0C86A56B8D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A8114B1C-C9A1-4844-9257-7A19BD0A07DA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/A8485452-2BD7-AE46-BB5D-06609AECC691.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AA556779-D629-E843-985F-6A1DA08E8BD0.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/ABF6B60C-48D1-2B4B-B6BF-C30DD204DD61.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AC262EB4-BD06-4E4C-8C7F-F54115C38BCF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AE02D4E7-ACC2-0243-9AD1-935E67D77F22.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AE86B621-BF23-9D4B-A349-5D492CBC68BA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AE892EB7-A846-CF44-B139-F847417E9FCE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AF4C1CAC-672B-7842-8C11-71F23AFAFB84.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/AF997B0F-5EC6-A44F-84E8-1C0727133111.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B14FFB0E-B13D-ED4D-96E7-AF531FCEF487.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B2A96337-A65B-6343-B537-9737349AF6A1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B2DACE6E-EC16-B745-8CC5-021EEFD659FA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B2FC1A38-B4D9-354F-98FC-D1D677BD5B51.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B4E6883B-67FA-1942-AE70-808D628080C4.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B52232B8-CFB9-5E4B-9ED2-74D6545BF1DE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B6629F01-8AC1-9E4E-998B-FB085096C7B2.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B768817C-AF5C-054A-9F7A-31DD8B874EAE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/B95669E2-D978-BB43-8C04-CA9570C202F6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BA7809EC-5CBB-7F43-BB8C-DB5CF71D6830.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BA8C2947-409C-134A-A61F-8DC0D3479577.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BC83535D-58AE-814B-8388-E78A0B473B85.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BCFAE5D9-4AFF-F547-BD5F-95DA87D4B268.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BED827B3-6376-6344-82B9-DA2CCF0EF6E4.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BF324989-4B59-3E44-B00F-9EC68FD4542C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/BF5093C2-C162-8C43-979B-6756A8C7045E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C12665AE-286C-2C42-A74D-886CEC5E799C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C34BE858-74B4-AA4F-946A-752F92BB92B1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C3CE5476-8366-6642-8424-5F4854067CF3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C631C601-C178-7E48-96BD-E8D755380A15.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C6DE0619-BC4D-F94F-B365-0F7ADCD037B9.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C86E290A-2B08-8E40-9418-9B2172F2C192.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C9B15CAA-22F5-3F49-8281-CA32B0A4B49B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/C9E4386A-E832-BE4D-9667-48E7D1A0CAAD.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/CAF1CF83-99C5-F249-92CE-C577BACDCAB1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/CB8092D6-9508-7F48-B65D-C143975477DB.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/CC5DCA98-1C88-AF43-86C7-7CEDDEB5E3E0.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/CC859A39-370A-C646-B18A-65D4C85C9744.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D01C1D9D-1BC2-894F-9F8B-8317D1CBC930.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D1954B22-1133-FF4F-B8A1-99A72E2EED2B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D34101CD-DE8C-884B-A298-73309BF01235.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D3C5833F-6D6A-F743-9E42-3C698BBB38EF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D459E81D-89AD-E349-8284-5A633B36F4D7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D5133091-AC71-FB41-935D-96163CEDA909.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D7384A65-36B8-FF43-9F19-56F2E7B0A3EA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/D7E8927C-8256-B34E-8B91-BE6EF6B3612C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DA41BDFD-9D4E-3141-92DA-8BA851B097B1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DA6D3F82-F2B0-9747-AF6E-40B9DD9E0A2C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DA7CDB32-8CEE-6B45-B929-AE29A6F33CCB.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DAA15A54-CA74-3440-AEB4-702CA7BB23F4.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DB371DE8-8002-0B4C-900A-5D941237CE7F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DD98B8EB-CB0F-C242-887E-7B04D52981DC.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DDF5ED7F-D6FB-5F4D-95A5-9FB9E7E6B846.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DE085982-4458-A94D-96EB-F35F7CDE5DEA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DE9F5AEB-F669-C140-9840-9443E92EB6EA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/DEA5C113-9478-AB43-8A3C-35305CA9F941.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E167DB01-9375-414F-8BCE-902D59912774.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E20E6375-48F4-654F-B4FF-0E9A5ABBAB0F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E3E94A88-28D8-0A41-B4FE-CB72A48EC040.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E5280063-E570-0F4C-BAA3-85332426E61D.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E5FA65A9-FB1A-F241-BD0D-C349BEA08C48.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E73E01C0-575F-554B-B784-7A66ADBF26CF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E7B887BD-3E22-174B-994D-563219968AA0.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E7E6EBFC-58BC-604F-8C5B-08DF6662440F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E83F2B93-032E-BA44-B6A5-E482D863E4D4.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E87C35B5-5A12-FB4B-BFAF-3BA6B280BBAB.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/E905EF14-D349-3F43-97C0-BF634E25A2B2.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/EABDA508-1B6B-1447-B3C5-AF308DD80CD9.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/EAE304FC-3E4C-754E-8A91-3D6205E025AE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/EC7BFD66-CC67-5449-AA0E-15538E611C28.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F00D62A6-1206-D140-89F3-E940F1EF2EF9.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F2430AD8-E06B-6347-9336-962FD480E239.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F27A6E6A-9F78-E24D-8E1E-785111CFEB14.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F3BEA230-443D-1144-9957-29E56607028B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F63425CA-F9BF-794F-8C88-FB8E93E589BA.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F68520A1-E84F-DF45-8F39-0500A08F48D1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F6CDDE21-EFD2-4C44-8AA2-8B8CACC32E70.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F7AF89AC-AC1A-344E-B629-798CDB39378C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F8382460-A6DE-5747-9041-684E5490B0BF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/F902D374-6664-F043-9609-5F1EEDE528C5.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FA1386EB-3AB1-B94A-99BA-AD07BECE5737.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FAF2D27D-83FE-CB49-B6FC-709922CA0959.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FB2456DD-7E3F-1A4F-9C0F-B9CE26FEACD6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FB2DB548-585B-164B-B52D-139440E7FF97.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FB3C38EF-8EB4-D44D-9417-25C9554A3320.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FB9E9F46-CF4B-C541-B624-4607CA4C473E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FC76D0FA-2A71-FA4C-A73D-1CFD23F34EAE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FD9FB10D-322C-E04F-B346-8DBC60CCACA3.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/260000/FE82661B-004A-A64D-B757-F3DCF5B9F2F8.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/071F4DC4-7D97-3748-B5A7-21F3ACC58518.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/1E6F150A-75B4-A746-8895-963483E41C39.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/291008C9-53B8-0E47-BF73-B5F80049CACC.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2A76F22F-03A3-F74A-B288-36B0AE289713.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/2B3BBF2C-E9ED-1749-B778-94D960A76BF1.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/344CCE6A-C87F-7443-BCF8-E4407E5579C4.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/38A100A1-6ADA-EE49-B592-2BDE610B9745.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/3C107B63-7CF3-D849-B82A-22D5F59DCEF2.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/52E62FAF-C447-DA46-990B-FE73A7FE364E.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/60A863BC-6756-B84A-92C8-2C0819E9D000.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/65E6921E-E544-934B-A458-7C2CBF6C95F6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/6672EEE5-D3B7-544D-9C55-1FBD02E08098.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/68DE63A8-8C50-D444-AA52-DD1A61429ACF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/6E740167-AC1D-D344-B23A-732F6CC94115.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/82334823-5CFF-7A47-B337-B9108560A3F6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/992C2CBC-14F0-544C-8AEC-535856A0AA48.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/9F788ACC-7DD8-7F42-909D-F0F497C4D5D6.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/A248AA2F-132E-FB49-ABC1-062BC7792DE0.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/A739617B-00AF-2E4B-A35A-D39ECA4CCD1C.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/A8065E51-7479-724F-8B7C-DE17B4184EF5.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/AA16763B-6E4C-964B-8D80-C08D92E6203F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/B74E1C69-E8C5-9B45-870A-33F2366D1A50.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C2A677E0-89F8-4849-BD44-48B99A9597A7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C638242B-2E46-734C-BE54-6D30E7123BF4.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C8174DB0-5780-AD40-A23D-E6CE881F22FE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/C9F079B6-BA10-9746-AFDE-8F2CDF7285B7.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/CADAAD3E-1E87-4C46-B4EC-00315730D041.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/DF44C61B-9C98-5145-B93B-F8C7B7FC730B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E1D9644D-33AB-ED4F-8F8C-434996736184.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E25759DD-7626-F14D-8D8B-4CD024FE5874.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/E2C5522B-E85C-674B-A088-4D7A8C3F12BE.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F15FDD2F-426E-8443-A20C-F348DB8A978F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F2784482-5392-6040-A951-A50E420F957B.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F60DB47E-5E47-4F4E-BAE1-AAEFBDE0DC5F.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/F78FC76D-9D8E-484B-BA80-685A37C22074.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/270000/FEA7B337-ED3B-D94E-BA39-1E1DF22131EF.root', 
        '/store/mc/RunIISummer20UL16MiniAOD/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_v13-v1/280000/0CB90113-BC83-BC4F-9A83-82FCE6AB58DB.root'
     ) ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('SUS_RunIISummer20UL16NanoAODv2 nevts:100'),
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
    #fileName = cms.untracked.string('file:SUS-RunIISummer20UL16NanoAODv2-00003.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_v15', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
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
