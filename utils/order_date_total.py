from datetime import datetime, timedelta

def order_date():
    today = datetime.now()
    return today.strftime("%d-%m-%Y")

