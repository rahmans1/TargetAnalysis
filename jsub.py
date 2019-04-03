import sys
import os


src=sys.argv[1]
tag=sys.argv[2]
particle=sys.argv[3]



jsub="/home/rahmans/analysis/BeamSteeringAnalysis/plane/jsub"
dest="/global/scratch/rahmans/root/beam_analysis"
tmp="/global/scratch/rahmans/tmp/beam_analysis"

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
	os.system("qsub -l nodes=2:ppn=4,pmem=3gb,walltime=02:00:00 "+jsub+"/"+tag+"_"+particle+".pbs")
							

