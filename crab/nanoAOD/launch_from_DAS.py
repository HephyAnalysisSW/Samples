import imp, os, sys
from optparse import OptionParser
import re, subprocess
from math import ceil
from Samples.Tools.config import  redirector

cfgPath    = os.path.expandvars( "$CMSSW_BASE/src/Samples/cfg/" )
allConfigs = [ x.strip( ".py" ) for x in os.listdir( cfgPath ) if x.endswith(".py") ]

parser = OptionParser(usage="python launch.py [options] component1 [ component2 ...]", \
                          description="Launch heppy jobs with CRAB3. Components correspond to the variables defined in heppy_samples.py (their name attributes)")
parser.add_option("--production_label", dest="production_label",                                  default="heppy", help="production label")
parser.add_option("--remoteDir",        dest="remoteDir",                                         default="",      help="remote subdirectory")
parser.add_option("--unitsPerJob",      dest="unitsPerJob",      type=int,                        default=1,       help="Nr. of units (files) / crab job")
parser.add_option("--totalUnits",       dest="totalUnits",       type=int,                        default=None,    help="Total nr. of units (files)")
parser.add_option("--config",           dest="config",                     choices = allConfigs,                   help="Which config?")
parser.add_option("--sample",           dest="sample",                                                             help="Which sample?")
parser.add_option("--inputDBS",         dest="inputDBS",          choices = ['phys03','global'],  default="global",help="Private or global production?")
parser.add_option("--publish",          action='store_true',                                      default=False,   help="Publish on dbs?")
parser.add_option("--runOnNonValid",    action='store_true',                                      default=False,   help="Allow running on invalid samples/samples still in production?")
parser.add_option("--sorted",           action='store_true',                                      default=False,   help="sort filelist by ending integer (only for local processing)")
parser.add_option('--nJobs',            action='store',          type=int,                        default=1,       help="Maximum number of simultaneous jobs.")
parser.add_option('--job',              action='store',          type=int,                        default=0,       help="Run only job i")
( options, args ) = parser.parse_args()

os.system("scram runtime -sh")
os.system("source /cvmfs/cms.cern.ch/crab3/crab.sh")

os.environ['CRAB_RUNONNONVALID'] = 'True' if options.runOnNonValid else 'False'
print "## Running on non-valid input dataset is set to: %s"%os.environ['CRAB_RUNONNONVALID']

os.environ["CRAB_PUBLISH"] = 'True' if options.publish else 'False'
print "## Publication is set to", os.environ["CRAB_PUBLISH"]

## Config selection
os.environ["CMSRUN_CFG"] = os.path.join( cfgPath, "%s.py" % options.config )
print "## Will use the following config: %s"%os.environ["CMSRUN_CFG"]

os.system("which crab")

#os.environ["CMG_REMOTE_DIR"]  = options.remoteDir
os.environ["CRAB_UNITS_PER_JOB"] = str(options.unitsPerJob)
if options.totalUnits:
    os.environ["CRAB_TOTAL_UNITS"] = str(options.totalUnits)


DASname, DAScampaign, DAStier = options.sample.split('/')[1:]

os.environ["CRAB_PROD_LABEL"]  = DAScampaign + "_" + options.production_label

os.environ["ORIG_PROD_LABEL"]   = options.production_label
os.environ["MAOD_SAMPLE_NAME"]  = DASname+"_"+DAScampaign

os.environ["CRAB_DATASET"]      = options.sample
os.environ["CRAB_input_DBS"]    = options.inputDBS

#os.system("crab submit --dryrun -c crabConfig.py")
os.system("crab submit -c crabConfig.py")
#os.system("crab preparelocal crabConfig.py")

