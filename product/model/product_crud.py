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

        return True

    except Exception as e:
        log_msg("crate fail: {}".format(e))
        return False


def update_product(id, name, code, category, size, unit_price, inventory, color):
    try:
        product = session.query(Product).filter_by(id=id).first()
        if name:
            product.name = name

        if code:
            product.code = code

        if category:
            product.category = category

        if size:
            product.size = size

        if isinstance(unit_price, int) and unit_price >= 0:
            product.unit_price = unit_price

        if isinstance(inventory, int) and inventory >= 0:
            product.inventory = inventory

        if color:
            product.color = color

        session.commit()

        retrun True

    except Exception as e:
        log_msg("update fail: {}".format(e))
        return False


def get_product(id):
    try:
        product = session.query(Product).filter_by(id=id).first()
        val = {
            "name": product.name
            "code": product.code
            "category": product.category
            "size": product.size
            "unit_price": product.unit_price
            "inventory": product.inventory
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

