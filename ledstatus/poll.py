import subprocess

import color
import sender


SENDER = sender.start_sender()


def grep(pattern, text):
    matches = []
    for line in text.splitlines():
        if pattern in line:
            matches.append(line)
    return matches


def make():
    bits = []

    try:
        out = subprocess.check_output(
                'cd .. && make all --keep-going',
                shell=True,
                stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        out = e.output

    for match in grep('LED-Bit unlocked:', out.decode('utf-8')):
        bits.append(int(match.strip()[-1]))

    print('Unlocked Bits:' + str(bits))
    return bits


def pull():
    subprocess.call(['git', 'pull'])


def loop():
    while True:
        pull()

        num = 0
        for bit in make():
            num |= 1 << bit

        for thresh, red, green in [(16, 255, 0), (32, 200, 50), (64, 150, 100), (128, 100, 150), (255, 50, 200)]:
            if num < thresh:
                col = color.Color(red, green, 0)
                break
        else:
            col = color.Color(0, 255, 0)

        print(num, col)

        SENDER.send(col)


try:
    loop()
except KeyboardInterrupt:
    pass
