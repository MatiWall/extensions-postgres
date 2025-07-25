from extensions.postgres import get_connection, set_global_config, get_cursor, read_sql

set_global_config(**{
    'host': 'localhost',
    'port': '5432',  # Usually 5432 for PostgreSQL
    'database': 'test',
    'user': 'postgres',
    'password': 'postgres',
})

with get_cursor() as cursor:
    cursor.execute("""
                   CREATE TABLE your_table (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                   """)

    cursor.execute("""
                   INSERT INTO your_table (id, name) VALUES
                    (1, 'Alice'),
                    (2, 'Bob'),
                    (3, 'Charlie');
                   """)    

with get_connection() as conn:
    with conn.cursor() as cursor:
        select_query = """
            SELECT * FROM public.your_table
            LIMIT 100
        """
        cursor.execute(select_query)
        for row in cursor.fetchall():
            print(row)


print('Spacing \n\n')

with get_cursor() as cursor:
    select_query = """
                SELECT * FROM public.your_table
    LIMIT 100
            """
    cursor.execute(select_query)
    for row in cursor.fetchall():
        print(row)


print('Spacing \n\n')

select_query = """
                SELECT * FROM public.your_table
    LIMIT 100
            """
df = read_sql(select_query)
print(df)

print('Spacing \n\n')

select_query = """
                SELECT * FROM public.your_table WHERE id = %s
            """
df = read_sql(select_query, (1, ))
print(df)