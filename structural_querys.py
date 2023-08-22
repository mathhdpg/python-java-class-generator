def get_table_structure(conn, table_name):
    query = """
        SELECT
            column_name,
            data_type,
            character_maximum_length,
            is_nullable,
            column_default,
            ordinal_position
        FROM information_schema.columns
        WHERE table_name = %s
        ORDER BY ordinal_position
    """
    with conn.cursor() as cursor:
        cursor.execute(query, (table_name,))
        columns = cursor.fetchall()

    return columns


def get_primary_keys(conn, table_name):
    query = """
        SELECT a.attname AS column_name
        FROM pg_index i
        JOIN pg_attribute a ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
        WHERE i.indrelid = %s::regclass
        AND i.indisprimary;
    """
    with conn.cursor() as cursor:
        cursor.execute(query, (table_name,))
        pks = cursor.fetchall()

    return [pk[0] for pk in pks]


def get_foreign_keys(conn, table_name):
    query = """
        SELECT conname AS foreign_key_name,
            conrelid::regclass AS table_name,
            a.attname AS column_name,
            cl.relname,
            pg_get_constraintdef(c.oid) AS constraint_definition
        FROM pg_constraint AS c
        JOIN pg_namespace AS n ON n.oid = c.connamespace
        JOIN pg_attribute AS a ON a.attnum = ANY(c.conkey) AND a.attrelid = c.conrelid
        JOIN pg_class AS cl ON cl.oid = c.confrelid
        JOIN pg_namespace AS cn ON cn.oid = cl.relnamespace
        WHERE 1 = 1
        AND conrelid::regclass::text = %s
        AND c.contype = 'f'
        ORDER BY table_name, foreign_key_name;
    """
    with conn.cursor() as cursor:
        try:
            cursor.execute(query, (table_name,))
            fks = cursor.fetchall()
            return fks
        except Exception as e:
            print("Error fetching foreign keys:", e)
            return []


def get_unique_fields(conn, table_name):
    query = """
        SELECT
            conname AS constraint_name,
            conrelid::regclass AS table_name,
            pg_get_constraintdef(c.oid) AS constraint_definition
        FROM pg_constraint AS c
        WHERE contype = 'u'
        AND conrelid::regclass::text LIKE %s
        ORDER BY table_name, constraint_name
    """
    with conn.cursor() as cursor:
        try:
            cursor.execute(query, (table_name,))
            uniques = cursor.fetchall()
            return uniques
        except Exception as e:
            print("Error fetching unique keys:", e)
            return []
