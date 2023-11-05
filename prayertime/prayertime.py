from essential.exceptionf import exceptionf
from prayer_times_calculator import PrayerTimesCalculator
from retry import retry

@retry(delay=5000)
def prayertime(date):
    calc = PrayerTimesCalculator(
        latitude=31.963158,
        longitude=35.930359,
        calculation_method='gulf',
        date=date,
        school="shafi",
        midnightMode="standard",
        latitudeAdjustmentMethod="middle of the night",
        tune=False,
        imsak_tune=0,
        fajr_tune=0,
        sunrise_tune=0,
        dhuhr_tune=0,
        asr_tune=0,
        maghrib_tune=0,
        sunset_tune=0,
        isha_tune=0,
        fajr_angle=15,
        maghrib_angle=None,
        isha_angle=15,
        iso8601=False
    )
    try:
        times = calc.fetch_prayer_times()
    except Exception as arg:
        exceptionf(arg)
    return times

#-------
