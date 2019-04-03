int overlay(){

const char src[64]="/global/scratch/rahmans/root/beam_analysis/ucoil_length_right";
const char tag[3][32]={"col2_15cm_NBS_oldraster", "col2_15cm_BS_oldraster", "col2_15cm_BS_newraster"};
const char particle[9][16]={"all","e-","e+","y", "p", "n", "pi0","pi-","pi+"};


for (int i=0;i<9;i++){
	for (int j=0;j<3;j++){
		auto file=new TFile(Form("%s/%s_%s.root",src,tag[j],particle[i]));
                std::cout<<Form("Reading file %s/%s_%s.root",src,tag[j],particle[i])<<std::endl; 
		TIter next(file->GetListOfKeys());
		while (auto key=(TKey *) next()){
			if (((TString) key->GetClassName()).EqualTo("TH1F")){
				TH1F *h=(TH1F *) gDirectory->Get(key->GetName());
                                std::cout << key->GetName() << " "<< h->Integral()<< std::endl;
				h->SetDirectory(0);
			} else {
				TH2F *h=(TH2F *) gDirectory->Get(key->GetName());
				std::cout << key->GetName() << " "<< h->Integral()<< std::endl;
				h->SetDirectory(0);
			}					
		}

		file->Close();
                delete file;
                delete next;
	}
}

return 0;
}
