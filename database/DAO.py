from database.DB_connect import DBConnect
from model.team import Team


class DAO():
    @staticmethod
    def getAllAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select distinct t.`year`  
                    from teams t 
                    where t.`year` > 1979 """
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getSquadreAnno(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from teams t 
                    where t.`year` = %s"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Team(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPesoSquadra(teamID, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select SUM(s.salary)
                    FROM salaries s 
                    WHERE s.teamID = %s
                    AND s.`year` = %s"""

        cursor.execute(query, (teamID, anno))

        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0]
