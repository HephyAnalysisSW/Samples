#run in CMSSW_9_4_7
tag = 'Autumn18-mAODv1-10222'

from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "fastMAOD" 
config.General.workArea = 'crab_miniAOD_%s' % tag
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = '../../cfg/miniAOD_mc_fast_102X_Autumn18.py'
config.JobType.psetName = '../../cfg/miniAODv1_Autumn18_fast_10_2_22.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 3500
config.section_("Data")
#config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.totalUnits  = 500000 
config.Data.unitsPerJob = 5000
#config.Data.totalUnits  = 50000 
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.ignoreLocality = False

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_CERN_CH', 'T1_US_FNAL_Disk'] #Run where the PU dataset is, not where the sample is
config.section_("User")

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    for input_dataset in [
    "/ttZ01j_lepWFilter/schoef-ttZ01j_lepWFilter-899787a12e1226a4d09ffc9eefc66945/USER",
    "/tWZtoLL01j_lepWFilter/schoef-tWZtoLL01j_lepWFilter-42ad673a357d0ca33dba80eecc7261d9/USER",
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        config.Data.outputDatasetTag = tag 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
