import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import Runner as rn
def analyse(data,choice):
    
    q1=data.set_index(["AppName","EXEDATE"])
    q1=q1.sort_index()
    print()
    print()
    print("Plotting and Saving Trend Lines for "+str(choice)+ " app, Please Wait!!!")
    plt.figure(figsize=(50,15))
    sns.set()
        
    plt.plot(q1.loc[(choice,),"STATUS"],color="black")
    plt.xticks(rotation=90)
    plt.savefig('report/'+choice+'_trendline.pdf')
    
        
    print()
    print()
    print("All files saved!.... Proceeding with further analysis")

    """Second Analysis"""
    q2=data[data.AppName==choice].loc[:,:]

    fail=q2.STATUS=="Fail"
    plt.figure(figsize=(10,10))
    sns.set_palette("pastel")
    sns.countplot("ENV|CODE|DATA|REQ",data=q2,palette="RdBu")
    plt.xticks(rotation=90)
    plt.savefig('report/error_occurence.pdf')
    """textual feed Back"""
    print()
    print()
    print("Top five error occurences are")
    print()
    print()

    print("++++++++++++++++++++++++++++++++++++++")
    print()

    
    print(q2['ENV|CODE|DATA|REQ'].value_counts().head(5))
    print()
    print("++++++++++++++++++++++++++++++++++++++")
    """Thrid Analysis"""
    #q3=data[data.AppName==choice]

    #plt.figure(figsize=(10,10))
    #sns.catplot(y='ENV|CODE|DATA|REQ',data=q3,kind='count',row='AppName',height=8.27, aspect=11.7/8.27,palette="GnBu")
    #plt.xticks(rotation=90)
    #plt.savefig('report/Appwise_error.pdf')
    #rn.runner(data,"2.2")
    print("App analysis done")
