from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    def getAllTeams():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT t.* 
                    FROM teams t 
                    """
        cursor.execute(query)

        for row in cursor:
            result.append(Team(**row))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllYears(team):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT DISTINCT t.`year` 
                    from teams t 
                    WHERE t.name =%s
                    """
        cursor.execute(query, (team.name,))

        for row in cursor:
            result.append((row[0]))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getPeso(team, anno1, anno2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT COUNT(DISTINCT a.playerID) 
                    from appearances a , appearances a2 , teams t 
                    WHERE a.teamCode  = a2.teamCode  AND t.teamCode  = a2.teamCode  AND t.name =%s
                    AND a2.playerID = a.playerID
                    AND a.`year`=%s 
                    AND a2.`year`=%s
                    """
        cursor.execute(query, (team.name, anno1, anno2))

        result = cursor.fetchone()

        cursor.close()
        conn.close()
        return result[0]


