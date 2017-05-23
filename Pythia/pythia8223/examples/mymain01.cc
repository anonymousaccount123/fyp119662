//Headers and Namespaces.
#include "Pythia8/Pythia.h" // include pythia headers

using namespace Pythia8; 	// implicit pythia8::
int main() {
	//setting up a generation
	Pythia pythia; //so a Pythia is a class
	pythia.readString("Top:gg2ttbar = on"); // We switch on a process using readstring command
	//pythia.readString("HiggsSM:gg2H = on"); // add a new process
	pythia.readString("Beams:eCM = 8000."); // 8 TeV CoM energy
	//pythia.readString("Next:numberShowEvent = 5"); // for reading a number of events greater than one
	
	
	pythia.init(); // Initialize, pp beams is default
	
	// Histogramming the events ooo...
	Hist pT("top blah blah", 100, 0.,200.);
	Hist eta("top pseudorapidity", 100,-5,5.);
    // arguments: name, no of bins, lower edge, upper edge
	
	
	// Now to generate event/s. this is an example event loop
	for (int iEvent = 0; iEvent < 1000; ++iEvent){
		
		// A loop to access all the particles in the event record
		
		//for (int i = 0; i < pythia.event.size(); ++i){
		//	cout << "i = " << i << ", id = " << pythia.event[i].id() << endl;
		//}
		
		//If we want to find the "definitive top production kinematics, just before the decay
		//we check in the loop for the last appearance fo the top by adding:
		
		//int iTop = 0; // right before the particle loop
		//if (pythia.event[i].id()== 6) iTop = i;  // inside the particle loop
		
		
		//then at the end of each even loop the iTop will give you the final top in the event record
		
		//example, finding the transverse momentum and pseudorapidity finder for the final top:
		int iTop = 0;
		for (int i = 0; i < pythia.event.size(); ++i){
			if (pythia.event[i].id()== 6) iTop = i;
		}
		//cout << "The final top has pT : " << pythia.event[iTop].pT() << "  and eta : " << pythia.event[iTop].eta() << endl;
		
		// we want to fill the heastogram in each event:
		pT.fill( pythia.event[iTop].pT() );
		eta.fill( pythia.event[iTop].eta() );
		
		
		
		pythia.next();
	}
	
	//to write out the histograms:
	cout << pT << eta;
	
	// For better data analysis consider saving the output of the kinematic variables and processing them in Python
	
	
	//pythia.next(); // Generates an event, fills the event record.
	pythia.stat();
	return 0;
}
// To compile you simply "make mymain01"
// To run ./mymain01.exe > myout01