import math
import os
import random
import sys
import time
import pygame as pg


WIDTH = 1100  # ゲームウィンドウの幅
HEIGHT = 650  # ゲームウィンドウの高さ
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Chat:
    """
    ゲーム画面に出力させる文字を出力
    """
    def __init__(self):
        pass
    def sent(self, massage):
        pass


class Event:
    """
    戦闘をするか宝箱を取るか選択する。
    どちらが出るかはランダム
    """
    def __init__(self):
        # 90% 戦闘のみ、10% 戦闘 + 宝箱
        self.mode = "battle_only" if random.random() < 0.9 else "battle_or_treasure"

    def select(self):
        keys = pg.key.get_pressed()
        chat = Chat()

        # 90% 戦闘のみ
        if self.mode == "battle_only":
            chat.sent("戦闘: F")
            if keys[pg.K_f]:
                return "battle_myTurn"
            return "select_action"

        # 10% 戦闘 + 宝箱
        else:
            chat.sent("戦闘: F   宝箱: T")
            if keys[pg.K_f]:
                return "battle_myTurn"
            if keys[pg.K_t]:
                return "treasure_chest"
            return "select_action"
        

class Player:
    def __init__(self):
        pass
    def action():
        pass
    def winBounus():
        pass

class Enemy:
    def __init__(self):
        pass
    def apper():
        pass
    def action():
        pass


def main():
    pg.display.set_caption("ゲーム")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load(f"IMG_2090.jpg")
    scene = "null"
    stage = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        
        if scene == "start":
            continue
        elif scene == "battle_myTurn":
            Player.action()
            scene = Player.finishScene()
        elif scene == "battle_enemyTurn":
            Enemy.apper()
            Enemy.action()
        elif scene == "finish_battle":
            Player.winBounus()
            event = Event()
            scene = "select_action"
        elif scene == "select_action":
            scene = event.select()
        elif scene == "finish":
            continue

        
        screen.blit(bg_img, [0, 0])
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()