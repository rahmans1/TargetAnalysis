import sys
import os
import ROOT as R


def integral(h,xmin,xmax):
	axis=h.GetXaxis()
	bmin=axis.FindBin(xmin)
	bmax=axis.FindBin(xmax)
	integral=h.Integral(bmin,bmax)
       # integral =integral-h.GetBinContent(bmin)*(xmin-axis.GetBinLowEdge(bmin))/axis.GetBinWidth(bmin)
#	integral = integral-h.GetBinContent(bmax)*(axis.GetBinUpEdge(bmax)-xmax)/axis.GetBinWidth(bmax)
	return integral;
plottype=sys.argv[1]
title=sys.argv[2]

src="/global/scratch/rahmans/root/beam_analysis"
tag=["col2_15cm_BS_newraster_hp_R0.0", "col2_15cm_BS_newraster_hp_R0.3", "col2_15cm_BS_newraster_hp_R-0.3"]
particle=["all","e-","e+","y", "p", "n", "pi0","pi-","pi+"]
rate=[]
color={}
style={}

color["all"]=1
color["e-"]=4
color["e+"]=2
color["y"]=5
color["p"]=6
color["n"]=3
color["pi0"]=28
color["pi-"]=7
color["pi+"]=46

style[tag[0]]=1
style[tag[1]]=2
style[tag[2]]=3


c=R.TCanvas("c","c",800,800)
c.SetLogy()
f=[]
histo=[]

h=R.THStack(plottype,title);
l=R.TLegend(0.75,0.6,0.9,0.9, "PID", "NDC")
count=0
size=len(particle)
integrals=open("/global/scratch/rahmans/fig/beamStudy/"+plottype+".txt","w+")

for part in particle:
	for filename in tag:
                f.append(R.TFile(src+"/"+filename+"_"+part+".root"))
                histo.append(f[count].Get(plottype))
		if filename==tag[0]:
			l.AddEntry(histo[count], part,"L")
		histo[count].SetLineColor(color[part])
		histo[count].SetLineWidth(style[filename])
		for i in range(0,20):
                	integrals.write(filename+" "+part+" "+str(integral(histo[count],i*5,(i+1)*5))+"\n")
		h.Add(histo[count])
                count=count+1
                print(str(count)+"\n")
	


h.Draw("HISTnostack")
l.Draw()	
c.Print("/global/scratch/rahmans/fig/beamStudy/"+plottype+".png")
integrals.close()

		







