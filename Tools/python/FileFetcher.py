import os
import subprocess

def FileFetcher( filename, target_name = None, overwrite=False, verbose=False):
    if filename.startswith('root://'):
        target = os.path.join( os.getcwd(), filename.split('/')[-1] if target_name is None else target_name)
        if os.path.exists( target ) and not overwrite:
            if verbose: print ("File {target} found. Do nothing".format(target=target))
            return target
        elif os.path.exists( target ) and overwrite: 
            if verbose: print ("Delete {target}".format(target=target))  
            os.remove( target )
        print( "Downloading file {filename} to {target}".format( filename=filename, target=target ) )
        subprocess.call( 'xrdcp {filename} {target}'.format( filename=filename, target=target ), shell=True)
        return target
    else:
        return None

if __name__=="__main__":
    filename = FileFetcher("root://eos.grid.vbc.ac.at//eos/vbc/experiments/cms/store/user/schoef/allOps-t-sch-RefPoint-noWidthRW/allOps-t-sch-RefPoint-noWidthRW/220910_110355/0000/GEN_LO_0j_102X_26.root", verbose=True, overwrite=True)
    print (filename)
