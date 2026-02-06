# 贪吃蛇游戏

一个使用Python和Pygame开发的简单贪吃蛇游戏。

## 游戏特点

- 🐍 经典贪吃蛇玩法
- 🎮 方向键控制
- 🍎 吃食物增加长度和分数
- 💀 撞到自己游戏结束
- 🔄 穿墙功能（从一边出来会从另一边进入）
- 📊 实时分数显示

## 安装依赖

首先创建并激活虚拟环境（推荐）：

```bash
python3 -m venv venv
source venv/bin/activate
```

然后安装依赖包（使用国内源加速）：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

或者直接安装pygame：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pygame
```

## 运行游戏

```bash
python3 snake_game.py
```

或者直接执行：

```bash
chmod +x snake_game.py
./snake_game.py
```

## 游戏操作

- **方向键**：控制蛇的移动方向（↑ ↓ ← →）
- **空格键**：游戏结束后重新开始
- **关闭窗口**：退出游戏

## 游戏规则

1. 使用方向键控制蛇的移动方向
2. 吃到红色食物后，蛇会变长，分数增加10分
3. 撞到自己游戏结束
4. 蛇可以穿墙（从边界一侧出去会从另一侧进入）

## 系统要求

- Python 3.6+
- macOS / Linux / Windows
- Pygame 2.x

## 技术栈

- Python 3
- Pygame
