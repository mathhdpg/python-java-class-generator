from file_utils import write_to_file
from string_utils import *

SERVICE_TEMPLATE_FILE = "file-models/ServiceModel.txt"
SERVICE_IMPL_TEMPLATE_FILE = "file-models/ServiceImplModel.txt"
GENERATE_PATH = "generated/"


def generate_service(class_name):
    with open(SERVICE_TEMPLATE_FILE, "r") as file:
        template_content = file.read()

    template_content = template_content.replace("{{ClassName}}", class_name)
    template_content = template_content.replace(
        "{{ClassNameParameter}}", get_attribute_name(class_name)
    )

    write_to_file(GENERATE_PATH, class_name + "Service.java", template_content)


def generate_service_impl(class_name, fields):
    with open(SERVICE_IMPL_TEMPLATE_FILE, "r") as file:
        template_content = file.read()

    template_content = template_content.replace("{{ClassName}}", class_name)
    template_content = template_content.replace(
        "{{ClassNameParameter}}", get_attribute_name(class_name)
    )

    # todo - Implementar incluir e editar olhando para os fields

    write_to_file(GENERATE_PATH, class_name + "ServiceImpl.java", template_content)
