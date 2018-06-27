# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['C:\\Users\\Josh\\PycharmProjects\\ITSupport\\pyinstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('icon.ico', 'C:\\Users\\Josh\\PycharmProjects\\ITSupport\\pyinstaller\\icon.ico', 'DATA'), 
           ('dds-logo3.png', 'C:\\Users\\Josh\\PycharmProjects\\ITSupport\\pyinstaller\\dds-logo3.png', 'DATA'),
           ('5qWKP09xSNPdW8pfFHLa.xml', 'C:\\Users\\Josh\\PycharmProjects\\ITSupport\\pyinstaller\\5qWKP09xSNPdW8pfFHLa.xml', 'DATA'),
           ('wifi.txt', 'C:\\Users\\Josh\\PycharmProjects\\ITSupport\\pyinstaller\\wifi.txt', 'DATA'),
           ('ra-check1.txt', 'C:\\Users\\Josh\\PycharmProjects\\ITSupport\\pyinstaller\\ra-check1.txt', 'DATA'),
           ('ra-check2.txt', 'C:\\Users\\Josh\\PycharmProjects\\ITSupport\\pyinstaller\\ra-check2.txt', 'DATA')
           ],
          name='run',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
	  icon='icon.ico')
