
import mysql.connector


def connectToMySQL():
    cnx = mysql.connector.connect(password='project', user='project')
    cursor = cnx.cursor()
    return cursor, cnx


def createDatabase(cursor, DB_NAME):
    '''
    :param cursor: instance of the connection to the database
    :param DB_NAME: name of the database to create
    Creates the database at cursor with the given name.
    '''

    try:
        cursor.execute("DROP DATABASE IF EXISTS {}".format(DB_NAME))  # Drops Database If It Exists
    except mysql.connector.Error as err:
        print("Failed dropping database: {}".format(err))

    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def makeTable(cursor):
    infile = open("criminals.txt", "r")
    line = infile.readline()
    line = line.strip()
    fields = line.split(",")
    sql = "CREATE TABLE Incident (" + fields[0] + " INT, " + fields[1] + " VARCHAR(255), " + fields[2] \
          + " VARCHAR(255), " + fields[3] + " VARCHAR(255), " + fields[4] + " VARCHAR(255), " + fields[5] + " INT, " \
          + fields[6] + " INT, " + fields[7] + " VARCHAR(255), " + fields[8] + " VARCHAR(40), " + fields[9] \
          + " VARCHAR(255), " + fields[10] + " VARCHAR(255), " + fields[11] + " VARCHAR(20), " + fields[12] + " VARCHAR(255), " + fields[13] + " VARCHAR(255), " \
          + fields[14] + " CHAR(1), " + fields[15] + " VARCHAR(255), " + fields[16] + " INT, " + fields[17] + " INT, " + fields[18] + " DECIMAL(10,8), " \
          + fields[19] + " DECIMAL(10,8), " + fields[20] + " VARCHAR(100) "  + ");"
    cursor.execute(sql)
    infile.close()
    print("1. Incident table created")

    print(sql)


def insertData(cursor):
    infile = open("criminals.txt", "r")
    header = infile.readline()  # don't need the header line so read past it.
    for line in infile:
        sql = ""
        line = line.strip()
        record = line.split(",")
        if len(record) != 21:
            print(f"Skipping invalid row with {len(record)} columns")
            continue
        data = ""
        for i in range(len(record)):
            if record[i] == "":
                data += "NULL, "
            else:
                data += "'" + record[i] + "', "
        data = data[:-2]
        sql = "INSERT INTO Incident VALUES (" + data + ");"
        cursor.execute(sql)
    infile.close()
    print("2. Incident data inserted into Incident table")


# the question and the query associated with that key as a list of 2 strings
def createQueries():
    queries = {}
    questionsFile = open("questions.txt", "r")
    queryFile = open("queries.txt", "r")
    for question in questionsFile:
        question = question.strip()
        query = queryFile.readline()
        query = query.strip()
        data = question.split(',')
        queries[data[0]] = [question[2:], query]
    questionsFile.close()
    queryFile.close()
    return queries


def questionA(cursor, outfile, queries):
    question = 'a'
    print(question, queries[question][0], sep='. ', file=outfile)
    print(queries[question][1], file=outfile)
    cursor.execute(queries[question][1])
    result = cursor.fetchone()
    while result is not None:
        print(result[0], sep=",", file=outfile)
        result = cursor.fetchone()
    print(file=outfile)



def main():
    DB_NAME = 'NYPD'
    cursor, connection = connectToMySQL()
    createDatabase(cursor, DB_NAME)  # comment this line after first successful run
    cursor.execute("USE {}".format(DB_NAME))
    makeTable(cursor)  # comment this line after first successful run
    insertData(cursor)  # comment this line after first successful run
    queries = createQueries()
    outfile = open("results.txt", "w")
    questionA(cursor, outfile, queries)















    outfile.close()

    # don't modify below this line
    connection.commit()
    cursor.close()
    connection.close()


main()
