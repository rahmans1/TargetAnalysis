#define processD_cxx
// The class definition in processD.h has been generated automatically
// by the ROOT utility TTree::MakeSelector(). This class is derived
// from the ROOT class TSelector. For more information on the TSelector
// framework see $ROOTSYS/README/README.SELECTOR or the ROOT User Manual.


// The following methods are defined in this file:
//    Begin():        called every time a loop on the tree starts,
//                    a convenient place to create your histograms.
//    SlaveBegin():   called after Begin(), when on PROOF called only on the
//                    slave servers.
//    Process():      called for each event, in this function you decide what
//                    to read and fill your histograms.
//    SlaveTerminate: called at the end of the loop on the tree, when on PROOF
//                    called only on the slave servers.
//    Terminate():    called at the end of the loop on the tree,
//                    a convenient place to draw/fit your histograms.
//
// To use this file, try the following session on your Tree T:
//
// root> T->Process("processD.C")
// root> T->Process("processD.C","some options")
// root> T->Process("processD.C+")
//


#include "processD.h"
#include <TH2.h>
#include <TStyle.h>


TString folder;
TString tag;
TString generator;

TFile* rootfile;

std::map<TString,Int_t> pid;

std::map<Int_t,Float_t > openmin;
std::map<Int_t, Float_t > transmin;
std::map<Int_t, Float_t> closedmin;
std::map<Int_t,Float_t > openmax;
std::map<Int_t, Float_t > transmax;
std::map<Int_t, Float_t> closedmax;



void processD::Begin(TTree * /*tree*/)
{
   // The Begin() function is called at the start of the query.
   // When running with PROOF Begin() is only called on the client.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();
   TObjArray *opt= option.Tokenize(",");
   folder=((TObjString *)(opt->At(0)))->String();
   tag= ((TObjString *)(opt->At(1)))->String();
   generator=((TObjString *)(opt->At(2)))->String();
   rootfile=new TFile(Form("%s/%s_%s.root",folder.Data(),tag.Data(),generator.Data()) , "RECREATE");
   
   pid["e-"]=11;

   openmin[28]=935; openmax[28]=1040;
   transmin[28]=960; transmax[28]=1075;
   closedmin[28]=960; closedmax[28]=1100;

   openmin[32]=885; openmax[32]=990;
   transmin[32]=885; transmax[32]=990;
   closedmin[32]=885; closedmax[32]=990;

}

void processD::SlaveBegin(TTree * /*tree*/)
{
   // The SlaveBegin() function is called after the Begin() function.
   // When running with PROOF SlaveBegin() is called on each slave server.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();

}

Bool_t processD::Process(Long64_t entry)
{
   // The Process() function is called for each entry in the tree (or possibly
   // keyed object in the case of PROOF) to be processed. The entry argument
   // specifies which entry in the currently loaded tree is to be processed.
   // When processing keyed objects with PROOF, the object is already loaded
   // and is available via the fObject pointer.
   //
   // This function should contain the \"body\" of the analysis. It can contain
   // simple or elaborate selection criteria, run algorithms on the data
   // of the event and typically fill histograms.
   //
   // The processing can be stopped by calling Abort().
   //
   // Use fStatus to set the return value of TTree::Process().
   //
   // The return value is currently not used.

   fReader.SetEntry(entry);

   return kTRUE;
}

void processD::SlaveTerminate()
{
   // The SlaveTerminate() function is called after all entries or objects
   // have been processed. When running with PROOF SlaveTerminate() is called
   // on each slave server.

}

void processD::Terminate()
{

   rootfile->Close();
   // The Terminate() function is the last function to be called during
   // a query. It always runs on the client, it can be used to present
   // the results graphically or save the results to file.

}
