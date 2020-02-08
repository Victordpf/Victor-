#! python3
"""说明：
1、tongxunlu.png图片必须用通讯录显示页最下面的图片；
2、2020春节已经测试过，可以用"""
import pyautogui,os,time,pyperclip
from PIL import Image
os.chdir('D:\\Python-Victor\\快速上手-用过的文件')
pyautogui.PAUSE=0.5
time.sleep(6)
text='拜年啦，拜年啦，鼠年来临之际，鹏飞祝您在鼠年：[此处有音乐]鹏程万里，飞黄腾达，身体健康，阖家安康，财运亨通，福星高照。'
pyperclip.copy(text)
#获取发消息焦点（由于会变动，要调用图片识别），'enter'发送信息
#获取通讯录焦点（图像识别）
tongxunlu=Image.open('tongxunlu.png')
locate1=pyautogui.locateOnScreen(tongxunlu)
center1=pyautogui.center(locate1)

#第一组发送
print(center1)
pyautogui.click(center1)

#以下为第一组发送特有的
renming=Image.open('renming.png')#这个图像为开始的图像，需要重新设置
#这一步是为了获取鼠标的焦点，也可以不用图像识别，直接设置鼠标坐标
#也可以把要单独发送信息的头像设置图像列表，只为个别人发送微信
locate3=pyautogui.locateOnScreen(renming)
center3=pyautogui.center(locate3)
print(center3)
pyautogui.click(center3)
#pyautogui.press('down')

#继续第一组发送
#这里的图像识别不能免除，因为图片的位置是不固定的
faxiaoxi=Image.open('faxiaoxi.png')
locate2=pyautogui.locateOnScreen(faxiaoxi)
center2=pyautogui.center(locate2)
print(center2)
pyautogui.click(center2)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
    

for i in range(942):#控制发送的人数，如果所有联系人共300，则设为300
    #点击到通讯录
    j=i+1
    print('循环中第'+str(j)+'个')
    pyautogui.click(center1)
    pyautogui.click(center3)

    #点击通讯录右边的姓名列，为了能够上下，自动选择灰色的姓名的地方
    pyautogui.press('down')

    #发送消息
    #faxiaoxi=Image.open('faxiaoxi.png')
    locate2=pyautogui.locateOnScreen(faxiaoxi)
    center2=pyautogui.center(locate2)
    pyautogui.click(center2)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
