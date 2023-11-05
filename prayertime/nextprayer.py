from datetime import datetime, timedelta
from .prayertime import prayertime
import threading
from essential.exceptionf import exceptionf
from automate.prayerreminder import prayerreminder
from automate.send_duha import send_duha
from automate.send_watir import send_watir
from automate.qiyam import qiyam
from automate.white_days_reminder import white_days_reminder
from automate.kahf_friday import kahf_friday
from automate.mt_days_reminder import mt_days_reminder
from essential.constants import h, m
from automate.send_adha10 import send_adha10
from automate.azkar_mn import azkar_mn
from timer.timez import *
from automate.salah_friday import salah_friday

def nextprayer():
    # x = datetime.today() + timedelta(hours=3)
    # x = datetime.fromtimestamp(mktime(timetz()))
    x = timetz()
    print(x)
    a = x.strftime("%Y-%m-%d")
    b = prayertime(a)
    # the next timer
    prayertom_y = x.replace(day=x.day, hour=2, minute=30, second=0, microsecond=0) + timedelta(days=1)
    delta_prayertom = prayertom_y - x
    prayertom_secs = delta_prayertom.total_seconds()
    t_nextprayer = threading.Timer(prayertom_secs, nextprayer)
    t_nextprayer.name = "next_prayertimes_timer"
    t_nextprayer.start()
    # ----
    prayertimes = []
    for prayer in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
        try:
            t = (x.replace(day=x.day, hour=int(b[prayer][0:2]), minute=int(b[prayer][3:5]), second=0, microsecond=0)) - x
            if t > timedelta(0):
                prayertimes.append(int(t.total_seconds()))
                l = t.total_seconds()
                t_prayer = threading.Timer(l, prayerreminder)
                t_prayer.name = f"prayer_timer_{prayer}"
                t_prayer.start()
            else:
                prayertimes.append(None)
        except Exception as arg:
            exceptionf(arg)
   # prayertimes_m=[]
   # for x in prayertimes:
    #    if isinstance(x,int):
      #      prayertimes_m.append(x/60)
    #    else:
    #        prayertimes_m.append(x)
    print(prayertimes)
    try:
        t = (x.replace(day=x.day, hour=int(b["Sunrise"][0:2]), minute=int(b["Sunrise"][3:5]), second=0, microsecond=0)) - x
        if t > timedelta(0):
            l = t.total_seconds()
            t_duha = threading.Timer(l, send_duha)
            t_duha.name = "duha_reminder"
            t_duha.start()
    except Exception as arg:
        exceptionf(arg)
    try:
        t = (x.replace(day=x.day, hour=int(b["Fajr"][0:2]), minute=int(b["Fajr"][3:5]), second=0, microsecond=0)) - x
        if t > timedelta(0):
            l = t.total_seconds()
            t_azkar_m = threading.Timer(l + 0.5*h, azkar_mn)
            t_azkar_m.name = "azkar_m"
            t_azkar_m.start()
    except Exception as arg:
        exceptionf(arg)
    try:
        t = (x.replace(day=x.day, hour=int(b["Asr"][0:2]), minute=int(b["Asr"][3:5]), second=0, microsecond=0)) - x
        if t > timedelta(0):
            l = t.total_seconds()
            t_azkar_n = threading.Timer(l + 0.5*h, azkar_mn)
            t_azkar_n.name = "azkar_n"
            t_azkar_n.start()
    except Exception as arg:
        exceptionf(arg)

    try:
        t = (x.replace(day=x.day, hour=int(b["Isha"][0:2]), minute=int(b["Isha"][3:5]), second=0, microsecond=0)) +timedelta(hours=1) - x
        if t > timedelta(0):
            l = t.total_seconds()
            t_watir = threading.Timer(l, send_watir)
            t_watir.name = "watir_reminder"
            t_watir.start()
    except Exception as arg:
        exceptionf(arg)

    try:
        t = (x.replace(day=x.day, hour=int(b["Lastthird"][0:2]), minute=int(b["Lastthird"][3:5]), second=0, microsecond=0)) - x + timedelta(days=1, hours=-2)
        if t > timedelta(0):
            l = t.total_seconds()
            t_qiyam = threading.Timer(l, qiyam)
            t_qiyam.name = "qiyam_timer"
            t_qiyam.start()
    except Exception as arg:
        exceptionf(arg)
    if  b["date"]["hijri"]["day"] in ["12","13","14"]:
        try:
            if isinstance(prayertimes[-2], int):
                t_wd = threading.Timer(prayertimes[-2]+0.25*h, white_days_reminder)
            elif isinstance(prayertimes[-1], int):
                t_wd = threading.Timer(prayertimes[-1]+0.25*h, white_days_reminder)
            try:
                t_wd.name = "white_day_reminder_timer"
                t_wd.start()
            except:
                pass

        except Exception as arg:
            exceptionf(arg)
    if (b["date"]["hijri"]["month"]["number"]) == 12:
        if int(b["date"]["hijri"]["day"]) < 11:
            try:
                if isinstance(prayertimes[0], int):
                    t_adha10 = threading.Timer(prayertimes[0]+2*h, send_adha10)
                elif isinstance(prayertimes[1], int):
                    t_adha10 = threading.Timer(prayertimes[1]+2*h, send_adha10)
                elif isinstance(prayertimes[2], int):
                    t_adha10 = threading.Timer(prayertimes[2]+2*h, send_adha10)
                try:
                    t_adha10.name = "10_days_before_eid_adha_timer"
                    t_adha10.start()
                except:
                    pass
            except Exception as arg:
                exceptionf(arg)

    if  (b['date']['gregorian']['weekday']['en']) in ["Sunday", "Wednesday"]:
        try:
            if isinstance(prayertimes[-2], int):
                t_mt = threading.Timer(prayertimes[-2]+0.25*h, mt_days_reminder)
            elif isinstance(prayertimes[-1], int):
                t_mt = threading.Timer(prayertimes[-1]+0.25*h, mt_days_reminder)
            try:
                t_mt.name = "monday_thursday_reminder_timer"
                t_mt.start()
            except:
                print('t_mt not defined')
                pass
        except Exception as arg:
            exceptionf(arg)
    if ( b['date']['gregorian']['weekday']['en']) in ["Friday"]:
        try:
            if isinstance(prayertimes[1], int):
                t_f = threading.Timer(prayertimes[1] + 0.5*h, kahf_friday)
            elif isinstance(prayertimes[2], int):
                t_f = threading.Timer(prayertimes[2] + 0.5*h, kahf_friday)
            try:
                t_f.name = "kahf_reminder"
                t_f.start()
            except:
                pass
        except Exception as arg:
            exceptionf(arg)
    if ( b['date']['gregorian']['weekday']['en']) in ["Thursday"]:
        try:
            if isinstance(prayertimes[3], int):
                t_sn = threading.Timer(prayertimes[3] + 0.5*h, salah_friday)
            elif isinstance(prayertimes[6], int):
                t_sn = threading.Timer(prayertimes[4] + 0.5*h, salah_friday)
            try:
                t_sn.name = "salah_ala_nabi_reminder"
                t_sn.start()
            except:
                pass
        except Exception as arg:
            exceptionf(arg)


