 DROP DATABASE tekstipeli;
CREATE DATABASE tekstipeli;
USE tekstipeli;

CREATE TABLE HidingSpot
(
  Spot_Id INT NOT NULL,
  Description VARCHAR(60) NOT NULL,
  Onko INT NOT NULL,
  PRIMARY KEY (Spot_Id)
);

CREATE TABLE Pelihahmo
(
  Pelaaja_Id INT NOT NULL,
  PRIMARY KEY (Pelaaja_Id)
);

CREATE TABLE Esinetyyppi
(
  Nimi VARCHAR(60) NOT NULL,
  EsineTyyppiId INT NOT NULL AUTO_INCREMENT,
  Description TEXT NOT NULL,
  PRIMARY KEY (EsineTyyppiId)
);

CREATE TABLE Paikat
(
  Name VARCHAR(60) NOT NULL,
  Description TEXT NOT NULL,
  PaikkaId INT NOT NULL AUTO_INCREMENT,
  Spot_Id INT,
  Pelaaja_Id INT,
  PRIMARY KEY (PaikkaId),
  FOREIGN KEY (Spot_Id) REFERENCES HidingSpot(Spot_Id),
  FOREIGN KEY (Pelaaja_Id) REFERENCES Pelihahmo(Pelaaja_Id)
);

CREATE TABLE Guard
(
  GuardId INT NOT NULL AUTO_INCREMENT,
  PaikkaId INT,
  PRIMARY KEY (GuardId),
  FOREIGN KEY (PaikkaId) REFERENCES paikat(PaikkaId)
);

CREATE TABLE Esine
(
  Item_Id INT NOT NULL AUTO_INCREMENT,
  EsineTId INT NOT NULL,
  Saatavilla INT NOT NULL,
  Kaytettavissa INT NOT NULL,
  PaikkaId INT,
  Pelaaja_Id INT DEFAULT NULL,
  Otettavissa INT DEFAULT 1,
  Kaytetty INT DEFAULT 0,
  PRIMARY KEY (Item_Id),
  FOREIGN KEY (EsineTId) REFERENCES esinetyyppi(EsineTyyppiId),
  FOREIGN KEY (PaikkaId) REFERENCES Paikat(PaikkaId),
  FOREIGN KEY (Pelaaja_Id) REFERENCES Pelihahmo(Pelaaja_Id)
);

CREATE TABLE Paasee
(
  tulee INT NOT NULL,
  menee INT NOT NULL,
  suunta VARCHAR(30) NOT NULL,
  kaytettavissa INT NOT NULL,
  avain INT,
  ovi INT,
  faildescription TEXT,
  description TEXT,
  PRIMARY KEY (tulee, menee),
  FOREIGN KEY (avain) REFERENCES esinetyyppi(EsineTyyppiId),
  FOREIGN KEY (tulee) REFERENCES Paikat(PaikkaId),
  FOREIGN KEY (menee) REFERENCES Paikat(PaikkaId),
  FOREIGN KEY (ovi) REFERENCES esinetyyppi(EsineTyyppiId)
);

#INSERTING PLAYER INTO DATABASE.

INSERT INTO pelihahmo VALUES (1);

# INSERT INTO esinetyyppi VALUES ('', NULL, '');
# INSERTING ITEM TYPES & DESCRIPTIONS INTO THE DATABASE.

INSERT INTO esinetyyppi VALUES ('Room1 desk', NULL, 'The desk is painted white, or used to be, it’s as worn as the rest of the room. There is one drawer that doesn’t appear to be locked.');
INSERT INTO esinetyyppi VALUES ('Money', NULL, '');
INSERT INTO esinetyyppi VALUES ('Crowbar', NULL, 'Somewhat bent crowbar, I should be able to break open something with this.');
INSERT INTO esinetyyppi VALUES ('Gate keys', NULL, 'Keys from the security building office.');
INSERT INTO esinetyyppi VALUES ('Keys for room1', NULL, 'Rusty discarded keys, I wonder where these fit to?');
INSERT INTO esinetyyppi VALUES ('Rock', NULL, 'An ordinary looking rock, I can’t imagine why would you collect these.');
INSERT INTO esinetyyppi VALUES ('Tickets', NULL, 'Collect all of these to gain more points upon finishing the game.');
INSERT INTO esinetyyppi VALUES ('Flashlight', NULL, '');
INSERT INTO esinetyyppi VALUES ('Door1', NULL, '');
INSERT INTO esinetyyppi VALUES ('Main switch', NULL, '');
INSERT INTO esinetyyppi VALUES ('Ugly painting', NULL, 'Why would anyone want to hang that on their wall?');
INSERT INTO esinetyyppi VALUES ('Security door', NULL, '');
INSERT INTO esinetyyppi VALUES ('Kitchen door', NULL, 'The DOOR leads to kitchen, nothing very interesting there.');
INSERT INTO esinetyyppi VALUES ('Security building desk', NULL, 'there are papers, work schedules, brochures, some old looking candies and a KEY');
INSERT INTO esinetyyppi VALUES ('Security building bookshelf', NULL, 'BOOKSHELF seems to have some books and magazines and also a FLASHLIGHT');
INSERT INTO esinetyyppi VALUES ('Phone', NULL, 'The PHONE next to the map is the sort of old fashioned devices you have never used before the- phone? - receiver? – handheld part, anyway is attached to big boxy thing at the wall by a cord. The big boxy wall part also has a coin slot.');
INSERT INTO esinetyyppi VALUES ('Control box', NULL, 'There are lots of buttons here and you have no idea what they do.');



# INSERTING PLACES & DESCRIPTIONS INTO DATABASE

# INSERT INTO paikat VALUES ('', '', NULL, NULL, NULL, NULL);

INSERT INTO paikat VALUES ('ROOM1', 'The room is quite small. The light is dim and flickers slightly. The walls look like they were white in some earlier life, but look yellowish now and the floor is worn linoleum. There is only a DESK with drawers in the room and un ugly PAINTING of three clowns hanging on the wall opposite the door. All in all, the room couldn’t be less like the cheerful and bright amusement park outside.
The door is locked.', NULL, NULL, 1);
INSERT INTO paikat VALUES ('INFO1', 'There is a large map of the park. You can see from the map that you are near to the north end of the park. There doesn’t appear to be any way out here. The main gates are in the south end and if there is another way out you can’t see it in the map. There is another Info-point nearer to the gates and it seems there is a payphone there. The food court is right south of you.', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('HAUNTED HOUSE', 'You had wanted to visit the haunted house and were disappointed to learn that it was closed for renovations and wouldn’t open for two months. It doesn’t really look like much of a haunted house right now, just an unfinished building. There’ some TICKETS lying on the ground but nothing else useful here.', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('BACK OF HAUNTED HOUSE', 'Behind the haunted house, you can see the things left by the workers for the night.
', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('Power switch', 'The building in front of you appears to be some sort of utility building. One of the windows is slightly open.
It’s quite dark. The light from the streetlights only barely reaches inside. You can just see the text above one of the many switches in the room that says MAIN SWITCH.'
, NULL, NULL, NULL);
INSERT INTO paikat VALUES ('FOOD COURT', 'The food court is completely empty, but the smell of greasy fast food still lingers in the air. This place was full of people, and noise, and sea gulls during the day.
The (INSERT NAME OF THE RESTAURANT HERE), you ate here with your family today. Looking through the window you can see that somebody forgot the tip jar on the counter and there’s still MONEY there.
', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('AQUARIUM', 'You never realized how creepy it feels to have fish staring at you. Or how creepy the aquarium really is. You are surrounded by tonnes of water held back by layer of thin glass. All it takes is a small crack…
The echo of your footsteps isn’t quite enough to fill the silence and you can hear your heart beating in your chest.
', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('SECURITY BUILDING', 'Another utility building. This one says SECURITY in small plaque next to the door. Probably the staff building from the map. For some reason the DOOR is ajar.
The room is dark, but you don’t dare to try the lights. You can see that there is DESK and a BOOKSHELF and another DOOR.
', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('CAROUSEL', 'The shape of the carousel rises dark in front of you. In the daylight and surrounded by people, light, and music the carrousel had appeared inviting. You had ridden the carousel with your sister. Now in the dark and quiet the exaggerated grins on the faces of the rides appear grotesque and you are quite certain that your sister wouldn’t like those horses one bit. All those shadows look like they would make good hiding place, but the longer you stay here the more you just want to run.', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('WATER SLIDES', 'The waterslides are separated from the rest of the park with a chain-link fence. Your parents hadn’t packed swimsuits for the trip so you didn’t get a chance to visit the slides. There are some tickets next to your foot.
', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('BUMPER CARS', 'You never really liked the Bumper cars. When you had been younger, your brother had picked on you by constantly bumping on you so you couldn’t move whenever you had wanted to try the Bumper cars.
The voices are getting closer.
', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('HALL OF MIRRORS', 'The hall of mirrors is ahead of you. There are no doors here, but going in would be a bad idea.', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('ROLLER COASTER', 'There is the rollercoaster ticket booth ahead of you.
The door is locked and bumping into it made loud enough sound to almost have you panic.', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('INFO 2', 'Yes! The second Info-point! Wait. There’s somebody there.', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('GATES', 'The gates! Finally, you are getting out of here! Except the closer you get to the gate the clearer it becomes that it’s not going to be that easy. The gates are closed, locked with heavy looking chains and way too high to climb.', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('Outside', 'You have finally escaped the amusement park.', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('BOOTH', 'Inside the booth, it is completely dark. Your hand accidentally hits the light switch', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('CAR', 'Hiding in a Bumper car was about as comfortable as it sounded, not much space there. Hey, wait a minute, were those tickets on the floor?', NULL, NULL, NULL);
INSERT INTO paikat VALUES ('INSIDE THE HALL OF MIRRORS', 'Everywhere you look you can see yourself, you’re not sure where to go and can’t see the entrance anymore. (there’s no way out here. game over)', NULL, NULL, NULL);

#INSERTING CONNECTIONS BETWEEN THE PLACES

INSERT INTO paasee VALUES (1, 2, "S", 0, 5, 9, "The door is locked.", "You have the wrong key.");
INSERT INTO paasee VALUES (1, 3, "W", 0, 5, 9, "The door is locked.", "You have the wrong key.");

INSERT INTO paasee VALUES (2, 1, "N", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (2, 3, "NW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (2, 6, "S", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (2, 7, "SE", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (2, 11, "SW", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (3, 1, "E", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (3, 2, "SE", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (3, 5, "W", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (3, 9, "S", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (4, 5, "SW", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (5, 3, "E", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (5, 4, "NE", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (6, 2, "N", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (6, 7, "E", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (6, 9, "NW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (6, 10, "SW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (6, 11, "W", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (6, 13, "S", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (6, 14, "SE", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (7, 2, "NW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (7, 6, "W", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (7, 12, "E", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (7, 13, "SW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (7, 14, "S", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (8, 9, "NE", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (8, 10, "E", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (8, 11, "SE", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (9, 3, "N", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (9, 6, "SE", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (9, 8, "SW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (9, 11, "S", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (10, 6, "NE", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (10, 8, "NW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (10, 11, "N", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (10, 13, "E", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (10, 15, "SE", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (11, 2, "NE", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (11, 6, "E", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (11, 8, "W", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (11, 9, "N", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (11, 10, "S", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (11, 13, "SE", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (12, 7, "W", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (12, 14, "SW", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (13, 6, "N", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (13, 7, "NE", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (13, 10, "W", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (13, 11, "NW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (13, 14, "E", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (13, 15, "S", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (14, 6, "NW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (14, 7, "N", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (14, 12, "NE", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (14, 13, "W", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (14, 15, "SW", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (15, 10, "NW", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (15, 13, "N", 1, NULL, NULL, NULL, NULL);
INSERT INTO paasee VALUES (15, 14, "NE", 1, NULL, NULL, NULL, NULL);

INSERT INTO paasee VALUES (15, 16, "S", 0, 4, NULL, NULL, NULL);


# INSERTING GUARDS INTO THE DATABASE.

INSERT INTO guard VALUES (1, 14);

#INSERT INTO guard VALUES (NULL);

# Inserting items into database
# INSERT INTO esine VALUES (NULL, TId, saatavilla, kaytettavissa, paikkaID, pelaajaId, otettavissa, kaytetty)
# INSERT INTO esine VALUES (NULL, , , , , NULL, , );

INSERT INTO esine VALUES (NULL, 5, 0, 0, 1, NULL, 1, 0);
INSERT INTO esine VALUES (NULL, 7, 0, 0, 1, NULL, 1, 0);
INSERT INTO esine VALUES (NULL, 11, 1, 0, 1, NULL, 0, 0);
INSERT INTO esine VALUES (NULL, 1, 1, 1, 1, NULL, 0, 0);
INSERT INTO esine VALUES (NULL, 10, 1, 1, 5, NULL, 0,0);
INSERT INTO esine VALUES (NULL, 9, 1, 1, 1, NULL, 0, 0);
INSERT INTO esine VALUES (NULL, 14, 1, 1, 8, NULL, 0, 0);
INSERT INTO esine VALUES (NULL, 15, 1, 0, 8, NULL, 0, 0);
INSERT INTO esine VALUES (NULL, 12, 1, 0, 8, NULL, 0, 0);
INSERT INTO esine VALUES (NULL, 17, 1, 1, 17, NULL, 0, 0);

