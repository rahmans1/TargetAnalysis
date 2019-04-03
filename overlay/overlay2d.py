import sys
import os
import ROOT as R


def integral(h,xmin,xmax):
	axis=h.GetYaxis()
	bmin=axis.FindBin(xmin)
	bmax=axis.FindBin(xmax)
	integral=h.Integral(0,-1,bmin,bmax)
       
      # integral =integral-h.GetBinContent(bmin)*(xmin-axis.GetBinLowEdge(bmin))/axis.GetBinWidth(bmin)
      #	integral = integral-h.GetBinContent(bmax)*(axis.GetBinUpEdge(bmax)-xmax)/axis.GetBinWidth(bmax)
	return integral;
plottype=sys.argv[1]
title=sys.argv[2]


R.gStyle.SetOptStat(0)

src="/global/scratch/rahmans/root/beam_analysis"
tag=["col2_15cm_BS_newraster_hp_R0.0", "col2_15cm_BS_newraster_hp_R0.3", "col2_15cm_BS_newraster_hp_R-0.3"]
particle=["all","e-","e+","y", "p", "n", "pi0","pi-","pi+"]

scale={}





c=R.TCanvas("c","c",800,800)
c.Divide(1,3)
f=[]
histo=[]


maxi=0
count=0
size=len(particle)
integrals=open("/global/scratch/rahmans/fig/beamStudy/"+plottype+".txt","w+")

for part in particle:
	for filename in tag:
                f.append(R.TFile(src+"/"+filename+"_"+part+".root"))
                histo.append(f[count].Get(plottype))
		if count==0:
			maxi=histo[count].GetMaximum()
		else:
			histo[count].SetMaximum(maxi)
		if (plottype=="zr_col2" or plottype=="zr_col4"):
			integrals.write(filename+" "+part+" "+plottype+" "+str(integral(histo[count],0.0,300.0))+"\n")
		else:		
			integrals.write(filename+" "+part+" "+plottype+" "+str(histo[count].Integral())+"\n")
                c.cd(tag.index(filename)+1)
		R.gPad.SetRightMargin(0.15)
		R.gPad.SetLogz()
                histo[count].SetTitle(title)
		histo[count].Draw("colz")
		(histo[count].GetZaxis()).SetLabelSize(0.08)
                count=count+1	
        c.Print("/global/scratch/rahmans/fig/beamStudy/"+plottype+"_"+part+".png")
integrals.close()

		







