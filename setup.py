from setuptools import setup, find_packages
from urllib.request import urlretrieve as download


long_description = '''# Small Windows Tools
Python package for Windows<br />
[GitHub](https://github.com/Pixelsuft/small_win_tools)
# Functions
1) Get screen width and height<br />
2) Check file exists<br />
3) Get cursor<br />
4) Play WAV sound<br />
5) Run console commands<br />
6) Set screen size<br />
7) Set console title<br />
8) Show message<br />
9) Show message box
# How does it work?
I compiled programs written on C++<br />
Python contact with C++ using command line arguments<br />
And gets result using return code
# Small Documentation
```import small_win_tools as tools``` - Import<br />
```tools.file_exists('document.txt')``` - Returns true if file exists<br />
```tools.play_sound('FileName.wav',snd_async=False, snd_loop=False)``` - Plays (only WAV!) sound<br />
```tools.system('color 0a')``` - Run command ```color 0a```<br />
```tools.get_screen_size()``` - Returns screen size (```tools.get_width()```,```tools.get_height()```)<br />
```tools.set_title('new title')``` -  Set console title<br />
```tools.show_message('text')``` - Show simple message (without \n, title, custom buttons and icons)<br />
Message Box:<br />
```tools.message_box('Title','Text', mb_icon=ICON, mb_buttons=BUTTONS, mb_defbutton=DEFAULT_BUTTON, mb_modal=MODAL)``` - Returns pressed button<br />
```ICON``` - icon (information, warning, error, question)<br />
```BUTTONS``` - buttons (ok, okcancel, retrycancel, abortretrycancel, yesno, yesnocancel)<br />
```DEFAULT_BUTTON``` - default button (1, 2, 3, 4)<br />
```MODAL``` - modal (appl, system)'''

setup(
    name="small_win_tools",
    version="0.0.5",
    author="Pixelsuft",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pixelsuft/small_win_tools/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.5',
    license='MIT', 
    keywords='small_win_tools',
    install_requires=[''],
    py_modules=["small_win_tools","urllib"]
)
'''download('https://github.com/Pixelsuft/small_win_tools/raw/main/file_exists.exe','file_exists.exe')
download('https://raw.githubusercontent.com/Pixelsuft/small_win_tools/main/__init__.py','__init__.py')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/get_cursor.exe','get_cursor.exe')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/get_height.exe','get_height.exe')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/get_width.exe','get_width.exe')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/message_box.exe','message_box.exe')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/play_sound.exe','play_sound.exe')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/set_size.exe','set_size.exe')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/set_title.exe','set_title.exe')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/show_message.exe','show_message.exe')
download('https://github.com/Pixelsuft/small_win_tools/raw/main/system.exe','system.exe')'''