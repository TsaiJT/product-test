# module
from utils_tool.common_tools import log_msg
from model.models import session, Product


def add_product(name, code, category, size, unit_price, inventory, color):
    product = Product(name=name,
                    code=code,
                    category=category,
                    size=size,
                    unit_price=unit_price,
                    inventory=inventory,
                    color=color)
    try:
        session.add(product)
        session.commit()

        return True, product.id

    except Exception as e:
        log_msg("create fail: {}".format(e))
        return False, "{}".format(e)


def update_product(id, **kwargs):
    try:
        product = session.query(Product).filter_by(id=id).first()
    except Exception as e:
        msg = "id not exist"
        log_msg(msg)
        return False, msg

    if kwargs.get("name") is not None:
        product.name = kwargs.get("name")

    if kwargs.get("code") is not None:
        product.code = kwargs.get("code")

    if kwargs.get("category") is not None:
        product.category = kwargs.get("category")

    if kwargs.get("size") is not None:
        product.size = kwargs.get("size")

    if isinstance(kwargs.get("unit_price"), int) and kwargs.get("unit_price") >= 0:
        product.unit_price = kwargs.get("unit_price")

    if isinstance(kwargs.get("inventory"), int) and kwargs.get("inventory") >= 0:
        product.inventory = kwargs.get("inventory")

    if kwargs.get("color") is not None:
        product.color = kwargs.get("color")

    try:
        session.commit()
        return True, ""
    except Exception as e:
        log_msg("update fail: {}".format(e))
        return False, "{}".format(e)




def get_product(id):
    try:
        product = session.query(Product).filter_by(id=id).first()
        val = {
            "name": product.name,
            "code": product.code,
            "category": product.category,
            "size": product.size,
            "unit_price": product.unit_price,
            "inventory": product.inventory,
            "color": product.color
        }

        return True, val

    except Exception as e:
        return False, "Not Found"


def delete_product(id):
    try:
        session.query(Product).filter_by(id=id).delete()
        return True

    except Exception as e:
        log_msg("delete fail: {}".format(e))
        return False

