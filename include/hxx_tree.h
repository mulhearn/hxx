#ifndef HXX_TREE_H
#define HXX_TREE_H

class TTree;

enum {LFMUMU=0, LFEMEM=1, LFEMMU=2}; // lpeton flavors

class hxx_tree {
public:
   hxx_tree();

   int sample;
   double weight;  
   double weight_met; // allows for rethrowing MET...
   int lepton_flavor;

   // multiplicities
   int nelec;
   int nmuon;
   int njet;
   
   // dilepton variables:
   double l1_pt;
   double l1_eta;
   double l1_phi;
   double l2_pt;
   double l2_eta;
   double l2_phi;
   double mll;

   // jet variables: (these have to be pointers because ... you know ... ROOT.)
   std::vector<double>  * jet_pt;
   std::vector<double>  * jet_eta;
   std::vector<double>  * jet_phi;
   std::vector<int>     * jet_btag;
   std::vector<int>     * jet_tautag;
   // (if adding variables, don't forget to add to clear() / erase() function!  Could easily go unnoticed and out of sync!...)
   void erase_jet(int i);

   // met variables:
   double met, met_phi;
   double nopu_met, nopu_met_phi;

   // Read/Write data in this class to a TTree
   // Note:  due to ROOT silliness, you must call ReadTree *before* WriteTree if doing both...
   void ReadTree(TTree * tree);
   void WriteTree(TTree * tree);
   void Clear();

};

#endif
