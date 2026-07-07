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
        pass
    def select():
        pass

class Player:
    """
    プレイヤーキャラクターを管理するクラス
    """
    def __init__(self, hp=100, atk=20):
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.is_defending = False
        self.is_buffed = False

    def action(self, enemy, command):
        """
        プレイヤーの行動処理
        command: 1(攻撃), 2(防御), 3(自己強化)
        """
        self.is_defending = False

        if command == 1:
            return self._attack(enemy)
        elif command == 2:
            return self._defend()
        elif command == 3:
            return self._buff()
        else:
            Chat.sent("無効なコマンドです。")
            return

    def _attack(self, enemy):
        Chat.sent("プレイヤーの攻撃！")

        # 乱数によるダメージ変動（0.8倍〜1.2倍のブレ）
        variance = random.uniform(0.8, 1.2)
        dmg = int(self.atk * variance)

        if self.is_buffed:
            dmg = int(dmg * 2.5)
            self.is_buffed = False
            Chat.sent(f"自己強化によりダメージが {dmg} にアップ！")

        result = enemy.attacked(dmg)
        return result

    def _defend(self):
        Chat.sent("プレイヤーは防御の態勢をとった！")
        self.is_defending = True
        return

    def _buff(self):
        Chat.sent("プレイヤーは力を溜めている…！次の攻撃力が2.5倍！")
        self.is_buffed = True
        return

    def take_damage(self, dmg):
        """
        敵から攻撃を受ける際の処理
        """
        if self.is_defending:
            dmg = int(dmg * 0.5)
            Chat.sent("防御によりダメージを半減した！")

        self.hp -= dmg
        Chat.sent(f"プレイヤーに {dmg} ダメージ！ 残りHP:{self.hp}")

        if self.hp <= 0:
            Chat.sent("プレイヤーは倒れた…")
            return
        return


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
        elif scene == "select_action":
            Event.select()
        elif scene == "finish":
            continue

        
        screen.blit(bg_img, [0, 0])
        pg.display.update()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

