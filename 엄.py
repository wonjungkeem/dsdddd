import pygame
import sys
from IPython.display import clear_output
import random

# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (50, 50, 50)

aa = input("바둑판 파일 : (파일이 없다면 '실행' 입력)")
# 나무 질감 이미지 불러오기
if aa == '실행':
    WOOD_TEXTURE = pygame.image.load('wood_texture.jpg')
# Pygame 설정
pygame.init()

# 설정 변수
CELL_SIZE = 40
BOARD_SIZE = 15
screen = pygame.display.set_mode((CELL_SIZE * BOARD_SIZE, CELL_SIZE * BOARD_SIZE))
pygame.display.set_caption("준성이의 준성이이")

# 나무 질감 이미지 크기 조정
WOOD_TEXTURE = pygame.transform.scale(WOOD_TEXTURE, (CELL_SIZE * BOARD_SIZE, CELL_SIZE * BOARD_SIZE))

class board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.array = [['+' for col in range(w)] for row in range(h)]
    
    def printf(self):
        for i in range(self.h):
            print("  ".join(self.array[i]))
    
    def xy(self, x, y):
        self.array[y-1][x-1] = '●'
    
    def xyz(self, x, y):
        self.array[y-1][x-1] = '○'
    
    def count_check(self):
        for f in range(15):
            for i in range(11):
                if self.array[f][i] == '○':
                    count = 0
                    for j in range(5):
                        if self.array[f][i+j] == '○':
                            count += 1
                    if count == 5:
                        return False
            for i in range(11):
                if self.array[i][f] == '○':
                    count = 0
                    for j in range(5):
                        if self.array[i+j][f] == '○':
                            count += 1
                    if count == 5:
                        return False
        for y in range(11):
            for x in range(11):
                if self.array[y][x] == '○':
                    count = 0
                    for j in range(5):
                        if self.array[y+j][x+j] == '○':
                            count += 1
                    if count == 5:
                        return False
        for y in range(11):
            for x in range(4, 15):
                if self.array[y][x] == '○':
                    count = 0
                    for j in range(5):
                        if self.array[y+j][x-j] == '○':
                            count += 1
                    if count == 5:
                        return False
        
        return True
    
    def count_check2(self):
        for f in range(15):
            for i in range(11):
                if self.array[f][i] == '●':
                    count = 0
                    for j in range(5):
                        if self.array[f][i+j] == '●':
                            count += 1
                    if count == 5:
                        return False
            for i in range(11):
                if self.array[i][f] == '●':
                    count = 0
                    for j in range(5):
                        if self.array[i+j][f] == '●':
                            count += 1
                    if count == 5:
                        return False
        for y in range(11):
            for x in range(11):
                if self.array[y][x] == '●':
                    count = 0
                    for j in range(5):
                        if self.array[y+j][x+j] == '●':
                            count += 1
                    if count == 5:
                        return False
        for y in range(11):
            for x in range(4, 15):
                if self.array[y][x] == '●':
                    count = 0
                    for j in range(5):
                        if self.array[y+j][x-j] == '●':
                            count += 1
                    if count == 5:
                        return False
        
        return True
    
print("● : 흑, ○ : 백")

# 보드 객체
p = board(15, 15)

# 마우스 클릭 좌표를 보드 상에 맞추는 함수
def get_cell_from_mouse(mouse_pos):
    return mouse_pos[0] // CELL_SIZE, mouse_pos[1] // CELL_SIZE

# 게임 루프
current_turn = '○'  # 백이 시작



while True:
    # 나무 질감을 배경으로 설정 (이미지를 화면 크기에 맞게 조정)
    screen.blit(WOOD_TEXTURE, (0, 0))  # 화면에 나무 질감 이미지 출력

    # 그리드 그리기
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            pygame.draw.rect(screen, GRID_COLOR, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            if p.array[y][x] == '○':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
            elif p.array[y][x] == '●':
                pygame.draw.circle(screen, BLACK, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            x, y = get_cell_from_mouse(mouse_pos)

            # 턴에 맞게 돌을 놓음
            if current_turn == '●' and p.array[y][x] == '+': #흑
                bb = random.randrange(1,4)
                bbb = input("가위 바위 보 :")
                if bb == 1:
                    print("가위!")
                    if bbb == '가위': 
                        pygame.display.set_caption("비김 ㅋ")
                        current_turn = '○'
                    if bbb == '바위':
                        pygame.display.set_caption("이김")
                        p.xyz(x + 1, y + 1)
                        current_turn = '○'
                    if bbb == '보':
                        pygame.display.set_caption("짐 ㅋ")
                        p.xy(x + 1, y + 1)
                        current_turn = '○'
                if bb == 2:
                    print("바위!")
                    if bbb == '바위': 
                        pygame.display.set_caption("비김 ㅋ")
                        current_turn = '○'
                    if bbb == '보':
                        pygame.display.set_caption("이김")
                        p.xyz(x + 1, y + 1)
                        current_turn = '○'
                    if bbb == '가위':
                        pygame.display.set_caption("짐 ㅋ")
                        p.xy(x + 1, y + 1)
                        current_turn = '○'
                    
                if bb == 3:
                    print("보!")
                    if bbb == '보': 
                        pygame.display.set_caption("비김 ㅋ")
                        current_turn = '○'
                    if bbb == '가위':
                        pygame.display.set_caption("이김")
                        p.xyz(x + 1, y + 1)
                        current_turn = '○'
                    if bbb == '바위':
                        pygame.display.set_caption("짐 ㅋ")
                        p.xy(x + 1, y + 1)
                        current_turn = '○'
            elif current_turn == '○' and p.array[y][x] == '+': #백
                bb = random.randrange(1,4)
                bbb = input("가위 바위 보 :")
                if bb == 1:
                    print("가위!")
                    if bbb == '가위': 
                        pygame.display.set_caption("비김 ㅋ")
                        current_turn = '●'
                    if bbb == '바위':
                        pygame.display.set_caption("이김")
                        p.xy(x + 1, y + 1)
                        current_turn = '●'
                    if bbb == '보':
                        pygame.display.set_caption("짐 ㅋ")
                        p.xyz(x + 1, y + 1)
                        current_turn = '●'
                if bb == 2:
                    print("바위!")
                    if bbb == '바위': 
                        pygame.display.set_caption("비김 ㅋ")
                        current_turn = '●'
                    if bbb == '보':
                        pygame.display.set_caption("이김")
                        p.xy(x + 1, y + 1)
                        current_turn = '●'
                    if bbb == '가위':
                        pygame.display.set_caption("짐 ㅋ")
                        p.xyz(x + 1, y + 1)
                        current_turn = '●'
                    
                if bb == 3:
                    print("보!")
                    if bbb == '보': 
                        pygame.display.set_caption("비김 ㅋ")
                        current_turn = '●'
                    if bbb == '가위':
                        pygame.display.set_caption("이김")
                        p.xy(x + 1, y + 1)
                        current_turn = '●'
                    if bbb == '바위':
                        pygame.display.set_caption("짐 ㅋ")
                        p.xyz(x + 1, y + 1)
                        current_turn = '●'

            clear_output()
            p.printf()

            # 승패 체크
            if p.count_check() == False:
                print("백돌 승")
                pygame.quit()
                sys.exit()

            if p.count_check2() == False:
                print("흑돌 승")
                pygame.quit()
                sys.exit()

    pygame.display.flip()
