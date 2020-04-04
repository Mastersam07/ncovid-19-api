from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from api import callmigrate


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(callmigrate.update_database, 'interval', hours=6)
    scheduler.start()
