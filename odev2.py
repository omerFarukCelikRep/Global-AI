cv1 = {"FirstName":"Ömer Faruk", "LastName":"Çelik", "Age":26,"Abilities":["C#","JavaScript","HTML"]};
cv2 = {"FirstName":"Ali", "LastName":"Veli", "Age":22,"Likes":["Books","Movies","Tv-Series"]};
cv3 = {"FirstName":"Zeki", "LastName":"Çalışkan", "Age":32,"Abilities":["PPAP","APQP"]};
cv4 = {"FirstName":"Ahmet", "LastName":"Paşazade", "Age":18,"Likes":["Motorsports","Games"]};
cv5 = {"FirstName":"Osman", "LastName":"Hatırsormaz", "Age":21,"Abilities":[]};

cvList = [];
cvList.append(cv1);
cvList.append(cv2);
cvList.append(cv3);
cvList.append(cv4);
cvList.append(cv5);


for i in range(0,len(cvList)):
    for k,v in cvList[i].items():
        print(f"{k} : {v}");