import pandas as pd
import sqlite3

con = sqlite3.connect("data/Chinook_Sqlite.sqlite")
cursor = con.cursor()

query = "Select * from artist"
artists_df = pd.DataFrame(cursor.execute(query).fetchall(), columns=['artist_id', 'artist_name'])
# print(artists_df)

query = "Select * from album"
albums_df = pd.DataFrame(cursor.execute(query).fetchall(), columns=['album_id', 'album_title', 'artist_id'])
# print(albums_df)

#Printing Album Information for 'AudioSlave'
query = "Select at.ArtistId as 'Artist ID', at.Name as 'Artist Name', al.Title as 'Album Title' from album al inner join artist at on at.ArtistId = al.ArtistId where at.Name = \'Audioslave\'"
data_Audioslave = pd.read_sql_query(query, con)
print(data_Audioslave)
print("\n")

#Printing Album information for all the aritst.
query_1 = "Select at.ArtistId as 'Artist ID', at.Name as 'Artist Name', al.Title as 'Album Title' from album al inner join artist at on at.ArtistId = al.ArtistId"
data = pd.read_sql_query(query_1, con)
print(data)


#artist_album = albums_df.set_index('artist_id').join(artists_df, on=['artist_id'])
# print(artist_album)

