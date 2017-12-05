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

from tipnem import WebSocketClient
from ed25519 import Ed25519

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
        
        popup.title = input_title
        popup.message_output.text = str(input_text)

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
        ws = WebSocketClient(url="ws://153.122.86.46:8088")

        output_maseege = ''

        ws.start()
        try:
            ws.login_by_pin_guest(screen = self.ws)
        except Exception as e:
            print("Error:%s" % e)
            output_maseege = e
            errorcode = 3
        
        print(" make secret key ")
        if(errorcode == 0):
            self.sec_ley = sec_ley.lower().lstrip().rstrip()
            if len(self.sec_ley) != 64:
                #print("Error:正しい形式の秘密鍵ではありません。空白などが混在していませんか？")
                errorcode = 1

        if(errorcode == 0):
            try:
                int(self.sec_ley, 16)
            except Exception as e:
                #print("Error:%s" % e)
                errorcode = 3
                output_maseege = e


        if(errorcode == 0):
            print("４、署名を作成します。")
            message = ws.user_code + self.tx_hash
            ecc = Ed25519()
            pub_key = ecc.public_key(sk=self.sec_ley).decode()
            sign = Ed25519.sign(message=message, secret_key=self.sec_ley, public_key=pub_key).decode()

            print("４、秘密鍵を削除します。")
            del self.sec_ley
            del ecc

            data = {
                'txhash': tx_hash,
                'sign': sign,
                'pubkey': pub_key
            }
            ok, result = ws.request(command="nem/lost", data=data)
            if not ok:
                errorcode = 4
                print("""
                ５、失敗しました。
                REASON: %s""" % result)

            else:
                print("""
                ５、成功しました。
                接続を切断します。""")
                

        # 結果表示
        if errorcode == 0:
            self.openPopup('成功', '成功しました。\n接続を切断します。')
        elif errorcode == 1:
            self.openPopup('Error', '正しい形式の秘密鍵ではありません。\n空白などが混在していませんか？')
        elif errorcode == 2:
            self.openPopup('エラー ', '正しい形式のハッシュではありません。\n空白などが混在していませんか？')
        elif errorcode == 3:
            self.openPopup('エラー ', output_maseege)
        elif errorcode == 4:
            self.openPopup('失敗しました ', result)

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
