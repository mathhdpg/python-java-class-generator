from file_utils import write_to_file
from string_utils import *

CONTROLLER_TEMPLATE_FILE = "file-models/ControllerModel.txt"
CONTROLLER_IMPL_TEMPLATE_FILE = "file-models/ControllerImplModel.txt"
GENERATE_PATH = "generated/"

def generate_controller(class_name):
    with open(CONTROLLER_TEMPLATE_FILE, "r") as file:
        template_content = file.read()

    template_content = template_content.replace("{{ClassName}}", class_name)
    template_content = template_content.replace("{{ClassNameParameter}}", get_attribute_name(class_name))

    write_to_file(GENERATE_PATH + "I" + class_name + "Controller.java", template_content)

    
def generate_controller_impl(class_name):
    with open(CONTROLLER_IMPL_TEMPLATE_FILE, "r") as file:
        template_content = file.read()

    template_content = template_content.replace("{{ClassName}}", class_name)
    template_content = template_content.replace("{{ClassNameParameter}}", get_attribute_name(class_name))

    write_to_file(GENERATE_PATH + class_name + "Controller.java", template_content)