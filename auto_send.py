import pyautogui
import time

xabar='Rahmat'
n=100
print('Boshlandi')

count=10
while (count!=0):
    time.sleep(1)
    count-=1

print('Bajarildi')

for i in range(0, int(n)):
    pyautogui.typewrite(xabar+'\n')
