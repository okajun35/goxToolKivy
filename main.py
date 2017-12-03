#-*- coding: utf-8 -*-


from kivy.config import Config
Config.set('graphics', 'height', '760')


import sys
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.listview import ListItemButton
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.uix.popup import Popup

# デフォルトに使用するフォントを変更する
resource_add_path('./fonts')
#resource_add_path('/storage/emulated/0/kivy/calc/fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


class MyPopup(Popup):
    pass

class RegistrationRoot(BoxLayout):
    ws =''
    sec_ley = ''
    tx_hash = ''

    def __init__(self, **kwargs):

        super(RegistrationRoot, self).__init__(**kwargs)
        

    def openPopup(self,input_title,input_text):
        '''処理結果をポップアップで表示する 
        '''
    
        popup = MyPopup()
        
        #popup.title = input_title
        popup.message_output.text = input_text

        # ポップアップ表示
        popup.open()

        
    def regist_done(self):   
        ''' 登録ボタンを押したときの状態 '''
      
        errorcode = 0
        
        # twitter
        self.ws = self.twitter.text

        # 秘密鍵
        self.sec_ley = self.secret_key.text
       
        # ハッシュ
        self.tx_hash = self.hush_exam.text
        print(self.tx_hash)

        # 処理部

        # 結果表示
        errorcode =1
        
        if errorcode == 0:
            self.openPopup('成功', '成功しました。\n接続を切断します。')
        elif errorcode == 1:
            self.openPopup('Error', '正しい形式の秘密鍵ではありません。\n空白などが混在していませんか？')
        elif errorcode == 2:
            self.openPopup('エラー ', '正しい形式のハッシュではありません。\n空白などが混在していませんか？')
        else:
            self.openPopup('エラー ', 'そのほか')
        
        
    def clear_done(self):   
        ''' 入力項目をクリアする '''
        print('All CLEAR')
        self.twitter.text = ''
        self.secret_key.text = ''
        self.hush_exam.text = ''




class GoxToolApp(App):

    def __init__(self, **kwargs):
        super(GoxToolApp, self).__init__(**kwargs)

        self.title = '送金GOX対応ツール'
    pass


def resourcePath():
    '''Returns path containing content - either locally or in pyinstaller tmp file'''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)

    return os.path.join(os.path.abspath("."))

def main():
    resource_add_path(resourcePath())
    GoxToolApp().run()


if __name__ == '__main__':
	main()
