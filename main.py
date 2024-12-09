import sys
import random

description = "ユーザーは、この 2 つの数字を入力すると、プログラムが 最少数(n) から 最少数(m) の範囲内で乱数を生成します。\nその後、ユーザーは試行可能回数を超えるにか乱数を正しく推測するまで、ゲームループの中で繰り返し数字を入力することになります。\n"
sys.stdout.buffer.write(description.encode('utf-8'))

# 最少数
n = 0
# 最大数
m = 0
# 試行可能回数
lim = 0

# 最少数を要求する対話
while True:
    sys.stdout.buffer.write("\n".encode('utf-8'))
    sys.stdout.buffer.write("最少数を数字で入力してください(例: 4)\n".encode('utf-8'))
    sys.stdout.buffer.flush()

    nStr = sys.stdin.buffer.readline().decode()

    try:
        int(nStr)
    except ValueError:
        sys.stdout.buffer.write("入力されたのは数字ではないようです\n".encode('utf-8'))
        sys.stdout.buffer.flush()
        continue
    else:
        n = int(nStr)
        sys.stdout.buffer.write(f'最少数に{n}が設定されました\n'.encode('utf-8'))
        break


# 最大数を要求する対話
while True:
    sys.stdout.buffer.write("\n".encode('utf-8'))
    sys.stdout.buffer.write("最大数を数字で入力してください(例: 21)\n".encode('utf-8'))
    sys.stdout.buffer.flush()

    mStr = sys.stdin.buffer.readline().decode()

    try:
        int(mStr)
    except ValueError:
        sys.stdout.buffer.write("入力されたのは数字ではないようです\n".encode('utf-8'))
        sys.stdout.buffer.flush()
        continue
    else:
        m = int(mStr)
        sys.stdout.buffer.write(f"最大数に{m}が設定されました\n".encode('utf-8'))
        break

# 試行可能回数を要求する対話
while True:
    sys.stdout.buffer.write("\n".encode('utf-8'))
    sys.stdout.buffer.write("試行可能回数を数字で入力してください(例: 10)\n".encode('utf-8'))
    sys.stdout.buffer.flush()

    limStr = sys.stdin.buffer.readline().decode()

    try:
        int(limStr)
    except ValueError:
        sys.stdout.buffer.write("入力されたのは数字ではないようです\n".encode('utf-8'))
        continue
    else:
        lim = int(limStr)
        sys.stdout.buffer.write(f"試行可能回数に{lim}が設定されました\n".encode('utf-8'))
        break

correct = random.randint(n, m)
curr = 1
while curr <= lim:
    sys.stdout.buffer.write("\n".encode('utf-8'))
    sys.stdout.buffer.write(f"残りの試行可能回数は{str(lim - (curr - 1))}回です\n".encode('utf-8'))
    sys.stdout.buffer.write("推測した数字をして入力してください\n".encode('utf-8'))
    if curr == lim : sys.stdout.buffer.write("これが最後の挑戦です...\n".encode('utf-8'))
    sys.stdout.buffer.flush()

    answer = sys.stdin.buffer.readline().decode()

    try:
        int(answer)
    except ValueError:
        sys.stdout.buffer.write("入力されたのは数字ではないようです\n".encode('utf-8'))
        continue

    if correct == int(answer) :
        sys.stdout.buffer.write("正解です！おめでとうございます！\n".encode('utf-8'))
        break
    else :
        sys.stdout.buffer.write("不正解です\n".encode('utf-8'))
        if curr == lim : sys.stdout.buffer.write("試行可能回数を超えました。ゲームは失敗です。\n".encode('utf-8'))
        curr += 1
        continue

sys.stdout.buffer.flush()



