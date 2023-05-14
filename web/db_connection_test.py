import psycopg2

if __name__ == '__main__':
    try:
        conn = psycopg2.connect()
        print("Successful connection.")
    except psycopg2.OperationalError:
        print("Connection failed.")
        exit(1)
