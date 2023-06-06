tag = '22-05-12'

from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_sim_%s' % tag
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../cfg/sim_mc_UL18.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 3000

config.section_("Data")
#config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.totalUnits  = 5000000 
config.Data.unitsPerJob = 500
#config.Data.totalUnits  = 50000 
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T1_US_FNAL', 'T1_US_FNAL'] #Run where the PU dataset is, not where the sample is
config.section_("User")

if __name__ == '__main__':

    for input_dataset in [
        '/TTTT_MS_EFTdecay/lwild-TTTT_MS_EFTdecay-c9278d5dad30c5b88f7ba5ad37f5f2d0/USER',
        '/TTbb_MS_EFT/lwild-TTbb_MS_EFT-c9278d5dad30c5b88f7ba5ad37f5f2d0/USER',
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        config.Data.outputDatasetTag = tag 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
