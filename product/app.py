# built-in
from itertools import product
import json

# 3rd
from flask import jsonify

# module
from flask_app import app
from utils_tool.common_tools import log_msg, return_message
from utils_tool.formmater_tools import check_json_format
from utils_tool.parameter_tools import get_parameters, check_required_parameter

from model.product_crud import add_product, update_product, get_product, delete_product, list_product


@app.route('/products/<int:id>', methods=['GET'])
def product_get(id):
    is_existed, val = get_product(id)

    if not is_existed:
        msg = return_message(False, "product id({}) does not exist".format(id))
        return jsonify(**msg), 404
    else:
        msg = return_message(True, val)
        return jsonify(**msg), 200


@app.route('/products', methods=['POST'])
def product_add():

    data_obj = check_json_format()
    if not data_obj.get("is_ok", True): return jsonify(**data_obj)

    # get parameter
    data = get_parameters(params=data_obj,
                        params_list=["name", "code", "category",
                                    "size", "unit_price", "inventory",
                                    "color"])


    is_successful = add_product(data["name"], data["code"], data["category"],
                                data["size"], data["unit_price"], data["inventory"],
                                data["color"])


    if not is_successful:
        msg = return_message(False, "product({}) create failed".format(data["name"]))
        return jsonify(**msg), 409
    else:
        msg = return_message(True, "product({}) create successfully".format(data["name"]))
        return jsonify(**msg), 201


@app.route('/products/<int:id>', methods=['PUT'])
def product_update(id):
    data_obj = check_json_format()
    if not data_obj.get("is_ok", True): return jsonify(**data_obj)

    # get parameter
    data = get_parameters(params=data_obj,
                        params_list=["name", "code", "category",
                                    "size", "unit_price", "inventory",
                                    "color"])

    update_val = {}
    for key in ["name", "code", "category", "size", "color"]:
        if data[key]:
            update_val[key] = data[key]

    for key in ["unit_price", "inventory"]:
        if data.get(key, -1) >= 0:
            update_val[key] = data[key]


    is_successful = update_product(id=id, **update_val)

    if not is_successful:
        msg = return_message(False, "product({}) update failed".format(id))
        return jsonify(**msg), 409
    else:
        msg = return_message(True, "product({}) update successfully".format(id))
        return jsonify(**msg), 200



@app.route('/products/<int:id>', methods=['DELETE'])
def product_delete(id):

    is_successful = delete_product(id)

    if not is_successful:
        msg = return_message(False, "product({}) delete failed".format(id))
        return jsonify(**msg), 409
    else:
        msg = return_message(True, "product({}) delete successfully".format(id))
        return jsonify(**msg), 200