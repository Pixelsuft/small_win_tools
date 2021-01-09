# Small Windows Tools
Python package for Windows<br />
[PyPi](https://pypi.org/project/small-win-tools/)
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
```MODAL``` - modal (appl, system)
# Bugs
Last symbol in message box doesn't displaying.
