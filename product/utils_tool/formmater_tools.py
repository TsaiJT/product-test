# built-in
import ipaddress, re

# 3rd
from flask import request


# module
from utils_tool.common_tools import return_message



##############
# FUNCTION
##############

# check json format
def check_json_format():
    if not request.is_json:
        return return_message(False, "missing JSON in request")

    return request.get_json()
