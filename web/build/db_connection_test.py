import psycopg

if __name__ == "__main__":
    try:
        conn = psycopg.connect()
        print("Successful connection.")
    except Exception as e:
        print(f"Connection failed: {e}")
        exit(1)
