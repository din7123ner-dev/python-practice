# Ursina本体を読み込む
from ursina import *

from random import randint

# FPS（一人称視点）のプレイヤーを使うために読み込む
from ursina.prefabs.first_person_controller import FirstPersonController


# ==================================================
# ゲーム開始
# ==================================================

# Ursinaアプリを作成
app = Ursina()


# ==================================================
# 空を作る
# ==================================================

# 背景色を水色にする
window.color = Color(0.78,0.86,0.92,1)


# ==================================================
# 地面を作る
# ==================================================

ground = Entity(

    # model='plane' は平面
    # cubeより地面向き
    model='plane',

    # 地面を大きくする
    scale=100,

    # 緑色
    color=Color(0.75,0.83,0.6,1),

    # 当たり判定
    collider='mesh'
)

# ムシ Lv1 チョウ
class Butterfly(Entity):

    def __init__(self):
        super().__init__(
            model='sphere',
            color=color.yellow,
            scale=0.5,

            # ランダムスポーン
            position=(
                randint(-40, 40),
                randint(3, 8),
                randint(-40, 40)
            )
        )

        # 飛ぶ向きをランダムに決める
        self.direction_x = randint(-100, 100) / 100
        self.direction_z = randint(-100, 100) / 100
        #生成時刻を記録
        self.spawn_time = time.time()

    def update(self):

        # ゆっくり飛ぶ
        self.x += self.direction_x * 2 * time.dt
        self.z += self.direction_z * 2 * time.dt

        # ひらひら感
        self.y += sin(time.time() * 3) * 0.01

for z in range(-50,51,10):
    Entity(
        model = 'cube',
        color = Color(0.70,0.78,0.55,1),
        scale = (1,0.1,1),
        position=(0,0.05,z)
    )

#lv2 バッタ
class Grasshopper(Entity):

    def __init__(self):
        super().__init__(
            model='sphere',
            color=color.green,
            scale=0.7,
            position=(
                randint(-40, 40),
                0.5,
                randint(-40, 40)
            )
        )

        self.spawn_time = time.time()
        # 次のジャンプ時間
        self.next_jump = time.time() + 2
        
    def update(self):
        
            # 2秒ごとにジャンプ
            if time.time() >= self.next_jump:
        
                jump_x = self.x + randint(-10,10)
                jump_z = self.z + randint(-10,10)
                # 空中へ
                self.animate_y(3,duration=0.2)
                    # 前へ飛ぶ
                self.animate_x(jump_x,duration=0.5)
                self.animate_z(jump_z,duration=0.5)
                    # 着地
                self.animate_y(0.5,duration=0.3,delay=0.2)
                self.next_jump = time.time()+2


        
# lv3 トンボ
class Dragonfly(Entity):

    def __init__(self):
        super().__init__(
            model='sphere',
            color=color.cyan,
            scale=0.6,

            position=(
                randint(-40, 40),
                randint(4, 10),
                randint(-40, 40)
            )
        )

        self.spawn_time = time.time()

        # 飛行方向
        self.direction_x = randint(-100, 100) / 100
        self.direction_z = randint(-100, 100) / 100


    def update(self):

        # 蝶より速い
        self.x += self.direction_x * 5 * time.dt
        self.z += self.direction_z * 5 * time.dt

        # 高さを少し変化させる
        self.y += sin(time.time() * 5) * 0.01

# lv4 カマキリ
class Mantis(Entity):

    def __init__(self):
        super().__init__(
            model='cube',
            color=color.lime,
            scale=(1.5, 1.5, 1.5),

            position=(
                randint(-40, 40),
                0.75,
                randint(-40, 40)
            )
        )

        self.spawn_time = time.time()
    def update(self):
        # プレイヤーに近づかれたら逃げる
        if distance(player,self) < 5:
            self.animate_y(
                self.y + 3,
                duration = 0.2
            )
            destroy(self,delay = 0.2)
            if self in mantises:
                mantises.remove(self)
# lv5 オニヤンマ
class GiantDragonfly(Entity):

    def __init__(self):
        super().__init__(
            model='sphere',
            color=color.orange,
            scale=1.0,

            position=(
                randint(-40, 40),
                randint(5, 12),
                randint(-40, 40)
            )
        )

        self.spawn_time = time.time()

        self.direction_x = randint(-100, 100) / 100
        self.direction_z = randint(-100, 100) / 100

    def update(self):

        # トンボよりかなり速い
        self.x += self.direction_x * 12 * time.dt
        self.z += self.direction_z * 12 * time.dt

        self.y += sin(time.time() * 8) * 0.01

# ==================================================
# ライトを追加
# ==================================================

# 太陽のような光
DirectionalLight()


# ==================================================
# プレイヤー作成
# ==================================================

# プレイヤー本体（胴体）
player = Entity(
    model='cube',
    color=color.blue,
    scale=(1, 2, 0.8),
    position=(0, 1, 0)
)

# 頭
head = Entity(
    parent=player,
    model='sphere',
    color=color.peach,
    scale=0.7,
    position=(0, 0.8, 0)
)

# 網の柄
net_handle = Entity(
    parent=player,
    model='cube',
    color=color.brown,
    scale=(0.1, 1.5, 0.1),
    position=(0.7, 0.3, 0),
    rotation_z=-30
)

# 網の枠
net_ring = Entity(
    parent=player,
    model='cube',
    color=color.gray,
    scale=(0.8, 0.1, 0.8),
    position=(1.2, 1.0, 0),
    rotation_z=-30
)

#生成時間の調整
last_spawn_time = 0
last_grasshopper_spawn = 0
last_dragonfly_spawn = 0
last_mantis_spawn = 0
last_giant_dragonfly_spawn = 0
#生成リスト
butterflies = []
grasshoppers = []
dragonflies = []
mantises = []
giant_dragonflies = []
money = 0

# 地面に埋まらないよう少し上から開始
player.position = (0, 1, 0)
camera.rotation_x = 20

# キーでプレイヤーを移動
def update():
    
    global last_spawn_time
    global last_grasshopper_spawn
    global last_dragonfly_spawn
    global last_mantis_spawn
    global last_giant_dragonfly_spawn

    speed = 10 * time.dt
# Xキーを押している間は速度を2倍にする
    if held_keys['x']:
        speed = 20 * time.dt

    if held_keys['w']: 
        player.z += speed

    if held_keys['s']:
        player.z -= speed

    if held_keys['a']:
        player.x -= speed

    if held_keys['d']:
        player.x += speed
        
# カメラの視点を調整し　プレイヤーを追跡する
    #camera.position = (
    #    player.x,
    #    player.y + 70,
    #    player.z - 70
    #)
    #camera.look_at(player)
    
    #butterfly.update()
    camera.position = (0, 60, -60)
    camera.look_at(player)


# 10秒ごとに蝶を出現
    if time.time() - last_spawn_time >= 10:

        butterflies.append(
         Butterfly()
        )

        last_spawn_time = time.time()
    # バッタスポーン
    if time.time() - last_grasshopper_spawn >= 25:

        grasshoppers.append(
            Grasshopper()
        )


        last_grasshopper_spawn = time.time()
    # トンボスポーン
    if time.time() - last_dragonfly_spawn >= 40:

        dragonflies.append(
            Dragonfly()
        )

        last_dragonfly_spawn = time.time()
    # カマキリスポーン
    if time.time() - last_mantis_spawn >= 60:
        
        mantises.append(
            Mantis()
        )
        
        last_mantis_spawn = time.time()
    # オニヤンマスポーン
    if time.time() - last_giant_dragonfly_spawn >= 75:

        giant_dragonflies.append(
            GiantDragonfly()
        )

        last_giant_dragonfly_spawn = time.time()
        


# 蝶の更新と削除
    for butterfly in butterflies[:]:

        butterfly.update()

    # 30秒たったら消える
        if time.time() - butterfly.spawn_time >= 30:

            destroy(butterfly)
            butterflies.remove(butterfly)
            
    for grasshopper in grasshoppers[:]:

        grasshopper.update()

    # 50秒で消える
        if time.time() - grasshopper.spawn_time >= 50:

            destroy(grasshopper)
            grasshoppers.remove(grasshopper)
    
    for dragonfly in dragonflies[:]:

        dragonfly.update()

    # 80秒で消える
        if time.time() - dragonfly.spawn_time >= 80:

            destroy(dragonfly)
            dragonflies.remove(dragonfly)
        
    for mantis in mantises[:]:
        mantis.update()
    
    for giant_dragonfly in giant_dragonflies[:]:

        giant_dragonfly.update()

    # 60秒で消える
        if time.time() - giant_dragonfly.spawn_time >= 60:

            destroy(giant_dragonfly)
            giant_dragonflies.remove(giant_dragonfly)

def input(key):

    global money

    # Eキーを押したら
    if key == 'e':

        # 蝶一覧を調べる
        for butterfly in butterflies[:]:

            # プレイヤーとの距離を計算
            if distance(net_ring, butterfly) <= 10:

                # 報酬
                money += 100

                print(f"蝶を捕獲！ 所持金: {money}円")

                # 蝶を削除
                destroy(butterfly)
                butterflies.remove(butterfly)
        for grasshopper in grasshoppers[:]:

            if distance(net_ring, grasshopper) <= 8:

                money += 300

                print(f"バッタ捕獲！ 所持金: {money}円")

                destroy(grasshopper)
                grasshoppers.remove(grasshopper)
        for dragonfly in dragonflies[:]:

            if distance(net_ring, dragonfly) <= 8:

                money += 500

                print(f"トンボ捕獲！ 所持金: {money}円")

                destroy(dragonfly)
                dragonflies.remove(dragonfly)
        for mantis in mantises[:]:
            if distance(net_ring,mantis)<= 8:
                money += 1000
                print(f"カマキリ捕獲！ 所持金:{money}円")
                destroy(mantis)
                mantises.remove(mantis)
        for giant_dragonfly in giant_dragonflies[:]:

            if distance(net_ring, giant_dragonfly) <= 8:

                money += 3000

                print(f"オニヤンマ捕獲！ 所持金: {money}円")

                destroy(giant_dragonfly)
                giant_dragonflies.remove(giant_dragonfly)


# ==================================================
# ゲーム開始
# ==================================================

app.run()
