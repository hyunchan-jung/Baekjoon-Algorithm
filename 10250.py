T = int(input())
room = []
for i in range(T):
    H, W, N = map(int, input().split(' '))
    if H == 1:
        floor = str(1)
        room_num = str(N)
    elif N%H==0:
        floor = str(H)
        room_num = str(N//H)
    else:
        floor = str(N%H)
        room_num = str(N//H+1)
    if len(room_num)==1: room_num = '0'+room_num
    room.append(floor+room_num)
[print(i) for i in room]