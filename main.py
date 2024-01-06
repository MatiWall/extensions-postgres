from extensions import get_connection, set_global_config, get_cursor, read_sql

set_global_config(**{
    'host': 'postgres.mw',
    'port': '5432',  # Usually 5432 for PostgreSQL
    'database': 'Test',
    'user': 'postgres',
    'password': 'postgres',
})


with get_connection(database='Test') as conn:
    with conn.cursor() as cursor:
        select_query = """
            SELECT * FROM public.your_table
LIMIT 100
        """
        cursor.execute(select_query)
        for row in cursor.fetchall():
            print(row)


print('Spacing \n\n')

with get_cursor(database='Test') as cursor:
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
df = read_sql(select_query, database='Test')
print(df)