import os
from datetime import datetime#, timedelta
import sys
import traceback
##from essential.reporter import reporter
import logging
import logging.config
from timer.timez import *
from essential.constants import my_id
from essential.writer import writer
from essential.deleter import deleter

# def get_time():
#     x = datetime.today() + timedelta(hours=3)#.replace(microsecond=0) + timedelta(hours=3)
#     a = x.strftime("%Y-%m-%d")
# #    t = x.strftime("%H:%M")
#     return a

# def timetz(*args):
#     return datetime.now(tz).timetuple()

# tz = timezone('Asia/Jerusalem') # UTC, Asia/Shanghai, Europe/Berlin






logging.Formatter.converter = timetz

rootLog = logging.getLogger()

logging.basicConfig(filename=f'./errors/std_{timetz().strftime("%Y-%m-%d")}.log',
                    filemode='a',
                    format=('%(levelname)s - at %(asctime)s - %(message)s'), # - at line (%(lineno)d) - filename (%(filename)s) - module (%(module)s) - funcname (%(funcName)s)'),
                    datefmt='%H:%M:%S',
                    level=logging.ERROR)

consoleHandler = logging.StreamHandler()
rootLog.addHandler(consoleHandler)



def exceptionf(arg, **kwargs):
    user = kwargs.get("user", None)
    dic = kwargs.get("dic", None)

    import os
    import sys
    
    print(arg)
    if 'too long' in str(arg):
        bot.send_message(my_id, 'bot has a problem, the text was too long, check what happened')
    elif ('bot was blocked by the user' in str(arg) or 'chat not found' in str(arg) or 'bot is not a member of the channel chat' in str(arg) or 'chat not found' in str(arg) or 'user is deactivated' in str(arg)):
        # bot.send_message(my_id, f'bot has been blocked by tg://user?id={user}')
        writer(deleter(user, dic))

    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logging.error(f"{arg, fname, exc_tb.tb_lineno}")
    # logging.error(f"Error Type : {type(arg).__name__},\n     Error Message : {arg}\n          ")
