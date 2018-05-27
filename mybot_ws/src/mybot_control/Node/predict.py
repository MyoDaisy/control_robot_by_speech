import os
import cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import time

#path to training data  
modelpath = "speaker_models/"

gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]

#Load the Gaussian gender Models
models = []
for i in range(len(gmm_files)):
    file = open(gmm_files[i], 'rb')
    models.insert(i, cPickle.load(file))
speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
              in gmm_files]

# Read the test directory and get the list of test audio files 

def chooseAction():    
    path = 'output.wav'   
    sr,audio = read(path)
    vector   = extract_features(audio,sr)


    log_likelihood = np.zeros(len(models)) 
    
    for i in range(len(models)):
        gmm    = models[i]  #checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
    
    winner = np.argmax(log_likelihood)
    return speakers[winner]
print chooseAction()