import random

'''
1)  хочу чтобы компютер рандомно выбирал клетку на поле после игрока и ходил туда
а)написать клетку
б)рандомно выбирать кто первый ходит
в)добавить очереди(игрок,комп,игрок...)
г)добавить концепцию хода
д)написать ии
е)вывод результа

'''
# print("[ ][ ][ ]\n[ ][ ][ ]\n[ ][ ][ ]")
karta = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"]

result = ""
valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
win_combos = [["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"], ["1", "5", "9"], ["3", "5", "7"]]
xmoves = []
omoves = []


def prosmotret():
    str1 = ""
    str2 = ""
    str3 = ""
    c = 9
    for kletka in karta:
        if c <= 9 and c > 6:
            str1 += kletka
            c -= 1
            
        elif c <= 6 and c > 3:
            str2 += kletka
            c -= 1
        elif c <= 3 and c > 0:
            str3 += kletka
            c -= 1

    print(str1)
    print(str2)
    print(str3)
    str1 = ""
    str2 = ""
    str3 = ""

def main():
    ...

def zherebyovka() -> int:
    return random.randrange(2)
     

def win_check(moves):
    for combo in win_combos:
        win_moves_count = 0
        for move in combo:
            if move in moves:
                win_moves_count += 1

            if win_moves_count == 3:
                return True
    return False

            

if zherebyovka() == 0:
    print("Move Player")
    while result != "Game Over":
        pl = input("Номер Клетки(1-9)")
        if pl not in valid_moves:
            print("Ход уже был")
            continue
        karta[int(pl) - 1] = "[X]"
        valid_moves.remove(pl)
        prosmotret()
        xmoves.append(pl)
        if win_check(xmoves) == True:
            result = "Game Over"
            print("Victory")
     
        print()
        pc = random.choice(valid_moves)
        karta[int(pc) - 1] = "[O]"
        valid_moves.remove(pc)
        prosmotret()
        print()
        omoves.append(pc)
        if win_check(omoves) == True:
                result = "Game Over"
                print("Defeat")

if zherebyovka() == 1:
    print("Move PC")
    while result != "Game Over":
        pc = random.choice(valid_moves)
        karta[int(pc) - 1] = "[X]"
        valid_moves.remove(pc)
        prosmotret()
        xmoves.append(pc)
        if win_check(xmoves) == True:
            result = "Game Over"
            print("Defeat")
        
        print()
        while True:
            pl = input("Номер Клетки(1-9)")
            if pl not in valid_moves:
                print("Ход уже был")
                continue
            break
        karta[int(pl) - 1] = "[O]"
        valid_moves.remove(pl)
        prosmotret()
        print()
        omoves.append(pl)
        if win_check(omoves) == True:
                result = "Game Over"
                print("Victory")