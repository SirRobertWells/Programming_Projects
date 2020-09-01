import datetime
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


alarmHour = int(input('What hour do you want to wake up?'))
alarmMinute = int(input('What minute do you want to wake up?'))
amPm = str(input('am or pm?'))

if amPm == 'pm':
    alarmHour += 12

while True:
    if (alarmHour == datetime.datetime.now().hour and
            alarmMinute == datetime.datetime.now().minute):
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        print('Wake up Lazy!')
        break
print('exited')
