import os
import json

JSONFILE = ("json_data.json")

def read(): 
    if os.path.exists(JSONFILE): 
        f = open(JSONFILE,'r') 
        try:
            tmp = json.loads(f.read()) 
        except:
            tmp = list() 
        f.close()
        return tmp
    else:      
        return list() 

def store(newData):
    dbfile = read()
    dbfile.append(newData.__dict__) 
    f = open(JSONFILE,'w')
    f.write(json.dumps(dbfile))
    f.close()