#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的贪吃蛇游戏
使用方向键控制蛇的移动，吃到食物后蛇会变长，撞到自己游戏结束
蛇可以穿墙（从边界一侧出去会从另一侧进入）
"""

import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏配置
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)

# 方向定义
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self):
        """初始化蛇"""
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        """获取蛇头位置"""
        return self.positions[0]

    def update(self):
        """更新蛇的位置"""
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + x) % GRID_WIDTH, (cur[1] + y) % GRID_HEIGHT)
        
        # 检查是否撞到自己
        if len(self.positions) > 2 and new in self.positions[2:]:
            return False
        
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        
        return True

    def reset(self):
        """重置蛇"""
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def render(self, surface):
        """绘制蛇"""
        for i, p in enumerate(self.positions):
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), 
                          (GRID_SIZE, GRID_SIZE))
            # 蛇头颜色深一些
            if i == 0:
                pygame.draw.rect(surface, (0, 200, 0), r)
            else:
                pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)


class Food:
    def __init__(self):
        """初始化食物"""
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self, snake_positions=None):
        """随机生成食物位置，避免生成在蛇身上"""
        self.position = (random.randint(0, GRID_WIDTH - 1),
                        random.randint(0, GRID_HEIGHT - 1))
        if snake_positions:
            while self.position in snake_positions:
                self.position = (random.randint(0, GRID_WIDTH - 1),
                                random.randint(0, GRID_HEIGHT - 1))

    def render(self, surface):
        """绘制食物"""
        r = pygame.Rect((self.position[0] * GRID_SIZE, 
                        self.position[1] * GRID_SIZE), 
                       (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)


def draw_grid(surface):
    """绘制网格"""
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, (40, 40, 40), rect, 1)


def main():
    """主游戏循环"""
    # 设置窗口
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    
    clock = pygame.time.Clock()
    
    # 使用内置的默认字体（支持基本ASCII字符）
    font = pygame.font.Font(None, 36)  # 标题字体，较大
    font_score = pygame.font.Font(None, 28)  # 分数字体，较小
    
    # 创建游戏对象
    snake = Snake()
    food = Food()
    
    running = True
    game_over = False
    
    while running:
        clock.tick(10)  # 控制游戏速度
        
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    # 游戏结束后按空格键重新开始
                    if event.key == pygame.K_SPACE:
                        snake.reset()
                        food.randomize_position(snake.positions)
                        game_over = False
                else:
                    # 控制方向（不能直接反向）
                    if event.key == pygame.K_UP and snake.direction != DOWN:
                        snake.direction = UP
                    elif event.key == pygame.K_DOWN and snake.direction != UP:
                        snake.direction = DOWN
                    elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                        snake.direction = LEFT
                    elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                        snake.direction = RIGHT
        
        if not game_over:
            # 更新蛇的位置
            if not snake.update():
                game_over = True
            
            # 检查是否吃到食物
            if snake.get_head_position() == food.position:
                snake.length += 1
                snake.score += 10
                food.randomize_position(snake.positions)
        
        # 绘制游戏
        screen.fill(BLACK)
        draw_grid(screen)
        snake.render(screen)
        food.render(screen)
        
        # 显示分数
        score_text = font_score.render(f'Score: {snake.score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # 游戏结束提示
        if game_over:
            # 添加半透明背景
            s = pygame.Surface((WINDOW_WIDTH, 100))
            s.set_alpha(220)
            s.fill(BLACK)
            screen.blit(s, (0, WINDOW_HEIGHT // 2 - 50))
            
            # 游戏结束文字
            game_over_text = font.render('GAME OVER!', True, RED)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, 
                                                        WINDOW_HEIGHT // 2 - 20))
            screen.blit(game_over_text, text_rect)
            
            # 重新开始提示
            restart_text = font_score.render('Press SPACE to restart', True, WHITE)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, 
                                                         WINDOW_HEIGHT // 2 + 20))
            screen.blit(restart_text, restart_rect)
        
        pygame.display.update()
    
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
