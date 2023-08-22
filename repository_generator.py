from file_utils import write_to_file
from string_utils import *

REPOSITORY_TEMPLATE_FILE = "file-models/RepositoryModel.txt"
GENERATE_PATH = "generated/"


def generate_repository(class_name, fields):
    with open(REPOSITORY_TEMPLATE_FILE, "r") as file:
        template_content = file.read()

    template_content = template_content.replace("{{ClassName}}", class_name)
    template_content = template_content.replace(
        "{{findByUniqueMethods}}", _generate_unique_queries(class_name, fields)
    )

    write_to_file(GENERATE_PATH, class_name + "Repository.java", template_content)


def _generate_unique_queries(class_name, fields):
    fields_code = ""
    for field in fields:
        if field["unique"]:
            field_name = field["field_name"]
            field_type = field["field_type"]
            capitalized_attribute_name = get_capitalized_attribute_name(field_name)
            attribute_name = get_attribute_name(field_name)

            fields_code += f"\tList<{class_name}> findAllBy{capitalized_attribute_name}({field_type} {attribute_name});\n\n"

    return fields_code
