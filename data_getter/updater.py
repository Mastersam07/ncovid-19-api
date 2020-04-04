from apscheduler.schedulers.background import BackgroundScheduler
from data_getter import getData


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(getData.update_database, 'interval', hours=6)
    scheduler.start()
