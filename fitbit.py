import requests

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
warnings.filterwarnings("ignore")

access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1MzM0giLCJzdWIiOiJCWlk4NUIiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJlY2cgcnNldCByb3h5IHJwcm8gcm51dCByc2xlIHJjZiByYWN0IHJyZXMgcmxvYyByd2VpIHJociBydGVtIiwiZXhwIjoxNzQ0ODEwMDY2LCJpYXQiOjE3MTMyNzQwNjZ9.CaQwg7LEjcu2yLr_ClxtzDpcQ-QFfRZ0-eMt-1E5TRg"

header = {'Authorization' : 'Bearer {}'.format(access_token)}
response = requests.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()

print(response['user'])

for k,v in response['user'].items():
    print(k)
    print(v)
    print("\n")