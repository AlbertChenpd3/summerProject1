--Creates the databases used to store rooms and within those rooms the status of each computer
DROP TABLE IF EXISTS roomList;
DROP TABLE IF EXISTS individualRooms;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);


CREATE TABLE roomList(
    roomName varchar(255) PRIMARY KEY, --ensures unique names
    roomHash INTEGER  AUTOINCREMENT --linked to each hash, should generate a unique one for each room

);

CREATE TABLE individualRooms(
    currentRoomHash INTEGER PRIMARY KEY --should link to roomList room Hash, also should be the row not the column 
    --need to store multiple values here somehow
    FOREIGN KEY (currentRoomHash) REFERENCES roomList(roomHash)
    --Placeholder we're just going to store 30 computers
    computer1 BOOLEAN
    computer2 BOOLEAN
    computer3 BOOLEAN
    computer4 BOOLEAN
    computer5 BOOLEAN
);
