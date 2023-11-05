import threading
from datetime import datetime, timedelta
from automate.azkar_mn import azkar_mn
from automate.send_sunah import send_sunah
from automate.send_duaa import send_duaa
from automate.send_ayah import send_ayah
from automate.send_estiadah import send_estiadah
from automate.nawawi import nawawi
from essential.constants import *
from automate.send_hesn import send_hesn
from timer.timez import *

def timer():
    #n# constants and timers
    # time now, and +3 from GMT timezone which is used by pythonanywhere
    # x = datetime.fromtimestamp(mktime(timetz()))
    x = timetz()

    # ayah timer at 1:00
    ayah_y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0)
    while (ayah_y - x).total_seconds() < 0:
        ayah_y = ayah_y + timedelta(hours=ayah_repeater)
    delta_ayah = ayah_y - x
    ayah_secs = delta_ayah.total_seconds()

    # hesn timer at 2:00
    hesn_y = x.replace(day=x.day, hour=2, minute=0, second=0, microsecond=0)
    while (hesn_y - x).total_seconds() < 0:
        hesn_y = hesn_y + timedelta(hours=hesn_repeater)
    delta_hesn = hesn_y - x
    hesn_secs = delta_hesn.total_seconds()

    # the first duaa timer at 00:30
    duaa_y = x.replace(day=x.day, hour=0, minute=30, second=0, microsecond=0)
    while (duaa_y - x).total_seconds() < 0:
        duaa_y = duaa_y + timedelta(hours=duaa_repeater)
    delta_duaa = duaa_y - x
    duaa_secs = delta_duaa.total_seconds()

    # estiadah timer at 4:00
    es_y = x.replace(day=x.day, hour=4, minute=0, second=0, microsecond=0)
    while (es_y - x) < timedelta(0):
        es_y = es_y + timedelta(hours=estiadah_repeater)
    delta_es = es_y - x
    es_secs = delta_es.total_seconds()

    #  sunan nawawi timer at 5:00
    na_y = x.replace(day=x.day, hour=5, minute=0, second=0, microsecond=0)
    while (na_y - x) < timedelta(0):
        na_y = na_y + timedelta(hours=nawawi_repeater)
    delta_na = na_y - x
    na_secs = delta_na.total_seconds()

    # azkar for morning and evening timer at 6:00
    azkar_y = x.replace(day=x.day, hour=6, minute=0, second=0, microsecond=0)
    while (azkar_y - x) < timedelta(0):
        azkar_y = azkar_y + timedelta(hours=azkar_mn_repeater)
    delta_azkar = azkar_y - x
    azkar_secs = delta_azkar.total_seconds()

    # sunah timer at 8:00
    sunah_y = x.replace(day=x.day, hour=8, minute=0, second=0, microsecond=0)
    while sunah_y - x < timedelta(0):
        sunah_y = sunah_y + timedelta(hours=sunah_repeater)
    delta_sunah = sunah_y - x
    sunah_secs=delta_sunah.total_seconds()


    sunah_t = threading.Timer(sunah_secs, send_sunah)
    sunah_t.name = "suna_timer"
    sunah_t.start()


    estiadah_t = threading.Timer(es_secs, send_estiadah)
    estiadah_t.name = "estiadah_timer"
    estiadah_t.start()

    naw_t = threading.Timer(na_secs, nawawi)
    naw_t.name = "nawawi_timer"
    naw_t.start()

    ayah_t = threading.Timer(ayah_secs, send_ayah)
    ayah_t.name = "ayah_timer"
    ayah_t.start()

    duaa_t = threading.Timer(duaa_secs, send_duaa)
    duaa_t.name = "duaa_timer"
    duaa_t.start()

    hesn_t = threading.Timer(hesn_secs, send_hesn)
    hesn_t.name = "hesn_timer"
    hesn_t.start()

