from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    def getAllTeams():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT *
                    FROM teams t """
        cursor.execute(query)

        for row in cursor:
            result.append(Team(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getYearsTeam(team):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT DISTINCT t.`year` 
                    from teams t 
                    WHERE t.name = %s"""
        cursor.execute(query, (team,))

        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(anno, team):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT SUM(s.salary)
                    FROM teams t , salaries s 
                    WHERE t.`year` = %s
                    AND t.ID = s.teamID 
                    AND t.name = %s"""
        cursor.execute(query, (anno, team))

        for row in cursor:
            if row[0] is None:
                result.append(0)
            else:
                result.append(row[0])

        return result