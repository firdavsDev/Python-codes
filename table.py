from prettytable import PrettyTable

#qatorning nomlarini yoazamiz
mytable=PrettyTable(["Student ismi",'Yoshi',"Bali"])

#ustun qushamiz
mytable.add_row(['Davron','19','5'])
mytable.add_row(['Firdavs','22','5'])
mytable.add_row(['Davlat','33','5'])

print(mytable)