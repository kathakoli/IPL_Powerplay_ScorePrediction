


def predictRuns(testInput):
    prediction = 0

    import tensorflow as tf
    import pandas as pd


    


    model = tf.keras.models.load_model("model.h5",compile=False)


    


    df2=pd.read_csv(testInput)
    ven=df2.iloc[:,0].values
    inn=df2.iloc[:,1].values
    bat_team=df2.iloc[:,2].values
    bowl_team=df2.iloc[:,3].values
    bat=df2.iloc[:,4].values
    bowl=df2.iloc[:,5].values


    


    
    c=0
    for i in bat[0]:
        if i==',':
            c+=1
            


    


    
    d=0
    for i in bowl[0]:
        if i==',':
            d+=1
            


    


    no_of_bowlers=float(d+1)
    no_of_wickets=float(c-1)
    innings=float(inn[0])
    if bat_team == "Kolkata Knight Riders":
        bat_no=6
    elif bat_team == "Royal Challengers Bangalore":
        bat_no=0
    elif bat_team == "Chennai Super Kings":
        bat_no=1
    elif bat_team == "Punjab Kings":
        bat_no=9
    elif bat_team == "Rajasthan Royals":
        bat_no=10
    elif bat_team == "Delhi Capitals":
        bat_no=2
    elif bat_team == "Sunrisers Hyderabad":
        bat_no=4
    elif bat_team == "Mumbai Indians":
        bat_no=7
    else:
        bat_no=5






    


    if bowl_team == "Kolkata Knight Riders":
        bowl_no=6
    elif bowl_team == "Royal Challengers Bangalore":
        bowl_no=0
    elif bowl_team == "Chennai Super Kings":
        bowl_no=1
    elif bowl_team == "Punjab Kings":
        bowl_no=9
    elif bowl_team == "Rajasthan Royals":
        bowl_no=10
    elif bowl_team == "Delhi Capitals":
        bowl_no=2
    elif bowl_team == "Sunrisers Hyderabad":
        bowl_no=4
    elif bowl_team == "Mumbai Indians":
        bowl_no=7
    else:
        bowl_no=5


    

    if ven == "Ahmedabad" or ven=="Narendra Modi Stadium":
        ven_no=26
    elif ven == "Mumbai" or ven=="Wankhede Stadium":
        ven_no=5
    elif ven == "Kolkata" or ven=="Eden Gardens":
        ven_no=4
    elif ven == "Chennai" or ven=="MA Chidambaram Stadium, Chepauk" or ven=="MA Chidambaram Stadium, Chepauk , Chennai" or ven=="MA Chidambaram Stadium":
        ven_no=8
    elif ven == "Delhi" or ven=="Feroz Shah Kotla" or ven=="Arun Jaitley Stadium":
        ven_no=3
    else:
        ven_no=1


    


    b=[]
    for i in range(0,11):
        if i==(bat_no):
            b.append(1)
        else:
            b.append(0)
        


    


    b1=[]
    for i in range(0,11):
        if i==(bowl_no):
            b1.append(1)
        else:
            b1.append(0)


    


    v=[]
    for i in range(1,27):
        if i==(ven_no):
            v.append(1)
        else:
            v.append(0)
        


    


    arr=[]
    arr.append(innings)


    


    arr.append(5.6)
    for i in v:
        arr.append(i)


    


    for i in b:
        arr.append(i)


    


    for i in b1:
        arr.append(i)


    



    arr.append(no_of_wickets)


    


    arr.append(no_of_bowlers)
        

    
      
    prediction=int(model.predict([arr]))
    

    if (prediction>=0 and prediction<10):
        prediction+=30
    elif (prediction>=10 and prediction<20):
        prediction+=20
    elif (prediction>=20 and prediction<25):
        prediction+=15
    elif (prediction>=25 and prediction<=27):
        prediction+=10
    elif (prediction>27 and prediction<=30):
        prediction+=8
    elif (prediction>30 and prediction<=32):
        prediction+=4
    else:
        prediction=prediction
  
  
    return prediction







