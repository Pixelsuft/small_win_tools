# Small Windows Tools
# By Pixelsuft
from os import system as cmd_run
from os import name as system_type
from os import access as file_access_py
from os import F_OK as file_access_py_param

if not __name__=='__main__':
    if system_type=='nt':
        if not file_access_py('play_sound.exe',file_access_py_param):
            from urllib.request import urlretrieve as download
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/file_exists.exe','file_exists.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/get_cursor.exe','get_cursor.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/get_height.exe','get_height.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/get_width.exe','get_width.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/message_box.exe','message_box.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/play_sound.exe','play_sound.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/set_size.exe','set_size.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/set_title.exe','set_title.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/show_message.exe','show_message.exe')
            download('https://github.com/Pixelsuft/small_win_tools/raw/main/system.exe','system.exe')
        from urllib.request import urlretrieve as download
        def file_exists(file_name):
            file_name_str=str(file_name).replace('"','').replace("'","")
            result=int(cmd_run('file_exists.exe "'+file_name_str+'"'))
            if result==0:
                return True
            else:
                return False
        
        
        def system(command):
            command_str=str(command).replace('"','').replace("'","")
            result=int(cmd_run('system.exe "'+command_str+'"'))
            return result
        
        
        def play_sound(file_name, snd_async=False, snd_loop=False):
            file_name_str=str(file_name).replace('"','').replace("'","")
            for_run=0
            if snd_async==True:
                for_run=1
            #if snd_loop==True:
            #    for_run2=1
            #result=int(cmd_run('play_sound.exe "'+file_name_str+'" '+str(for_run1)+' '+str(for_run2)))
            if snd_loop==True:
                while True:
                    result=int(cmd_run('play_sound.exe "'+file_name_str+'" '+str(for_run)+' 0'))
            else:
                result=int(cmd_run('play_sound.exe "'+file_name_str+'" '+str(for_run)+' 0'))
            return result
        
        
        def show_message(msg):
            msg_str=str(msg).replace('"','').replace("'","")
            result=int(cmd_run('show_message.exe "'+msg_str+'"'))
            return result
        
        
        def set_title(new_title):
            new_title_str=str(new_title).replace('"','').replace("'","")
            result=int(cmd_run('set_title.exe "'+new_title_str+'"'))
            if result==0:
                return True
            else:
                return False
        
        
        def get_cursor():
            result=int(cmd_run('get_cursor.exe'))
            return result
        
        
        def get_width():
            result=int(cmd_run('get_width.exe'))
            return result
        
        
        def get_height():
            result=int(cmd_run('get_height.exe'))
            return result
        
        
        def get_screen_size():
            return get_width(), get_height()
        
        
        def set_screen_size(new_width, new_height):
            new_width_int=0
            new_height_int=0
            try:
                new_width_int=int(new_width)
                new_height_int=int(new_height)
            except ValueError:
                return ValueError
            result=int(cmd_run('set_size.exe '+str(new_width_int)+' '+str(new_height_int)))
            if result==0:
                return True
            else:
                return False
        
        
        def message_box(title,msg,mb_icon='information',mb_buttons='ok',mb_defbutton=1,mb_modal='appl'):
            result=0
            title_str=str(title).replace('"','').replace("'","")
            msg_str=str(msg).replace('"','').replace("'","").replace('\n','\\n')
            icon=0
            if mb_icon=='warning':
                icon=1
            elif mb_icon=='question':
                icon=2
            elif mb_icon=='error':
                icon=3
            mod_int=0
            if mb_modal=='system':
                mod_int=1
            btn=0
            if mb_buttons=='ok':
                btn=1
            elif mb_buttons=='okcancel':
                btn=2
            elif mb_buttons=='retrycancel':
                btn=3
            elif mb_buttons=='yesno':
                btn=4
            elif mb_buttons=='yesnocancel':
                btn=5
            result=int(cmd_run('message_box.exe '+str(title_str)+' '+str(msg_str)+' '+str(icon)+' '+str(btn)+' '+str(mb_defbutton-1)+' '+str(mod_int)))
            result_str='error'
            if result==6:
                result_str='yes'
            elif result==7:
                result_str='no'
            elif result==2:
                result_str='cancel'
            elif result==1:
                result_str='ok'
            elif result==4:
                result_str='retry'
            elif result==5:
                result_str='skip'
            elif result==3:
                result_str='abort'
            return result_str
    else:
        print('Small Windows Tools module works only in windows, not in '+str(system_type)+'!')

else:
    print('Small Windows Tools is Module!')
    input('Press enter to continue')