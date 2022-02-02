# SAVE A DICTIONARY INTO A PICKLE FILE.
import pickle
import numpy  as np
import pandas as pd
import os
import json

 #FILENAME
filename='tmp'     

#READ AND WRITE DICTIONARY AS PICKLE FILE 
print("\n-----DICTIONARY OBJECT TO PICKLE-----")
x1 = { "lion": "yellow", "kitty": "red", "list": [1,2,3,4] }
pickle.dump( x1, open( filename, "wb" ) )
x2 = pickle.load( open(filename, "rb" ) )
print(x2,type(x2))

#READ AND WRITE DICTIONARY AS JSON FILE 
print("\n-----DICTIONARY TO JSON I/O-----")
with open(filename, 'w') as outfile:
    # json.dump(x1, outfile)                             #CONDENSED FORM
    json.dump(x1, outfile, indent=4, sort_keys=True)    #EXPANDED FORM

f = open(filename)    
x2 = json.load(f)
print(x2,type(x2))

#READ AND WRITE NUMPY ARRAY AS PICKLE FILE 
print("\n-----NUMPY ARRARYS TO PICKLE-----")
x1=np.array([1.0,0.1,2.0])
pickle.dump( x1, open(  filename, "wb" ) )
x2 = pickle.load( open( filename, "rb" ) )
print(x2,type(x2))

#READ AND WRITE PANDA DATAFRAME ARRAY AS PICKLE FILE 
print("\n-----PANDAS DATAFRAME-----")
#https://pandas.pydata.org/docs/user_guide/10min.html
x1 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
pickle.dump( x1, open(  filename, "wb" ) )
x2 = pickle.load( open( filename, "rb" ) )
print(x2,type(x2))

#REMOVE FILES (START FRESH NEXT TIME)
os.remove(filename)