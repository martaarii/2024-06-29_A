from database.BD_connect import DBConnect
from model.album import Album
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAlbum(num):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.AlbumId, Title , ArtistId, count(*) as numCanzoni
                    from album a 
                    left join track t on t.AlbumId = a.AlbumId 
                    group by AlbumId 
                    having numCanzoni > %s"""
        cursor.execute(query, (num,))
        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result