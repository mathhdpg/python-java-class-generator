def get_attribute_name(field_name):
    words = field_name.split('_')
    attribute_name = words[0] + ''.join(word.capitalize() for word in words[1:])
    attribute_name = attribute_name[0].lower() + attribute_name[1:]
    return attribute_name

def get_capitalized_attribute_name(field_name):
    words = field_name.split('_')
    return ''.join(word.capitalize() for word in words)

def get_fk_field_name(field_name):
    return field_name.replace("id_", "").replace("_id", "")

def get_class_name_by_table_name(table_name):
    if table_name.startswith("lca_"):
        table_name = table_name[4:]
    return ' '.join(name.capitalize() for name in table_name.split('_')).replace(' ', '')