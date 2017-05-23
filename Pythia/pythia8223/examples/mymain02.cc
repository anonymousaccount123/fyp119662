//Headers and Namespaces.
#include "Pythia8/Pythia.h" // include pythia headers
using namespace Pythia8; 	// implicit pythia8::

//This program will locate all the kinematic variables of Higgs production from the channel gg -> H0 -> bbar of the bbar pair 




int main() {
	
	Pythia pythia;
	pythia.readString("HiggsSM:gg2H = on");
	pythia.readString("Beams:eCM = 8000.");
	pythia.readString("Next:numberShowEvent = 0");
	pythia.readString("Random:SetSeed = 0");
	pythia.init();
		
	
	
	// optional histogram
	Hist pT("transverse momentum of higgs", 100, 0.,200.);
	Hist y("True rapidity", 100,-5,5.);
	Hist eta("Pseudo rapidity",100,-5,5.);
	for (int iEvent = 0; iEvent < 100 ; ++iEvent){
		
		
		
		int ib   = 0;
		int ibbar= 0;
		int imum = 0;
		
		for (int i = 0; i < pythia.event.size(); ++i){
			
			if (pythia.event[i].id()== 5 && pythia.event[i].pT() > 25 && pythia.event[pythia.event[i].mother1()].id() == 25 ) 
				ib = i;
				imum = pythia.event[i].mother1();
		}
		
		for (int i = 0; i < pythia.event.size(); ++i){
			
			if (pythia.event[i].id()== -5 && pythia.event[i].pT() > 25 && pythia.event[pythia.event[i].mother1()].id() == 25) ibbar = i;
		}
		
		// Here we would print out any qualities of ib and ibbar that we want to save.
		if (ib != 0 && ibbar !=0){
			cout<<pythia.event[ib].eta()<< endl << pythia.event[ib].pT()<< endl <<pythia.event[ib].phi()<< endl;
			cout<<pythia.event[ib].px()<< endl << pythia.event[ib].py()<< endl << pythia.event[ib].pz() << pythia.event[ib].e()<< endl;
			cout<<pythia.event[ibbar].eta()<< endl << pythia.event[ibbar].pT()<< endl <<pythia.event[ibbar].phi()<< endl;
			cout<<pythia.event[ibbar].px()<< endl << pythia.event[ibbar].py()<< endl << pythia.event[ibbar].pz() << pythia.event[ibbar].e()<< endl;
			cout<<pythia.event[imum].eta()<< endl << pythia.event[imum].pT()<< endl <<pythia.event[imum].phi()<< endl;
			cout<<pythia.event[imum].px()<< endl << pythia.event[imum].py()<< endl << pythia.event[imum].pz() << pythia.event[imum].e()<< endl;
		}
		pythia.next();
	}
	return 0;
}