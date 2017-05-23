//Headers and Namespaces.
#include "Pythia8/Pythia.h" // include pythia headers
using namespace Pythia8; 	// implicit pythia8::

//This program will locate all the kinematic variables of Higgs production from the channel gg -> H0 -> bbar of the bbar pair 




int main() {
	
	Pythia pythia;
	pythia.readString("HardQCD:gg2bbbar = on");
	pythia.readString("Beams:eCM = 8000.");
	pythia.readString("Next:numberShowEvent = 0");
	pythia.readString("Random:SetSeed = on");
	pythia.readString("Random:seed = 0");
	pythia.init();
		
	
	
	// optional histogram
	Hist pT("transverse momentum of higgs", 100, 0.,200.);
	Hist y("True rapidity", 100,-5,5.);
	Hist eta("Pseudo rapidity",100,-5,5.);
	for (int iEvent = 0; iEvent < 1000 ; ++iEvent){
		
		
		
		int ib   = 0;
		int ibbar= 0;
		int imum = 0;
		
		for (int i = 0; i < pythia.event.size(); ++i){
			
			if (pythia.event[i].id()== 5 && pythia.event[i].pT() > 25 && pythia.event[pythia.event[i].mother1()].id() == 21 ) 
				ib = i;
				imum = pythia.event[i].mother1();
		}
		
		for (int i = 0; i < pythia.event.size(); ++i){
			
			if (pythia.event[i].id()== -5 && pythia.event[i].pT() > 25 && pythia.event[pythia.event[i].mother1()].id() == 21) ibbar = i;
		}
		
		// Here we would print out any qualities of ib and ibbar that we want to save.
		if (ib != 0 && ibbar !=0){
			cout<<pythia.event[ib].eta()<< "\t" << pythia.event[ib].pT()<< "\t" <<pythia.event[ib].phi()<< "\t";
			cout<<pythia.event[ib].px()<< "\t" << pythia.event[ib].py()<< "\t" << pythia.event[ib].pz() <<"\t"<< pythia.event[ib].e()<< "\t";
			cout<<pythia.event[ibbar].eta()<< "\t" << pythia.event[ibbar].pT()<< "\t" <<pythia.event[ibbar].phi()<< "\t";
			cout<<pythia.event[ibbar].px()<< "\t" << pythia.event[ibbar].py()<< "\t" << pythia.event[ibbar].pz()<< "\t" << pythia.event[ibbar].e()<< "\t";
			cout<<pythia.event[imum].eta()<< "\t" << pythia.event[imum].pT()<< "\t" <<pythia.event[imum].phi()<< "\t";
			cout<<pythia.event[imum].px()<< "\t" << pythia.event[imum].py()<< "\t" << pythia.event[imum].pz() << "\t"<<pythia.event[imum].e()<< endl;
		}
		pythia.next();
	}
	return 0;
}