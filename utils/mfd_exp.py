import random
from datetime import datetime, timedelta

# Generate a random date within the last 1 year
def mfd():
    today = datetime.now()
    start_date = today - timedelta(days=365)
    random_date = start_date + timedelta(days=random.randint(0, 365))
    return random_date.strftime("%d-%m-%Y")  

# Expiration date is 3 years from the manufacturing date
def exp(mfd_date):
    mfd_date = datetime.strptime(mfd_date, "%d-%m-%Y")
    exp_date = mfd_date + timedelta(days=3*365)
    return exp_date.strftime("%d-%m-%Y")  
