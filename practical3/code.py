n = int(input())
room = list(map(int, input().split()))
room_number=set(room)
for i in room_number:
     if room.count(i)==1:
         print(i)
