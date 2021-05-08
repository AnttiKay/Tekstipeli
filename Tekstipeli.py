
#Forming connection to the database
import mysql.connector
db = mysql.connector.connect(host="localhost",
                             user="dbuser",
                             passwd="dbpass",
                             db="tekstipeli",
                             buffered=True)

#Defining the game functions

def myprint(mjono):
    if mjono != None:
        row_length = 60
        lista = mjono.split()
        kaytetty = 0
    
        for sana in lista:
            if kaytetty + len(sana) <= row_length:
                if kaytetty > 0:
                    print(" ", end="")
                    kaytetty = kaytetty + 1
                print(sana, end="")

            else:
                print("")
                kaytetty = 0
                print (sana, end="")
            kaytetty = kaytetty + len(sana)
        print("")
        
                
        

def go(direction):
    a = 0
    cur = db.cursor()
    sql = "SELECT menee, suunta, kaytettavissa FROM paasee, paikat, pelihahmo WHERE tulee = paikat.PaikkaId and paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id;"
    cur.execute(sql)
    connections = cur.fetchall()
    #print(connections)
    #print(str(connections[0][2]))
    for i in range(len(connections)):
        
        if connections[i][1] == direction:
            a = 1

            if connections[i][2] == 1:
                
                sql = "SELECT paasee.kaytettavissa, paasee.suunta FROM paasee, pelihahmo, paikat WHERE pelihahmo.Pelaaja_Id = paikat.Pelaaja_Id AND paasee.tulee = paikat.PaikkaId"
                #print(connections[i][1])
                sql = "UPDATE paikat SET paikat.Pelaaja_Id = NULL WHERE paikat.Pelaaja_Id = 1;"
                cur.execute(sql)
                sql = "UPDATE paikat SET paikat.Pelaaja_Id = 1 WHERE paikat.PaikkaId = "+ str(connections[i][0]) + ";"
                #print(sql)
                cur.execute(sql)

            else:
                sql = "SELECT paasee.faildescription FROM paasee WHERE paasee.menee = "+str(connections[i][0])+ " AND paasee.suunta = '" +connections[i][1]+ "'"
                #myprint(sql)
                cur.execute(sql)
                failure = cur.fetchall()
                if len(failure) > 0:
                    myprint(failure[0][0])
                else:
                    myprint("You can't go that way.")
                    
    if a == 0:
        myprint("You can't go that way.")

def look():
    cur = db.cursor()
    sql = "SELECT DISTINCT paikat.Name, paasee.suunta FROM paikat, paasee WHERE (paikat.PaikkaId, paasee.suunta) IN ( SELECT menee, suunta FROM paasee, paikat, pelihahmo WHERE tulee = paikat.PaikkaId and paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id);"
    cur.execute(sql)
    paikat = cur.fetchall()
    
    
    myprint("Places you see from your location: ")
    for i in range(len(paikat)):
        if paikat[i][1] == "W":
            myprint("To the West you see: "+ paikat[i][0])
        elif paikat[i][1] == "S":
            myprint("To the South you see: "+ paikat[i][0])
        elif paikat[i][1] == "E":
            myprint("To the East you see: "+ paikat[i][0])
        elif paikat[i][1] == "N":
            myprint("To the North you see: "+ paikat[i][0])
        elif paikat[i][1] == "NE":
            myprint("To the Northeast you see: "+ paikat[i][0])
        elif paikat[i][1] == "NW":
            myprint("To the Northwest you see: "+ paikat[i][0])
        elif paikat[i][1] == "SE":
            myprint("To the Southeast you see: "+ paikat[i][0])
        elif paikat[i][1] == "SW":
            myprint("To the Southwest you see: "+ paikat[i][0])
        
    print()
            

def inventory():
    cur = db.cursor()
    sql = "SELECT esinetyyppi.Nimi FROM esinetyyppi WHERE esinetyyppi.EsineTyyppiId IN( SELECT esine.EsineTId FROM esine, pelihahmo WHERE esine.Pelaaja_Id = pelihahmo.Pelaaja_Id)"
    cur.execute(sql)
    items = cur.fetchall()
    if len(items)>0:
        myprint("Items in inventory: ")
        for i in items:
            myprint("--"+ i[0])
    else:
        myprint("No items in inventory")

def examine(name):
    find = 0
    cur = db.cursor()
    sql = "SELECT esinetyyppi.Nimi FROM esinetyyppi WHERE esinetyyppi.EsineTyyppiId IN (SELECT esine.EsineTId FROM esine WHERE esine.Saatavilla = 1 AND esine.PaikkaId IN ( SELECT paikat.PaikkaId FROM paikat, pelihahmo WHERE paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id))"
    cur.execute(sql)
    exa = cur.fetchall()
    #print(exa)
    for a in exa:
        #print(a[0])
        if a[0].lower().find(name) != -1:
            find = 1
            sql = "SELECT esinetyyppi.Description FROM esinetyyppi WHERE esinetyyppi.Nimi = '"+a[0]+"'  AND esinetyyppi.EsineTyyppiId IN (SELECT esine.EsineTId FROM esine WHERE esine.PaikkaId IN ( SELECT paikat.PaikkaId FROM paikat, pelihahmo WHERE paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id))"
            cur.execute(sql)
            desc = cur.fetchall()
            if len(desc) > 0:
                myprint("You examine the "+ a[0]+ ": " )
                print()
                myprint(desc[0][0])
                print()
    if find == 0:
        myprint("I don't see any such thing")

def take(item):
    cur = db.cursor()
    sql = "SELECT esinetyyppi.Nimi FROM esinetyyppi WHERE esinetyyppi.EsineTyyppiId IN( SELECT esine.EsineTId FROM esine WHERE esine.Saatavilla = 1 AND esine.Otettavissa = 1 AND esine.PaikkaId IN ( SELECT paikat.PaikkaId FROM paikat, pelihahmo WHERE paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id ));"
    cur.execute(sql)
    takeable = cur.fetchall()
    #print(takeable)
    for a in takeable:
        if a[0].lower().find(item) != -1:
            #print("!")
            #print(a[0])
            sql = "UPDATE esine, pelihahmo, paikat SET esine.Pelaaja_Id = 1, esine.PaikkaId = NULL  WHERE esine.PaikkaId IS NOT NULL AND pelihahmo.Pelaaja_Id = paikat.Pelaaja_Id AND esine.EsineTId IN ( SELECT esinetyyppi.EsineTyyppiId FROM esinetyyppi WHERE esinetyyppi.Nimi = '"+ a[0] +"');"
            cur.execute(sql)

def use(objecti, target):
    targets = ["door1", "gates", "Phone"]
    objects = ["Room1 desk", "Security building desk", "Control box"]
    cur = db.cursor()
    sql = "SELECT esinetyyppi.Nimi FROM esinetyyppi WHERE esinetyyppi.EsineTyyppiId IN( SELECT esine.EsineTId FROM esine WHERE esine.Kaytettavissa = 1 AND esine.Saatavilla = 1 AND esine.PaikkaId IN ( SELECT paikat.PaikkaId FROM paikat, pelihahmo WHERE paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id ));"
    cur.execute(sql)
    usables = cur.fetchall()
    
    if len(objecti) >= 3 and target != None:
        for a in targets:
            if a.find(target) != -1:
                #print("target")
                sql = "SELECT esinetyyppi.Nimi FROM esinetyyppi WHERE esinetyyppi.EsinetyyppiId IN ( SELECT esinetyyppi.EsineTyyppiId FROM esinetyyppi, paasee, pelihahmo, paikat WHERE esinetyyppi.EsineTyyppiId = paasee.avain AND paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id AND paikat.PaikkaId = paasee.tulee )"
                cur.execute(sql)
                key = cur.fetchall()
                #print(key[0][0])
                sql = "SELECT esinetyyppi.Nimi FROM esinetyyppi WHERE esinetyyppi.EsineTyyppiId IN (SELECT esine.EsineTId FROM esine, pelihahmo WHERE esine.Pelaaja_Id = pelihahmo.Pelaaja_Id)"
                cur.execute(sql)
                items = cur.fetchall()
                #print(items)
                for o in items:
                    if o[0] == items[0][0]:
                        if key[0][0].lower().find(objecti) != -1:
                            sql = "SELECT esine.Item_Id FROM esine WHERE esine.EsineTId IN( SELECT DISTINCT paasee.ovi FROM paasee WHERE paasee.tulee IN( SELECT paikat.PaikkaId FROM paikat, pelihahmo WHERE paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id ));"
                            cur.execute(sql)
                            door = cur.fetchall()
                            #print(door[0][0])
                            
                            sql = "UPDATE paasee SET paasee.kaytettavissa = 1 WHERE paasee.ovi =" +str(door[0][0])+ " AND paasee.kaytettavissa = 0 AND paasee.tulee IN( SELECT paikat.PaikkaId FROM paikat, pelihahmo WHERE paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id)"
                            cur.execute(sql)
                            myprint("Doors lock slowly turns open, you use all of your power to push the door open.")
                            print()
                            update(door[0][0])
                            ## INSERT SUCCESS DESCRTIPTION HERE ##
                
    elif len(objecti) >= 3:
        #print(usables)
        #print("o1")
        for z in objects:
            for s in usables:
               # print(s[0])
                if z.find(s[0]) != -1:
                    #print("o2")
                    if z.find(objecti) != -1:
                        #print("o3")
                        sql = "SELECT esine.Item_Id FROM esine WHERE esine.EsineTId IN ( SELECT esinetyyppi.EsineTyyppiId FROM esinetyyppi	WHERE esinetyyppi.Nimi = '"+z+"')"
                        cur.execute(sql)
                        itemId = cur.fetchall()
                        #print(itemId[0][0])
                        update(itemId[0][0])
                    else:
                        myprint("I don't see any such item.")
                        

def update(itemId):
    #print("u1")
    cur = db.cursor()
    sql = "SELECT esine.EsineTId FROM esine WHERE esine.Kaytettavissa = 1 AND esine.Item_Id = "+ str(itemId)
    cur.execute(sql)
    tId = cur.fetchall()
    #print(itemId)
    #print(tId[0][0])

    if tId[0][0] == 1 and itemId == 4:
        cur.execute("UPDATE esine SET esine.Saatavilla = 1 WHERE esine.Item_Id < 3")
        cur.execute("SELECT esine.EsineTId FROM esine WHERE esine.PaikkaId = 1 AND esine.Saatavilla = 1 AND esine.Otettavissa = 1")
        items = cur.fetchall()
        #print (items)
        if len(items) > 0:
            myprint("Inside you find: ")
            myprint("- Keys")
            myprint("- Tickets")
            print()
        else:
            myprint("Inside you find nothing.")
            print()
            
    elif tId[0][0] == 9 and itemId == 6:
        sql = "UPDATE paikat SET paikat.Description = 'The room is quite small. The light is dim and flickers slightly. The walls look like they were white in some earlier life, but look yellowish now and the floor is worn linoleum. There is only a DESK with drawers in the room and un ugly PAINTING of three clowns hanging on the wall opposite the door. All in all, the room couldn’t be less like the cheerful and bright amusement park outside.' WHERE paikat.PaikkaId = 1"
        cur.execute(sql)
    

def placeDesc():
    cur = db.cursor()
    sql = "SELECT paikat.Name, paikat.Description FROM paikat, pelihahmo WHERE pelihahmo.Pelaaja_Id = paikat.Pelaaja_Id"
    cur.execute(sql)
    desc = cur.fetchall()
    myprint(desc[0][0])
    print()
    myprint(desc[0][1])
    
    
    


#Main Game loop
cmd = 1
commands = ["n", "s", "w", "e", "nw", "ne", "sw", "se", "take", "look", "use", "examine"]

while cmd != "exit":
    
    placeDesc()

    cmd = input(">> ").lower().split()
    
    if   cmd[0] in ["n", "north"]:
        go("N")
        
    elif cmd[0] in ["s", "south"]:
        go("S")
        
    elif cmd[0] in ["e", "east"]:
        go("E")
        
    elif cmd[0] in ["w", "west"]:
        go("W")

    elif cmd[0] in ["nw", "northwest"]:
        go("NW")

    elif cmd[0] in ["ne", "norhteast"]:
        go("NE")

    elif cmd[0] in ["sw", "southwest"]:
        go("SW")

    elif cmd[0] in ["se", "southeast"]:
        go("SE")

    elif cmd[0] in ["take"]:
        if len(cmd) >= 2:
            take(cmd[1])
        else:
            myprint("What are you taking?")

    elif cmd[0] in ["look", "l"]:
        look()

    elif cmd[0] in ["inventory", "i"]:
        inventory()

    elif cmd[0] in ["use", "open"]:
        if len(cmd) >= 3:
            use(cmd[1], cmd[2])
        elif len(cmd) >= 2:
            use(cmd[1], None)
        else:
            myprint("What do you wish to use and on what?")
            

    elif cmd[0] in ["examine", "exa"]:
        if len(cmd) >= 2:
            examine(cmd[1])
        else:
            myprint("What are you examining?")    

db.close()

















