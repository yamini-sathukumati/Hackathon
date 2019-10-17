import Diverter as di
def ChoiceMaker(data):
    print()
    print()
    
    
    Choice=input("Which report  you want to generate? (enter choice All/Single)")
    if(Choice=="All" or Choice=="all"):
        di.diverter(data,"all")
    else:
        print("These are the apps in the data:")
        print(list(data["AppName"].unique()))
        AppChoice=input("Which App you want to analyse")
        
        di.diverter(data,AppChoice)
        
    
