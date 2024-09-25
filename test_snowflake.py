import snowflake.connector

conn = snowflake.connector.connect(
    user='junelus',
    password='SnowFlake924!',
    account='mfkwhap-nu09395',
    warehouse='COMPUTE_WH',
    database='MY_DB',
    schema='PUBLIC'
)

try:
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_VERSION()")
    row = cursor.fetchone()
    print(f"Snowflake version: {row[0]}")
finally:
    cursor.close()
    conn.close()
