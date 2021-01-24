import sys
import pygame
from Alien.settings import Settings
from Alien.ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "PLAY")
    pygame.display.set_caption('外星人入侵')
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船，创建一个用于存储子弹的编组，创建一个外星人
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship,aliens)
    # 开始游戏的主循环
    while 1:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            # 删除已消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
            # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, stats, sb,ship, aliens, bullets,
                         play_button)
run_game()
