import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()
        #使飞船对象拥有screen属性
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')
        #飞船的外接矩形
        self.rect = self.image.get_rect()
        #屏幕的外接矩形
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        # 飞船中心点横坐标x=窗口中心横坐标x
        self.rect.centerx = self.screen_rect.centerx
        # 飞船举行底部纵坐标y =
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    """根据移动标志调整飞船的位置"""
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
    #让飞船在屏幕上居中
    def center_ship(self):
        self.center = self.screen_rect.centerx