# -*- mode: python -*-

block_cipher = None


a = Analysis(['main1.py'],
             pathex=['D:\\User\\Jimmy_wei\\Jimmy_wei\\python_code\\skill_system\\2-Python\\1-python3\\8-Í¼Æ¬²Ù×÷\\3-tool'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main1',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
