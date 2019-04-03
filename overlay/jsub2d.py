import sys
import os






plottype=["zr_col1", "zr_col1fin", "zr_col2", "zr_col4", "zr_col5", "zr_ucoil", "zr_dcoil", "zr_bpipe"]
title=["Dep. Power(W/uA/mm^2) vs rz (mm^2) [col1]",
       "Dep. Power(W/uA/mm^2) vs rz (mm^2) [col1fin]",
       "Dep. Power(W/uA/mm^2) vs rz (mm^2) [col2]",
       "Dep. Power(W/uA/mm^2) vs rz (mm^2) [col4]",
       "Dep. Power(W/uA/mm^2) vs rz (mm^2) [col5]",
       "Dep. Power(W/uA/mm^2) vs rz (mm^2) [ucoil]",
       "Dep. Power(W/uA/mm^2) vs rz (mm^2) [dcoil]",
       "Dep. Power(W/uA/mm^2) vs rz (mm^2) [bpipe]"]


for i in range(0,8):
	os.system("python overlay2d.py \""+plottype[i]+"\" \""+title[i]+"\"")	


"""
jsubf=open(jsub+"/"+tag+"_"+particle+".pbs", "w")
jsubf.write("#!/bin/bash\n")
jsubf.write("#PBS -S /bin/bash\n")
jsubf.write("#PBS -o "+tmp+"/"+tag+"_"+particle+".out\n")
jsubf.write("#PBS -e "+tmp+"/"+tag+"_"+particle+".err\n")
jsubf.write("# Script for running sensitivity analysis\n")
jsubf.write("cd "+jsub+"/../\n")
jsubf.write("echo \"Current working directory is `pwd`\"\n")
jsubf.write("echo \"Node file: $PBS_NODEFILE:\"\n")
jsubf.write("echo \"-----------------------------\"\n")
jsubf.write("cat $PBS_NODEFILE\n")
jsubf.write("echo \"-----------------------------\"\n")
jsubf.write("CORES=`/bin/awk 'END {print NR}' $PBS_NODEFILE`\n")
jsubf.write("echo \"Running on $CORES cores.\"\n")
jsubf.write("echo \"Starting run at: `date`\"\n")
jsubf.write("module load root-cern/6.14.04-gcc52\n")
jsubf.write("export OMP_NUM_THREADS=$CORES\n")
jsubf.write("python processD.py \""+src+"\" \""+dest+"\" \""+tag+"\" \""+particle+"\" \n")
jsubf.write("echo \"Program analysis finished with exit code $? at: `date`\"\n")
jsubf.close()
                            
if os.path.exists(dest+".root"):
	c=1
else:
	os.system("qsub -l nodes=1:ppn=4,pmem=3gb,walltime=01:15:00 "+jsub+"/"+tag+"_"+particle+".pbs")
							
"""
