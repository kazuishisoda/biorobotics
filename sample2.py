import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# 画面の設定
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cabbage Harvesting Simulation")

# キャベツのクラス
class Cabbage(pygame.sprite.Sprite):
    def __init__(self, size):
        super().__init__()
        if size == 'S':
            self.image = pygame.image.load('s.png')  # 画像を読み込み
        elif size == 'M':
            self.image = pygame.image.load('m.png')  # 画像を読み込み
        else:
            self.image = pygame.image.load('l.png')  # 画像を読み込み
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(height - self.rect.height)
        self.size = size

# 収穫機のクラス
class Harvester(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('track.png')  # 収穫機の画像を読み込み
        self.rect = self.image.get_rect()
        self.rect.x = width 
        self.rect.y = height

# スプライトグループの作成
all_sprites = pygame.sprite.Group()
cabbages = pygame.sprite.Group()

# キャベツを生成してスプライトグループに追加
for _ in range(10):
    size = random.choice(['S', 'M', 'L'])
    cabbage = Cabbage(size)
    all_sprites.add(cabbage)
    cabbages.add(cabbage)

# 収穫機を生成してスプライトグループに追加
harvester = Harvester()
all_sprites.add(harvester)

# スコアトラッキング
score_S = 0
score_M = 0
score_L = 0
font = pygame.font.Font(None, 36)

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # "R"キーでスコアをリセット
                score_S = 0
                score_M = 0
                score_L = 0

    # 収穫機の位置をマウスに追従
    harvester.rect.center = pygame.mouse.get_pos()

    # キャベツと収穫機の当たり判定
    hits = pygame.sprite.spritecollide(harvester, cabbages, True)

    # スコアの更新
    for hit in hits:
        if hit.size == 'S':
            score_S += 1
        elif hit.size == 'M':
            score_M += 1
        else:
            score_L += 1

    # 新しいキャベツを生成してスプライトグループに追加
    for _ in range(len(hits)):
        size = random.choice(['S', 'M', 'L'])
        cabbage = Cabbage(size)
        all_sprites.add(cabbage)
        cabbages.add(cabbage)

    # 画面のクリア
    screen.fill((255, 255, 255))

    # すべてのスプライトを描画
    all_sprites.draw(screen)

    # スコアを表示
    score_text = font.render(f"S: {score_S}  M: {score_M}  L: {score_L}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # 画面の更新
    pygame.display.flip()

# Pygameの終了
pygame.quit()
sys.exit()
