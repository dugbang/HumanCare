
import time


CONTROL_BLOCK = {
    1: '시작하기',
    2: '종료하기',
    3: '취소하기',
    4: '다음페이지',
    5: '이전페이지',
    6: '캐릭터',
    7: '튜토리얼',

    11: '사용자1',
    12: '사용자2',
    13: '사용자3',
    14: '사용자4',
    15: '사용자5',
}

ALPHABAT_BLOCK = {
    51: 'A',
    52: 'B',
    53: 'C',
    54: 'D',
    55: 'E',
    56: 'F',
    57: 'G',
    58: 'H',
    59: 'I',
    60: 'J',
    61: 'K',
    62: 'L',
    63: 'M',
    64: 'N',
    65: 'O',
    66: 'P',
    67: 'Q',
    68: 'R',
    69: 'S',
    70: 'T',
    71: 'U',
    72: 'V',
    73: 'W',
    74: 'X',
    75: 'Y',
    76: 'Z',
}

FIGURE_BLOCK = {
    81: '삼각형',
    82: '사각형',
    83: '원',
    84: '별',
}

EMOTION_BLOCK = {
    101: '행복',
    102: '슬픔',
    103: '기쁨',
    104: '짜증',
    105: '외로움',
    106: '두려움',
    107: '쓸쓸함',
}

USING_ALPHABAT_BLOCK = ()


def map_display(using_map):
    out = []
    for k in using_map.keys():
        out.append(using_map[k])
        #print('{:2} > {}'.format(k, using_map[k]))

    print('map length; {}'.format(len(using_map)))
    return out



if __name__ == '__main__':
    t = time.time()

    record = []

    record += map_display(CONTROL_BLOCK)
    record += map_display(ALPHABAT_BLOCK)
    record += map_display(FIGURE_BLOCK)
    record += map_display(EMOTION_BLOCK)

    col = 6
    #for r in record:
    #    print(r)
    st = 0
    end = col
    while end < len(record):
        print(record[st:end])
        st += col
        end += col

    print(record[st:end])
    #print(record[0:6])
    #print('block length; {}'.format(len(record)))


    #process_time = (timeit.default_timer() - t)    # 신규 CPU 에서 오류는 없는가?
    process_time = (time.time() - t)
    tm = time.localtime()
    if process_time < 100:
        print(__file__, 'Python Elapsed {:.02f} seconds, current time; {:02d}:{:02d}'.format(
            process_time, tm.tm_hour, tm.tm_min))
    else:
        print(__file__, 'Python Elapsed {:.02f} seconds, current time; {:02d}:{:02d}'.format(
            process_time / 60, tm.tm_hour, tm.tm_min))

