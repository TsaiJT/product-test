# built-in

# 3rd

# module
from utils_tool.common_tools import return_message


##############
# FUNCTION
##############
def get_parameters(params, params_list):
    parameters = {}

    for parameter in params_list:
        if params.get(parameter) != None:
            parameters[parameter] = params.get(parameter)

    return parameters


def check_required_parameter(params, required_list):
    for parameter in required_list:
        if params.get(parameter) is None:
            return return_message(False, "a necessary parameter({}) is missing".format(parameter))

    return {}