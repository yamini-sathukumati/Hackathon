import sys
import pandas as pd
import Choice as ch
name=sys.argv[1]
data=pd.read_csv(name)

ch.ChoiceMaker(data)
