import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
from kivy.lang import Builder
from kivy.core.window import  Window
from kivy.graphics import Rectangle, Color
from datetime import datetime , timedelta
from kivy.core.image import Image
from kivy.uix.popup import Popup
import socket
import os
#Builder.load_file('a.kv')
class Eleventhpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        aa = open("file_main.txt", 'r')
        for i in range(1, 20):
            aa.readline()
        MAC = aa.readline()

        aa.close()
        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()
class Tenthpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        aa = open("file_main.txt", 'r')
        for i in range(1, 18):
            aa.readline()
        MAC = aa.readline()
        aa.close()
        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()
class Ninthpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        aa = open("file_main.txt", 'r')
        for i in range(1, 16):
            aa.readline()
        MAC = aa.readline()
        aa.close()
        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()
class Eigthpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        aa = open("file_main.txt", 'r')
        for i in range(1, 14):
            aa.readline()
        MAC = aa.readline()
        aa.close()
        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()
class Seventhpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        aa = open("file_main.txt", 'r')
        for i in range(1, 12):
            aa.readline()
        MAC = aa.readline()
        aa.close()
        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()
class Sixthpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        aa = open("file_main.txt", 'r')
        for i in range(1, 10):
            aa.readline()
        MAC = aa.readline()
        aa.close()
        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()
class Fifthpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        aa = open("file_main.txt", 'r')
        for i in range(1, 8):
            aa.readline()
        MAC = aa.readline()
        aa.close()
        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()
class Fourthpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        aa = open("file_main.txt", 'r')
        for i in range(1, 6):
            aa.readline()
        MAC = aa.readline()
        aa.close()
        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()
class Thirdpage(FloatLayout):
    def __init__(self):
        super().__init__()
        self.logo = Label(text='DPU', bold=True, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'y': 0.82},
                          font_size=36)
        self.add_widget(self.logo)
        self.presence=Button(text='     MARK\nPRESENCE',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.5,'y':0.4},background_color='#75141B',on_press=self.on_press)
        self.add_widget(self.presence)
        self.back=Button(text='<-',bold=True,size_hint=(0.2, 0.07),pos_hint={'x':0.04,'y':0.9},background_color='#75141B',on_press=self.go_back)
        self.add_widget(self.back)

    def go_back(self,obj):
        myapp.screen_manager.current = 'second'

    def on_press(self,obj2):
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

        aa=open("file_main.txt",'r')
        for i in range(1,4):
            aa.readline()
        MAC=aa.readline()
        print(MAC)

        client.connect((MAC, 19))
        fa=open("file_main.txt",'r')
        a=fa.readline()
        fa.close()
        #len(roll_no)
        len=3
        roll=''
        while(len>0):

            roll+=a[-len]
            len-=1
        print(roll)



        try:

            message = "roll no "+roll+" present"
            client.send(message.encode("utf-8"))
                # data=client.recv(1024)
                # if not data:
                #     break
                # print(f"Message :{data.decode('utf-8')}")

        except OSError as e:
            pass
        client.close()


class Secondpage(FloatLayout):
    def __init__(self):
        super().__init__()

        self.on_press=0

        self.logo=Label(text='DPU',bold=True,size_hint=(0.5,0.2),pos_hint={'center_x':0.16,'y':0.82},font_size=36)
        self.add_widget(self.logo)

        self.add_subj=Button(text='+',size_hint=(0.4,0.07),pos_hint={'x':0.05,'y':0.05},on_press=self.add,bold=True,background_color='#75141B')
        self.add_widget(self.add_subj)

        self.remove_subj = Button(text='-', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.05},
                               on_press=self.final_Remove, bold=True, background_color='#75141B')
        self.add_widget(self.remove_subj)

        self.button1 = Button(text='  ', size_hint=(0.4, 0.07), pos_hint={'x': 0.05, 'y': 0.72}, on_press=self.ch_scr_2,
                              bold=True, background_color='#75141B')
        self.button2 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.05, 'y': 0.62},
                              on_press=self.ch_scr_2, bold=True, background_color='#75141B')
        self.button3 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.05, 'y': 0.52},
                              on_press=self.ch_scr_2, bold=True, background_color='#75141B')
        self.button4 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.05, 'y': 0.42},
                              on_press=self.ch_scr_2, bold=True, background_color='#75141B')
        self.button5 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.72},
                              on_press=self.ch_scr_2, bold=True, background_color='#75141B')
        self.button6 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.62},
                              on_press=self.ch_scr_2, bold=True, background_color='#75141B')
        self.button7 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.52},
                              on_press=self.ch_scr_2, bold=True, background_color='#75141B')
        self.button8 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.42},
                              on_press=self.ch_scr_2, bold=True, background_color='#75141B')
        self.button9 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.32},
                              on_press=self.ch_scr_2, bold=True, background_color='#75141B')
        # self.add_widget(self.button1)
        self.keep_button()




    def add(self,obj):
        self.text1=Label(text='Special Code : ',size_hint=(0.4,0.07),pos_hint={'x':0,'y':0.19},color=(1,1,1),bold=True)
        self.new_subj_code=TextInput(text=' ',size_hint=(0.4,0.05),pos_hint={'x':0.05,'y':0.15},border=(20,20,20,20),multiline=False)

        self.text2 = Label(text='Subject : ', size_hint=(0.4, 0.07), pos_hint={'x': 0, 'y': 0.29}, color=(1, 1, 1),bold=True)
        self.new_subj_2 = TextInput(text=' ', size_hint=(0.4, 0.05), pos_hint={'x': 0.05, 'y': 0.25},border=(20, 20, 20, 20),multiline=False)

        self.final_submit=Button(text='apply', size_hint=(0.2, 0.07), pos_hint={'x': 0.05, 'y': 0.32},on_press=self.final_Submit, bold=True, background_color='#75141B')

        self.add_widget(self.final_submit)
        self.add_widget(self.text1)
        self.add_widget(self.new_subj_code)
        self.add_widget(self.text2)
        self.add_widget(self.new_subj_2)






    def keep_button(self):
        m=open("file_main.txt",'r')
        m.readline()
        m.readline()

        if len(m.readline())==1:
            m.close()
            try:
                with open('file_main.txt', 'r') as fr:
                    # reading line by line
                    lines = fr.readlines()

                    # pointer for position
                    ptr = 1

                    # opening in writing mode
                    with open('file_main.txt', 'w') as fw:
                        for line in lines:

                            # we want to remove 5th line
                            if ptr != 3:
                                fw.write(line)
                            ptr += 1
                #print("Deleted")

            except:
                print("Oops! something error")




        max_subj_check_1=2
        a=open("file_main.txt",'r')
        a.readline()

        while True:
            ab = a.readline()
            if len(ab) == 0:
                break
            max_subj_check_1+=1
            #print(max_subj_check_1)
            #print(ab)

            if max_subj_check_1==4:


                self.button1.text=ab
                self.add_widget(self.button1)
            elif max_subj_check_1==6 :
                self.button2.text=ab
                self.add_widget(self.button2)
            elif max_subj_check_1 == 8 :
                self.button3.text=ab
                self.add_widget(self.button3)
            elif max_subj_check_1 == 10 :
                self.button4.text=ab
                self.add_widget(self.button4)
            elif max_subj_check_1 == 12:
                self.button5.text=ab
                self.add_widget(self.button5)
            elif max_subj_check_1 == 14:
                self.button6.text=ab
                self.add_widget(self.button6)
            elif max_subj_check_1 == 16 :
                self.button7.text=ab
                self.add_widget(self.button7)
            elif max_subj_check_1 == 18:
                self.button8.text=ab
                self.add_widget(self.button8)
            elif max_subj_check_1 == 20 :
                self.button9.text=ab
                self.add_widget(self.button9)
            else:
                pass




        a.close()


    def final_Remove(self,obj5):

        self.remove_widget(self.button1)
        self.remove_widget(self.button2)
        self.remove_widget(self.button3)
        self.remove_widget(self.button4)
        self.remove_widget(self.button5)
        self.remove_widget(self.button6)
        self.remove_widget(self.button7)
        self.remove_widget(self.button8)
        self.remove_widget(self.button9)
        f0=open("file_main.txt",'r+')

        t=f0.readline()
        k=f0.readline()

        f0.close()

        f7=open("file_main.txt",'w')
        f7.write("")
        f7.close()

        f8=open("file_main.txt","a")
        f8.writelines(t)
        f8.writelines(k)


        f8.close()
    def final_Submit(self,obj1):

        max_subj_check=2
        f0=open('file_main.txt', 'r')
        f0.readline()
        while f0.readline() !="":
            max_subj_check+=1
            #print(max_subj_check)
        f0.close()
        max_subj_check-=1

        if max_subj_check < 20:
            f1=open('file_main.txt', 'a')
            f1.write("\n")
            f1.write(self.new_subj_2.text)
            f1.write("\n")
            f1.write(self.new_subj_code.text)
            f1.close()

            self.remove_widget(self.final_submit)
            self.remove_widget(self.text1)
            self.remove_widget(self.new_subj_code)
            self.remove_widget(self.text2)
            self.remove_widget(self.new_subj_2)

            self.add_subject_main_button()





        else :
            layout = GridLayout(cols=1, padding=10)

            popupLabel = Label(text="Max 09 subject ")
            closeButton = Button(text="Close")

            layout.add_widget(popupLabel)
            layout.add_widget(closeButton)

            # Instantiate the modal popup and display
            popup = Popup(title='Alert!!',
                          content=layout,size_hint=(0.5,0.33))
            popup.open()

            # Attach close button press with popup.dismiss action
            closeButton.bind(on_press=popup.dismiss)

            self.remove_widget(self.final_submit)
            self.remove_widget(self.text1)
            self.remove_widget(self.new_subj_code)
            self.remove_widget(self.text2)
            self.remove_widget(self.new_subj_2)

    def add_subject_main_button(self):
        new_button_pos = Window.size

        self.button1 = Button(text='  ', size_hint=(0.4, 0.07), pos_hint={'x': 0.05, 'y': 0.72}, on_press=self.ch_scr_2,
                              bold=True, background_color='#75141B')
        self.button2 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.05, 'y': 0.62},
                              on_press=self.ch_scr_3, bold=True, background_color='#75141B')
        self.button3 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.05, 'y': 0.52},
                              on_press=self.ch_scr_4, bold=True, background_color='#75141B')
        self.button4 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.05, 'y': 0.42},
                              on_press=self.ch_scr_5, bold=True, background_color='#75141B')
        self.button5 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.72},
                              on_press=self.ch_scr_6, bold=True, background_color='#75141B')
        self.button6 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.62},
                              on_press=self.ch_scr_7, bold=True, background_color='#75141B')
        self.button7 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.52},
                              on_press=self.ch_scr_8, bold=True, background_color='#75141B')
        self.button8 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.42},
                              on_press=self.ch_scr_9, bold=True, background_color='#75141B')
        self.button9 = Button(text='add', size_hint=(0.4, 0.07), pos_hint={'x': 0.55, 'y': 0.32},
                              on_press=self.ch_scr_10, bold=True, background_color='#75141B')

        self.keep_button()


    def ch_scr_2(self,onj2):
        myapp.screen_manager.current = 'third'


    def ch_scr_3(self,onj3):
        myapp.screen_manager.current = 'fourth'

    def ch_scr_4(self,onj4):
        myapp.screen_manager.current = 'fifth'

    def ch_scr_5(self,onj5):
        myapp.screen_manager.current = 'sixth'

    def ch_scr_6(self,onj6):
        myapp.screen_manager.current = 'seventh'

    def ch_scr_7(self,onj7):
        myapp.screen_manager.current = 'eigth'

    def ch_scr_8(self,onj8):
        myapp.screen_manager.current = 'ninth'

    def ch_scr_9(self,onj9):
        myapp.screen_manager.current = 'tenth'

    def ch_scr_10(self,onj10):
        myapp.screen_manager.current = 'eleventh'

class Mylayout(FloatLayout):
    def __init__(self):
        super().__init__()
        if os.path.getsize("file_main.txt")>0:
            self.submit = Button(text='Login', size_hint=(0.4, 0.1), pos_hint={'x': 0.30, 'y': 0.40},
                                 on_press=self.ch_scr, bold=True, background_color='#75141B')
            self.add_widget(self.submit)

        else :

            self.registration_page()


        #self.page_check(a)
    #def page_check(self,a):
        #if a==1:
                #self.registration_page()
        #else : self.main_page1()

    def registration_page(self):

        size=Window.size
        print(size)
        self.rect = Rectangle(pos=(20, self.center_y-10), size=((0.2*size[0]),(0.76*size[1])),radius=25,color=(228,226,177))
        self.canvas.add(self.rect)
        self.canvas.add(Color(228, 226, 177))
        #print(self.center_y)
        self.rect1=Rectangle(pos=(0,self.height * 6.5), size=((1*size[0]),(1*size[1])),radius=25,color=(228,226,177))
        self.canvas.add(self.rect1)
        self.canvas.add(Color(228, 226, 177))


        self.label=Label(text='REGISTER',size_hint=(0.5,0.2),pos_hint={'x':0.27,'y':0.8},color=(0,0,0),bold=True)

        self.label1=Label(text='Name : ',size_hint=(0.5,0.2),pos_hint={'x':0,'y':0.66},color=(0,0,0),bold=True)
        self.name=TextInput(text=' ',size_hint=(0.3,0.05),pos_hint={'x':0.1,'y':0.65},border=(20,20,20,20))

        self.label2 = Label(text='Year : ',size_hint=(0.5,0.2),pos_hint={'x':0,'y':0.48},color=(0,0,0),bold=True)
        self.spinnerObject = Spinner(text="select", values=("FE", "SE", "TE","BE"),background_color='#75141B')
        self.spinnerObject.size_hint = (0.3, 0.05)
        self.spinnerObject.pos_hint = {'x': .1, 'y': .45}

        self.label3 = Label(text='Class : ',size_hint=(0.5,0.2),pos_hint={'x':0,'y':0.08},color=(0,0,0),bold=True)
        self.clas = TextInput(text='A',size_hint=(0.3,0.05),pos_hint={'x':0.1,'y':0.06})

        self.label4 = Label(text='Roll number : ',size_hint=(0.5,0.2),pos_hint={'x':0,'y':0.28},color=(0,0,0),bold=True)
        self.roll_no = TextInput(text='1',size_hint=(0.3,0.05),pos_hint={'x':0.1,'y':0.25})

        self.submit=Button(text='submit',size_hint=(0.4,0.1),pos_hint={'x':0.55,'y':0.35},on_press=self.submit_data,bold=True,background_color='#75141B')


        self.add_widget(self.label)
        self.add_widget(self.label1)
        self.add_widget(self.name)
        self.add_widget(self.label2)
        #self.add_widget(self.year)
        self.add_widget(self.spinnerObject)
        #self.add_widget(self.main_button)
        self.add_widget(self.label3)
        self.add_widget(self.clas)
        self.add_widget(self.label4)
        self.add_widget(self.roll_no)
        self.add_widget(self.submit)


        #page 2 labels








    def submit_data(self,obj):
        print(self.name.text)
        print(self.spinnerObject.text)
        print(self.clas.text)
        print(self.roll_no.text)

        if self.name.text!="" and self.spinnerObject.text!="select" and self.clas.text!='' and self.roll_no.text!='':

            f = open('file_main.txt', 'a')
            f.writelines(self.name.text)
            f.writelines(self.spinnerObject.text)
            f.writelines(self.clas.text)
            f.writelines(self.roll_no.text)
            f.writelines("\n")
            f.writelines("go next")
            f.close()
            #self.main_page1()
            myapp.screen_manager.current='second'


        else:
            self.registration_page()
        #self.page_check(a)
    def ch_scr(self,obj):
        myapp.screen_manager.current = 'second'

    #def spinner_clicked(self):
       # pass

        #print(self.name)
class MyApp(App):
    def build(self):
        if not os.path.exists('App'):
         os.mkdir('App')
        else:
            print("already exists")
        if not os.path.isfile("file_main.txt") :
         f = open("file_main.txt", "x")
         f.close()
        else:
            print("file already exists")
        #with open('file_main.txt','r') as fp:
            #if fp.readline() == "":
             # a=1
            #else:
             #   a=0
        #fp.close()
        self.screen_manager = ScreenManager()
        #if os.path.getsize("file_main.txt")>0:
            #a=0

        self.firstpage = Mylayout()
        screen = Screen(name='first')
        screen.add_widget(self.firstpage)
        self.screen_manager.add_widget(screen)
        #else :
        self.secondpage=Secondpage()
        screen=Screen(name='second')
        screen.add_widget(self.secondpage)
        self.screen_manager.add_widget(screen)

        self.thirdpage = Thirdpage()
        screen = Screen(name='third')
        screen.add_widget(self.thirdpage)
        self.screen_manager.add_widget(screen)

        self.fourthpage = Fourthpage()
        screen = Screen(name='fourth')
        screen.add_widget(self.fourthpage)
        self.screen_manager.add_widget(screen)

        self.fifthpage = Fifthpage()
        screen = Screen(name='fifth')
        screen.add_widget(self.fifthpage)
        self.screen_manager.add_widget(screen)

        self.sixthpage = Sixthpage()
        screen = Screen(name='sixth')
        screen.add_widget(self.sixthpage)
        self.screen_manager.add_widget(screen)

        self.seventhpage = Seventhpage()
        screen = Screen(name='seventh')
        screen.add_widget(self.seventhpage)
        self.screen_manager.add_widget(screen)

        self.eigthpage = Eigthpage()
        screen = Screen(name='eigth')
        screen.add_widget(self.eigthpage)
        self.screen_manager.add_widget(screen)

        self.ninthpage = Ninthpage()
        screen = Screen(name='ninth')
        screen.add_widget(self.ninthpage)
        self.screen_manager.add_widget(screen)

        self.tenthpage = Tenthpage()
        screen = Screen(name='tenth')
        screen.add_widget(self.tenthpage)
        self.screen_manager.add_widget(screen)

        self.eleventhpage = Eleventhpage()
        screen = Screen(name='eleventh')
        screen.add_widget(self.eleventhpage)
        self.screen_manager.add_widget(screen)

        Window.clearcolor="#75141B"
        return self.screen_manager
if __name__=='__main__':
    myapp = MyApp()
    myapp.run()




