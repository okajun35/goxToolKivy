# -*- mode: python -*-
from kivy.deps import sdl2, glew

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\hddwm\\OneDrive\\ドキュメント\\GitHub\\goxToolKivy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas+=[('goxtool.kv','C:\\Users\\hddwm\\OneDrive\\ドキュメント\\GitHub\\goxToolKivy\\goxtool.kv',"DATA")]
a.datas+=[('mplus-2c-regular.ttf','C:\\Users\\hddwm\\OneDrive\\ドキュメント\\GitHub\\goxToolKivy\\mplus-2c-regular.ttf',"DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='goxtool',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True , icon='icon.ico')
          
coll = COLLECT(exe, Tree('.'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='test')