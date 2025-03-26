import psycopg

if __name__ == "__main__":
    try:
        conn = psycopg.connect()
        print("Successful connection.")
    except psycopg.OperationalError:
        print("Connection failed.")
        exit(1)
