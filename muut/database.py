#!/usr/bin/env python

import mysql.connector

import myprint
print = myprint.myprint

DB_NAME = "tekstipeli"
DB_USER = "dbuser"
DB_HOST = "127.0.0.1"
DB_PASSWORD = "dbpass"

db = mysql.connector.connect(host=DB_HOST,
                             user=DB_USER,
                             passwd=DB_PASSWORD,
                             db=DB_NAME,
                             buffered=True)

cur = db.cursor()

def init():
    file = open("db.sql", 'r')
    sql = " ".join(file.readlines())
    for result in cur.execute(sql, multi=True):
        pass
    commit()

def commit():
    db.commit()

def close():
    db.close()

def get_room_desc():
    sql = "SELECT paikat.Name, paikat.Description FROM paikat, pelihahmo WHERE pelihahmo.Pelaaja_Id = paikat.Pelaaja_Id"
    cur.execute(sql)
    desc = cur.fetchall()
    print(desc[0][0] + "\n")
    print(desc[0][1])

def get_player_location():
    sql = "SELECT paikat.PaikkaId FROM paikat WHERE paikat.Pelaaja_Id = 1;"
    cur.execute(sql)
    location = cur.fetchall()
    return location[0][0]

def get_guard_location(guard_id):
    sql = "SELECT guard.PaikkaId FROM guard WHERE guard.GuardId = " + str(guard_id) + ";"
    cur.execute(sql)
    location = cur.fetchall()
    #print(location[0][0])#debug
    return location[0][0]

def guard_patrol():
    guard_id = 2
    patrol = [8, 9, 3, 2, 7, 14, 13, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    sql = "SELECT guard.PatrolIndex FROM guard WHERE guard.GuardId = " + str(guard_id) + ";"
    cur.execute(sql)
    patrol_index = cur.fetchall()[0][0]
    #print(patrol_index)#debug
    if patrol_index >= len(patrol)-1:
        patrol_index = 0
    else:
        patrol_index += 1
    sql = "UPDATE guard SET guard.PatrolIndex = " + str(patrol_index) + " WHERE guard.GuardId = " + str(guard_id) + ";"
    cur.execute(sql)
    sql = "UPDATE guard SET guard.PaikkaId = " + str(patrol[patrol_index]) + " WHERE guard.GuardId = " + str(guard_id) + ";"
    cur.execute(sql)

def move_player(direction):
    sql = "SELECT menee, suunta, kaytettavissa FROM paasee, paikat, pelihahmo WHERE tulee = paikat.PaikkaId and paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id;"
    cur.execute(sql)
    connections = cur.fetchall()
    for i in range(len(connections)):
        if connections[i][1] == direction and connections[i][2] == 1:
            sql = "UPDATE paikat SET paikat.Pelaaja_Id = NULL WHERE paikat.Pelaaja_Id = 1;"
            cur.execute(sql)
            sql = "UPDATE paikat SET paikat.Pelaaja_Id = 1 WHERE paikat.PaikkaId = "+ str(connections[i][0]) + ";"
            cur.execute(sql)
            r = [True, ""]
            break
        elif connections[i][1] == direction and connections[i][2] == 0:
            sql = "SELECT paasee.faildescription FROM paasee WHERE paasee.menee = "+str(connections[i][0])+ " AND paasee.suunta = '" +connections[i][1]+ "'"
            cur.execute(sql)
            failure = cur.fetchall()
            r = ["locked", failure[0][0]]
            break
    else:
        r = [False, ""]
    return r

def look():
    sql = "SELECT DISTINCT paikat.Name, paasee.suunta FROM paikat, paasee WHERE (paikat.PaikkaId, paasee.suunta) IN ( SELECT menee, suunta FROM paasee, paikat, pelihahmo WHERE tulee = paikat.PaikkaId and paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id);"
    cur.execute(sql)
    paikat = cur.fetchall()
    print("Places you see from your location: ")
    for i in range(len(paikat)):
        if paikat[i][1] == "W":
            print("To the West you see: "+ paikat[i][0])
        elif paikat[i][1] == "S":
            print("To the South you see: "+ paikat[i][0])
        elif paikat[i][1] == "E":
            print("To the East you see: "+ paikat[i][0])
        elif paikat[i][1] == "N":
            print("To the North you see: "+ paikat[i][0])
        elif paikat[i][1] == "NE":
            print("To the Northeast you see: "+ paikat[i][0])
        elif paikat[i][1] == "NW":
            print("To the Northwest you see: "+ paikat[i][0])
        elif paikat[i][1] == "SE":
            print("To the Southeast you see: "+ paikat[i][0])
        elif paikat[i][1] == "SW":
            print("To the Southwest you see: "+ paikat[i][0])
        

def get_item_desc(name):
    sql = "SELECT esinetyyppi.Description FROM esinetyyppi, esine, pelihahmo, paikat WHERE esine.PaikkaId = paikat.PaikkaId AND paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id AND esine.EsineTId = esinetyyppi.EsineTyyppiId AND esinetyyppi.Nimi = '"+ name + "'" 
    cur.execute(sql)
    desc = cur.fetchall()
    if len(desc) > 0:
        print("You examine the " + name + ".\n")
        print(desc[0][0])
    else:
        print("I don't see any such thing")

def inventory():
    sql = "SELECT esinetyyppi.Nimi FROM esinetyyppi, pelihahmo, esine WHERE esinetyyppi.EsineTyyppiId = esine.EsineTId AND esine.Pelaaja_Id = pelihahmo.Pelaaja_Id"
    cur.execute(sql)
    items = cur.fetchall()
    if len(items)>0:
        print("Items in inventory: ")
        for i in items:
            print("--"+ i[0])
    else:
        print("No items in inventory")
    print("")

def take(item):
    sql = "UPDATE esine, pelihahmo, paikat SET esine.Pelaaja_Id = 1, esine.Saatavilla = 0 WHERE pelihahmo.Pelaaja_Id = paikat.Pelaaja_Id AND esine.EsineTId IN ( SELECT esinetyyppi.EsineTyyppiId FROM esinetyyppi WHERE esinetyyppi.Nimi = '"+ item +"');"
    cur.execute(sql)

