import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def runner(data,version):
    print("Running the app using the version number = "+str(version))
    print()
    print("these apps still failed even after the version upgradtaion")
    print(data[data.STATUS=="Fail"])
    
