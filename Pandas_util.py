import pandas as pd
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


pseries = pd.Series(thisdict)
#df = pd.DataFrame(data= thisdict)
print(pseries)

def change(data):
    return data.astype(str)

print(type(change(pseries)[2]))
pseries = pseries.append(pd.Series({"broken":"yes"}))
print(pseries)