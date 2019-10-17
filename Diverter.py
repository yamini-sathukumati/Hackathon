import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import AllAnalyser as aan
import Analyser as an
def diverter (data,choice):
    q1=data
    if(choice=="all"):
        aan.analyse(data)
        
    else:
        an.analyse(data,choice)
       

    print(" Analyser ki vachindi")
    

