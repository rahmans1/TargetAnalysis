import sys
import os






plottype=["r_all_27", "r_27", "r_all_26", "r_26", "r_all_25", "r_25", "r_all_24", "r_24", "r_all_28", "r_28", "r_all_29", "r_29"]
title=["Inc. Power(W/uA/mm) vs r (mm) [US1,all]","Inc. Power(W/uA/mm) vs r (mm) [US1,E>1MeV]",
       "Inc. Power(W/uA/mm) vs r (mm) [US2,all]","Inc. Power(W/uA/mm) vs r (mm) [US2,E>1MeV]",
       "Inc. Power(W/uA/mm) vs r (mm) [DS1,all]","Inc. Power(W/uA/mm) vs r (mm) [DS1,E>1MeV]",
       "Inc. Power(W/uA/mm) vs r (mm) [DS2,all]","Inc. Power(W/uA/mm) vs r (mm) [DS2,E>1MeV]",
       "Inc. Power(W/uA/mm) vs r (mm) [M,all]","Inc. Power(W/uA/mm) vs r (mm) [M,E>1MeV]",
       "Inc. Power(W/uA/mm) vs r (mm) [EH,all]","Inc. Power(W/uA/mm) vs r (mm) [EH,E>1MeV]"]


for i in range(0,12):
	os.system("python overlay.py \""+plottype[i]+"\" \""+title[i]+"\"")	


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
