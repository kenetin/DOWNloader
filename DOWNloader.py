from cx_Freeze import setup, Executable

setup(name = 'DOWNloader',
      version = '0.1',
      executables = [Executable('youtube-downloader.py')])
