import win10toast
toaster = win10toast.ToastNotifier()
import time,datetime
startTime=datetime.datetime(2021, 9, 26)

while datetime.datetime.now()< startTime:
    time.sleep(1)
toaster.show_toast('python','happy birthday taruni',duration=10)
