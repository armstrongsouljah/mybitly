from django.core.exceptions import ValidationError 
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    reg_val = value
    
    if "http" in reg_val:
        new_value = reg_val
    else:
        new_value = "https://" + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid url for this field")
    return new_value

    # value_1_invalid = False
    # value_2_invalid = False
    # try:
    #    url_validator(value)
    # except:
    #   value_1_invalid = True
    # value_2_url = "http://" + value
    # try:
    #   url_validator(value_2_url)
    # except:
    #   value_2_invalid = True

    # if value_1_invalid == False and value_2_invalid == False:
    #    raise ValidationError("Invalid URL for this field")
    # return value

def validate_dot_com(value):
    if not "com" in value:
        raise ValidationError("Url invalid because no .com found")
    return value
