
def make(num:str) ->str:
    han = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    a = ['천', '백', '십', '']
    result = ''
    for i in range(len(num)):
        if num[i] != '0':
            if num[i] != '1':
                result += han[int(num[i])-1]
            result += a[i]
    return result
def divide(num:str) -> None:
    try:
        int(num)
    except ValueError:
        return '숫자가 아닙니다'
    isMinus = False
    if num[0] == '-':
        isMinus = True
        num = num[1:]
    a = ['', '만', '억', '조', '경', '해', '서', '양', '구', '간', '정', '재', '극', '항아사', '아승기', '나유타', '불가사의']
    result = ''
    while len(num)%4:
        num = '0' + num
    b = []
    for i in range(len(num)//4):
        b.append(num[4*i:4*(i+1)])
    for i in range(len(b)):
        result = make(b[-i-1]) + a[i] + result
    for i in range(len(a)-2):#bad algorithm..
        result = result.replace(a[i+1] + a[i+2], a[i+2])
    if isMinus:
        return '마이너스' + result
    else:
        return result

if __name__ == '__main__':
    num = input()
    print(divide(num))
