from file_utils import write_to_file
from string_utils import *

ENTITY_TEMPLATE_FILE = "file-models/EntityModel.txt"
GENERATE_PATH = "generated/"


def generate_entity(table_name, class_name, fields):
    with open(ENTITY_TEMPLATE_FILE, "r") as file:
        template_content = file.read()

    template_content = template_content.replace("{{TableName}}", table_name)
    template_content = template_content.replace("{{ClassName}}", class_name)
    template_content = template_content.replace(
        "{{TableNameWithoutPrefix}}", table_name
    )

    template_content = template_content.replace(
        "{{FieldsDeclaration}}", _generate_fields(table_name, fields)
    )

    write_to_file(GENERATE_PATH, class_name + ".java", template_content)


def _generate_fields(table_name, fields):
    table_name_without_prefix = table_name.replace("lca_", "")

    fields_code = ""
    for field in fields:
        field_type = field["field_type"]
        field_name = field["field_name"]
        temporal_type = field["temporal_type"]
        attribute_name = get_attribute_name(field_name)

        if field["is_primary_key"]:
            fields_code += f"\t@Id\n"
            fields_code += f'\t@Column(name = "{field_name}")\n'
            fields_code += f'\t@GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "{field_name}_{table_name_without_prefix}")\n'
            fields_code += f'\t@SequenceGenerator(name = "{field_name}_{table_name_without_prefix}", sequenceName = "gen_{field_name}_{table_name_without_prefix}", allocationSize = 1, schema = "public")\n'
            fields_code += f"\tprivate {field_type} {attribute_name};\n\n"

        elif field["is_foreign_key"]:
            fk_class_name = get_class_name_by_table_name(field["referenced_table"])
            field_name_without_id = get_fk_field_name(field_name)
            attribute_name = get_attribute_name(field_name_without_id)
            referenced_column_name = field["referenced_field"]

            fields_code += (
                f"\t@ManyToOne(fetch = FetchType.LAZY, cascade = CascadeType.DETACH)\n"
            )
            fields_code += f'\t@JoinColumn(name = "{field_name}", referencedColumnName = "{referenced_column_name}")\n'
            fields_code += f"\tprivate {fk_class_name} {attribute_name};\n\n"

        else:
            fields_code += f'\t@Column(name = "{field_name}")\n'
            if temporal_type:
                fields_code += f"\t@Temporal(TemporalType.{temporal_type})\n"
            fields_code += f"\tprivate {field_type} {attribute_name};\n\n"

    return fields_code
