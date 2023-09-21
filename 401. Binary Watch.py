turnedOn = 1


def readBinaryWatch(turnedOn: int):
    res = []
    for h in range(12):
        for m in range(60):
            if bin(h).count('1') + bin(m).count('1') == turnedOn:
                res.append(f'{h}:{m:02d}')
    return res

print(readBinaryWatch(turnedOn))