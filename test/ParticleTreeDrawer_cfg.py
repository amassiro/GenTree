import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')


options.parseArguments()



process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 1000




process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring (),
    inputCommands=cms.untracked.vstring(
                  'keep *',
                  'drop CandidateTracks_candidateTrackProducer_*_*',
          )
)

if "many::" not in str(options.inputFiles):
    #process.source.fileNames.append(str(options.inputFiles))
    process.source.fileNames = cms.untracked.vstring (options.inputFiles)
else :
  # many:: -> 6 characters
  name_file = str((options.inputFiles)[0]) [6:]
  print " name_file = " , name_file, " <<-- " ,  str(options.inputFiles)
  list_inputFiles = open(name_file,"r")
  for file_to_add in list_inputFiles:
    print " --> ", file_to_add
    process.source.fileNames.append ( file_to_add )






process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
                                   #src = cms.InputTag("genParticles"), 
                                   src = cms.InputTag("prunedGenParticles"), 
                                   printP4 = cms.untracked.bool(False),
                                   printPtEtaPhi = cms.untracked.bool(False),
                                   printVertex = cms.untracked.bool(False),
                                   printStatus = cms.untracked.bool(False),
                                   printIndex = cms.untracked.bool(False),
                                   status = cms.untracked.vint32( 3 )
                                   )



process.p = cms.Path(process.printTree)



