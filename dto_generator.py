from file_utils import write_to_file
from string_utils import *

ENTITY_TEMPLATE_FILE = "file-models/DtoModel.txt"

def generate_dto(class_name, fields):
    with open(ENTITY_TEMPLATE_FILE, "r") as file:
        template_content = file.read()

    template_content = template_content.replace("{{ClassName}}", class_name)
    template_content = template_content.replace("{{FieldsDeclaration}}", _generate_fields(class_name, fields))

    write_to_file(class_name + "DTO.java", template_content)

def _generate_fields(class_name, fields):
    fields_code = ""
    for field in fields:
        field_name = field["field_name"]

        field_type = field["field_type"]
        attribute_name = get_attribute_name(field_name)
        swagger_doc = get_swagger_doc(class_name, attribute_name)

        if field["is_foreign_key"]:
            referenced_class_name = get_class_name_by_table_name(field["referenced_table"])
            attribute_name = get_attribute_name(get_fk_field_name(field_name))
            field_type = f"{referenced_class_name}DTO"
            swagger_doc = get_swagger_doc(class_name, attribute_name)

        fields_code += f"\t{swagger_doc}\n"
        fields_code += f"\tprivate {field_type} {attribute_name};\n\n"

    return fields_code

def get_swagger_doc(class_name, attribute_name):
    return f'@ApiModelProperty(notes = "${{campo.{class_name}DTO.{attribute_name}.description}}")'
