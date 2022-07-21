# built-in
import time, sys

# module
from flask_app import app


##############
# FUNCTION
##############
def log_msg(msg):
    #print(msg)
    app.logger.info(msg)
    sys.stdout.flush()


def return_message(is_ok, msg):

    return {
        "ok": is_ok,
        "msg": msg,
        "timestamp": int(time.time())
    }



