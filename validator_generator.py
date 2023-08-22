from file_utils import write_to_file
from string_utils import *

VALIDATOR_TEMPLATE_FILE = "file-models/ValidatorModel.txt"
GENERATE_PATH = "generated/"


def generate_validator(class_name, table_name):
    with open(VALIDATOR_TEMPLATE_FILE, "r") as file:
        template_content = file.read()

    template_content = template_content.replace("{{ClassName}}", class_name)
    template_content = template_content.replace(
        "{{ClassNameParameter}}", get_attribute_name(class_name)
    )

    write_to_file(
        GENERATE_PATH, class_name + "Validator.java", template_content
    )