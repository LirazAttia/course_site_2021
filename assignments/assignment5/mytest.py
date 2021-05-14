
#imports
import pandas as pd
import json

# Opening JSON file
f = open('data.json')
data = json.load(f)
data = pd.DataFrame(data)
print(data)
f.close()