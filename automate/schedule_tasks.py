import schedule
import time

def task():
    print("Automated Task Running...")

# Schedule the task every minute
schedule.every(1).minute.do(task)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)