--Creates the databases used to store rooms and within those rooms the status of each computer
DROP TABLE IF EXISTS roomList;
DROP TABLE IF EXISTS individualRooms;

CREATE TABLE roomList(
    roomName varchar(255) PRIMARY KEY, --ensures unique names
    roomHash INTEGER PRIMARY KEY AUTOINCREMENT --linked to each hash, should generate a unique one for each room

);

CREATE TABLE individualRooms(
    roomHash INTEGER PRIMARY KEY --should link to roomList room Hash, also should be the row not the column
    --need to store multiple values here somehow
);
