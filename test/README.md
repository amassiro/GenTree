Instructions
====

See
    https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsTemplateCrossSection
    
Where:

    /afs/cern.ch/user/a/amassiro/work/LHCXSWG/CMSSW_8_0_19/src/GeneratorInterface/GenTree
    
Run

    cmsRun GenTree_cfg.py
    
    
    cmsRun GenTree_powheg_cfg.py
    cmsRun GenTree_powheg_nnlops_cfg.py
    cmsRun GenTree_amcatnlo_cfg.py

    cmsRun GenTree_powheg_nnlops_ATLAS_cfg.py
    cmsRun GenTree_powheg_nnlops_CMS_cfg.py
    cmsRun GenTree_powheg_nnlops_CMS_private_cfg.py

    
    r99t  gentree.root
    tree = (TTree*) _file0->Get("GenTree/gentree")
    tree->Draw("jets30")
    
    
Add uncertainties to the tree:

    voms-proxy-init --voms cms

    cmsRun GenTree_powheg_nnlops_CMS_cfg.py

    addUncertainty  gentree_powheg_nnlops_cms_tune.root   gentree_powheg_nnlops_cms_tune_uncertainty.root     
    addUncertainty  /tmp/amassiro/gentree_powheg_nnlops_cms_tune.root   /tmp/amassiro/gentree_powheg_nnlops_cms_tune_uncertainty.root     
    
    r99t gentree_powheg_nnlops_cms_tune_uncertainty.root Table.cxx
    r99t /tmp/amassiro/gentree_powheg_nnlops_cms_tune_uncertainty.root Table.cxx
       
    
    r99t gentree_powheg_nnlops_cms_tune_uncertainty.root 
    tree = (TTree*) _file0->Get("GenTree/gentree")
    tree->Draw("stage1_cat_pTjet30GeV")
    
    
Original script by Dag:

    https://indico.cern.ch/event/618048/attachments/1430472/2204126/ggF_qcd_uncertainty_2017.cxx
    
    https://indico.cern.ch/event/628660/?filterActive=1&showDate=2017-05-16
    
    
    
Draw

    r99t  gentree_powheg_nnlops_cms_tune.root  gentree_powheg_nnlops_cms_tune_private.root DrawComparison.cxx\(\"higgs_pt\",81,0,405,\"Higgs\ p_\{T\}\ \[GeV\]\"\)



    r99t  gentree_powheg_nnlops_cms_tune.root   DrawSingle.cxx\(\"higgs_pt\",40,0,200,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    
    r99t  gentree_powheg_nnlops_cms_tune.root   DrawSingle.cxx\(\"higgs_pt\",81,0,405,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    r99t  gentree_powheg_nnlops_atlas_tune.root DrawSingle.cxx\(\"higgs_pt\",81,0,405,\"Higgs\ p_\{T\}\ \[GeV\]\"\)

    r99t  gentree_powheg_nnlops_cms_tune.root  gentree_powheg_nnlops_atlas_tune.root DrawComparison.cxx\(\"higgs_pt\",81,0,405,\"Higgs\ p_\{T\}\ \[GeV\]\"\)

    
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    Draw.cxx
    
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    Draw.cxx\(\"jets30\",5,0,5,\"n\ jet\ 30\ GeV\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    Draw.cxx\(\"higgs_pt\",20,0,200,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    Draw.cxx\(\"higgs_eta\",20,-6,6,\"Higgs\ #eta\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    Draw.cxx\(\"jet1_pt\",20,0,200,\"jet1\ p_\{T\}\ \[GeV\]\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    Draw.cxx\(\"higgs_pt\",26,0,260,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    Draw.cxx\(\"jets30\",5,0,5,\"n\ jet\ 30\ GeV\"\)
    

    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    DrawNjetCorrected.cxx\(\"higgs_pt\",20,0,200,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    DrawNjetCorrected.cxx\(\"jets30\",5,0,5,\"n\ jet\ 30\ GeV\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    DrawNjetCorrected.cxx\(\"higgs_eta\",20,-6,6,\"Higgs\ #eta\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    DrawNjetCorrected.cxx\(\"jet1_pt\",20,0,200,\"jet1\ p_\{T\}\ \[GeV\]\"\)


    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    DrawHpTCorrected.cxx\(\"higgs_pt\",20,0,200,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    DrawHpTCorrected.cxx\(\"jets30\",5,0,5,\"n\ jet\ 30\ GeV\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    DrawHpTCorrected.cxx\(\"higgs_eta\",20,-6,6,\"Higgs\ #eta\"\)
    r99t   gentree_powheg.root  gentree_powheg_nnlops.root   gentree_amcatnlo.root    DrawHpTCorrected.cxx\(\"jet1_pt\",20,0,200,\"jet1\ p_\{T\}\ \[GeV\]\"\)
    

    
Check scale variation:


    /tmp/amassiro/gentree_powheg_nnlops_cms_tune_uncertainty.root

    
    r99t  /tmp/amassiro/gentree_powheg_nnlops_cms_tune_uncertainty.root   DrawSingleScaleVariation.cxx\(\"higgs_pt\",40,0,200,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    
    r99t  /tmp/amassiro/gentree_powheg_nnlops_cms_tune_uncertainty.root   DrawSingleScaleVariation.cxx\(\"higgs_pt\",50,0,300,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    
    r99t  /tmp/amassiro/gentree_powheg_nnlops_cms_tune_uncertainty.root   DrawSingleScaleVariation.cxx\(\"higgs_pt\",50,0,1000,\"Higgs\ p_\{T\}\ \[GeV\]\"\)
    
    

    r99t  /tmp/amassiro/gentree_powheg_nnlops_cms_tune_uncertainty.root   CalculateScaleVariation.cxx
       --> values.txt
       
    r99t GetScaleVariation.cxx
    
    
Example output:

     njet:pt_H 0 : 0    smaller +/- -25.5441 %     greater +/- 8.99985 % 
     njet:pt_H 0 : 1    smaller +/- -0.385311 %     greater +/- 22.7309 % 
     njet:pt_H 0 : 2    smaller +/- -6.04268e-06 %     greater +/- inf % 
     njet:pt_H 0 : 3    smaller +/- -6.04268e-06 %     greater +/- inf % 
     njet:pt_H 1 : 0    smaller +/- -18.6496 %     greater +/- 0.199579 % 
     njet:pt_H 1 : 1    smaller +/- -2.32479 %     greater +/- 2.47356 % 
     njet:pt_H 1 : 2    smaller +/- -0.543701 %     greater +/- 5.11504 % 
     njet:pt_H 1 : 3    smaller +/- -0.126483 %     greater +/- 7.42588 % 
     njet:pt_H 2 : 0    smaller +/- -9.65114 %     greater +/- 0.132244 % 
     njet:pt_H 2 : 1    smaller +/- -3.67025 %     greater +/- 1.41323 % 
     njet:pt_H 2 : 2    smaller +/- -1.20915 %     greater +/- 3.15546 % 
     njet:pt_H 2 : 3    smaller +/- -0.341676 %     greater +/- 5.44669 % 
     njet:pt_H 3 : 0    smaller +/- -11.0656 %     greater +/- 0.0393883 % 
     njet:pt_H 3 : 1    smaller +/- -3.50812 %     greater +/- 0.941225 % 
     njet:pt_H 3 : 2    smaller +/- -1.87696 %     greater +/- 2.27198 % 
     njet:pt_H 3 : 3    smaller +/- -0.905543 %     greater +/- 4.56983 % 

    
    
    
Decay chain draw:

    cmsRun ParticleTreeDrawer_cfg.py   inputFiles=many::samples_petrucciani_MG.py  \
                                       outputFile=/tmp/amassiro/test.root
                              
                              
    
    


    
