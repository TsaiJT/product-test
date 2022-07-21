# built-in

# 3rd

# module
from utils_tool.common_tools import return_message


##############
# FUNCTION
##############
def get_parameters(params, params_list):
    parameters = dict()

    for parameter in params_list:
        if params.get(parameter, None):
            parameters[parameter] = params.get(parameter, None)

    return parameters


def check_required_parameter(params, required_list):
    for parameter in required_list:
        if not params.get(parameter, None):
            return return_message(False, "a necessary parameter({}) is missing".format(parameter))

    return None