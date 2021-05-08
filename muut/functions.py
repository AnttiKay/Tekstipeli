#!/usr/bin/env python

import mysql.connector

DB_NAME = "tekstipeli"
DB_USER = "dbuser"
DB_HOST = "127.0.0.1"
DB_PASSWORD = "dbpass"

db = mysql.connector.connect(host=DB_HOST,
                             user=DB_USER,
                             passwd=DB_PASSWORD,
                             db=DB_NAME,
                             buffered=True)

patrol_index = 0

def get_room_desc():
    cur = db.cursor()
    sql = "SELECT paikat.Name, paikat.Description FROM paikat, pelihahmo WHERE pelihahmo.Pelaaja_Id = paikat.Pelaaja_Id"
    cur.execute(sql)
    desc = cur.fetchall()
    print(desc[0][0])
    print(desc[0][1])

def guard_patrol():
    global patrol_index
    patrol = [8, 9, 3, 2, 7, 14, 13, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8]
    #print("patrol" + str(patrol_index) + " : " + str(patrol[patrol_index]))
    if patrol_index >= len(patrol)-1:
        patrol_index = 0
    else:
        patrol_index += 1
    cur = db.cursor()
    sql = "UPDATE paikat SET paikat.GuardId = NULL WHERE paikat.GuardId = 2;"
    #print(sql)
    cur.execute(sql)
    sql = "UPDATE paikat SET paikat.GuardId = 2 WHERE paikat.PaikkaId = "+ str(patrol[patrol_index]) + ";"
    #print(sql)
    cur.execute(sql)
    # ??????
    #db.commit()


def move_player(direction):
    #TODO return error if can't move to a direction
    cur = db.cursor()
    sql = "SELECT menee, suunta FROM paasee, paikat, pelihahmo WHERE tulee = paikat.PaikkaId and paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id;"
    cur.execute(sql)
    connections = cur.fetchall()
    #print(connections)
    for i in range(len(connections)):
        if connections[i][1] == direction:
            #print(connections[i][1])
            sql = "UPDATE paikat SET paikat.Pelaaja_Id = NULL WHERE paikat.Pelaaja_Id = 1;"
            cur.execute(sql)
            sql = "UPDATE paikat SET paikat.Pelaaja_Id = 1 WHERE paikat.PaikkaId = "+ str(connections[i][0]) + ";"
            #print(sql)
            cur.execute(sql)
            return

def examine_item(name):
    cur = db.cursor()
    sql = "SELECT esinetyyppi.Description FROM esinetyyppi, esine, pelihahmo, paikat WHERE esine.PaikkaId = paikat.PaikkaId AND paikat.Pelaaja_Id = pelihahmo.Pelaaja_Id AND esine.EsineTId = esinetyyppi.EsineTyyppiId AND esinetyyppi.Nimi = '"+ name + "'" 
    #print(sql)
    cur.execute(sql)
    desc = cur.fetchall()
    if len(desc) > 0:
        myprint("You examine the "+ name)
        myprint(desc[0][0])
    else:
        myprint("I don't see any such thing")
