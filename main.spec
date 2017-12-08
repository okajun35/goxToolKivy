# -*- mode: python -*-
from kivy.deps import sdl2, glew

block_cipher = None


a = Analysis(['main.py'],
             pathex=['.\\goxToolKivy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas+=[('goxtool.kv','.\\goxtool.kv',"DATA")]
a.datas+=[('mplus-2c-regular.ttf','.\\mplus-2c-regular.ttf',"DATA")]



pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='main')
