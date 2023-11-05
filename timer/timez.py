# from datetime import datetime
# from pytz import timezone
# from time import mktime


# def timetz(*args):
#     return datetime.now(tz).timetuple()

# tz = timezone('Asia/Jerusalem') # UTC, Asia/Shanghai, Europe/Berlin

# print(datetime.fromtimestamp(mktime(timetz())).strftime("%Y-%m-%d"))

import datetime
from pytz import timezone
# import time

def timetz(*args):
    tz = timezone('Asia/Baghdad') #Amman
    # return datetime.datetime.now(tz).timetuple()
    return datetime.datetime(*datetime.datetime.now(tz).timetuple()[:6], tzinfo=tz)


