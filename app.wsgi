import psycopg2

def application(environ, start_response):
    con = None
    status = '200 OK'
    output = ""
    response_headers = [('Content-type', 'text/plain')]

    try:
        con = psycopg2.connect("dbname='testdb' user='vagrant' password='secret'")
        cur = con.cursor()
        
        cur.execute("SELECT * FROM cars;")
        cars = cur.fetchall()
        
        output = "id, name, price\n"
        for car in cars:
            output += "%s, %s, %s\n" % (car[0], car[1], car[2])
        
        response_headers.append(('Content-Length', str(len(output))))
    except psycopg2.DatabaseError, e:
        if con: 
            con.rollback()

        status = '500 Internal Server Error'
        output = str(e)  
        response_headers.append(('Content-Length', str(len(output))))
    finally:
        if con: 
            con.close()

    start_response(status, response_headers)
    return [output]
