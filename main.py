import psycopg2
import argparse

from entity_generator import generate_entity
from dto_generator import generate_dto
from repository_generator import generate_repository
from structural_querys import *
from connection import get_connection
from string_utils import get_class_name_by_table_name

def get_class_fields(columns, pks, fks, unique):
    class_fields = []

    for column in columns:
        field_name = column[0]
        data_type = column[1]
        character_max_length = column[2]
        is_nullable = (column[3] == "YES")
        referenced_table = None
        referenced_field = None
        temporal_type = ""
        java_type = "String"
        is_primary_key = (field_name in pks)
        is_foreign_key = any(fk[2] == field_name for fk in fks)
        is_unique = any(field_name in un[2] for un in unique)        

        if data_type == "character varying":
            java_type = "String"
        elif data_type == "integer" or data_type == "bigint":
            java_type = "Integer"
        elif data_type == "double precision" or data_type == "numeric":
            java_type = "BigDecimal"
        elif data_type == "boolean":
            java_type = "Boolean"
        elif data_type == "date":
            java_type = "Date"
            temporal_type = "DATE"
        elif data_type == "timestamp without time zone":
            java_type = "Date"
            temporal_type = "TIMESTAMP"
        else:
            print("TIPO NÃO TRATADO: %s",  data_type)
        
        if is_foreign_key:
            for fk in fks:
                if fk[2] == field_name:
                    referenced_table = fk[3]
                    referenced_field = "id" #fk[4]
                    break
        
        field_object = {
            "field_name": field_name,
            "field_type": java_type,
            "max_length": character_max_length,
            "not_null": not is_nullable,
            "unique": is_unique,
            "is_primary_key": is_primary_key,
            "is_foreign_key": is_foreign_key,
            "referenced_table": referenced_table,
            "referenced_field": referenced_field,
            "temporal_type": temporal_type
        }
        
        class_fields.append(field_object)
    return class_fields

def main(table_name):
    try:
        conn = get_connection()

        # table_name = "pedido"
        class_name = get_class_name_by_table_name(table_name)

        columns = get_table_structure(conn, table_name)
        pks = get_primary_keys(conn, table_name)
        fks = get_foreign_keys(conn, table_name)
        unique = get_unique_fields(conn, table_name)

        fields = get_class_fields(columns, pks, fks, unique)

        # generate_entity(table_name, class_name, fields)
        # generate_dto(class_name, fields)
        # generate_service(class_name, fields)
        # generate_controller(class_name, fields)
        generate_repository(class_name, fields)
        # generate_validator(class_name, fields)

    except psycopg2.Error as e:
        print("Error:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate DTO classes from a database table")
    parser.add_argument("table_name", help="Name of the database table to generate DTO for")
    args = parser.parse_args()

    main(args.table_name)