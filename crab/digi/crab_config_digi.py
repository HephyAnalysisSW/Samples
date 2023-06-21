tag = '22-05-12'

from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_digi_%s' % tag
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../cfg/digi_mc_UL18.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.numCores = 1
config.JobType.maxMemoryMB = 3000

config.section_("Data")
#config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.totalUnits  = 5000000 
config.Data.unitsPerJob = 2000
#config.Data.totalUnits  = 50000 
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.ignoreLocality = True

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
config.Site.whitelist = ['T1_US_FNAL', 'T2_CH_CERN', 'T2_AT_Vienna', 'T1_UK_RAL', 'T2_DE_DESY', 'T2_DE_RWTH', 'T2_IT_Bari', 'T2_IT_Rome', 'T2_IT_Pisa' ] #Run where the PU dataset is, not where the sample is
config.section_("User")

if __name__ == '__main__':

    for input_dataset in [
        '/TTTT_MS_EFTdecay/schoef-22-05-12-128efeffab8ceb577467d0e58be013b1/USER',
        '/TTbb_MS_EFT/schoef-22-05-12-128efeffab8ceb577467d0e58be013b1/USER',
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        config.Data.outputDatasetTag = tag 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
