# 10/27 更新にて　一旦発表　
# ad: 草の効果　虫を隠すようにもできる
# 要素増やしすぎないほうがいい

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
    model='plane',

    # 地面を大きくする
    scale=100,

    # 緑色
    color=Color(0.75,0.83,0.6,1),

    # 当たり判定
    collider='mesh'
)

# ==================================================
# 草を配置
# ==================================================

for i in range(250):

    x = randint(-48, 48)
    z = randint(-48, 48)

    # スタート地点周辺は空ける
    if abs(x) < 8 and abs(z) < 8:
        continue

    Entity(
        model='cube',

        # 草色
        color=Color(0.65,0.74,0.50,1),

        # 細長い草
        scale=(0.2, 1.2, 0.2),

        position=(
            x,
            0.6,
            z
        )
    )

# ムシ Lv1 チョウ
class Butterfly(Entity):

    def __init__(self):
        super().__init__(

            position=(
                randint(-40, 40),
                randint(3, 8),
                randint(-40, 40)
            )
        )

        # 胴体
        Entity(
            parent=self,
            model='cube',
            color=color.black,
            scale=(0.15, 0.5, 0.15)
        )

        # 左の羽
        Entity(
            parent=self,
            model='sphere',
            color=color.yellow,
            scale=(0.4, 0.3, 0.1),
            x=-0.25
        )

        # 右の羽
        Entity(
            parent=self,
            model='sphere',
            color=color.yellow,
            scale=(0.4, 0.3, 0.1),
            x=0.25
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

            position=(
                randint(-40, 40),
                0.5,
                randint(-40, 40)
            )
        )

        self.spawn_time = time.time()
        self.next_jump = time.time() + 2

        # 胴体
        Entity(
            parent=self,
            model='cube',
            color=color.green,
            scale=(0.8, 0.3, 1.2)
        )

        # 頭
        Entity(
            parent=self,
            model='sphere',
            color=color.green,
            scale=0.35,
            z=0.8
        )

        # 左後ろ足
        Entity(
            parent=self,
            model='cube',
            color=color.dark_gray,
            scale=(0.1, 0.6, 0.1),
            position=(-0.3, -0.2, -0.4),
            rotation_z=30
        )

        # 右後ろ足
        Entity(
            parent=self,
            model='cube',
            color=color.dark_gray,
            scale=(0.1, 0.6, 0.1),
            position=(0.3, -0.2, -0.4),
            rotation_z=-30
        )
        
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

            position=(
                randint(-40, 40),
                randint(4, 10),
                randint(-40, 40)
            )
        )

        self.spawn_time = time.time()

        self.direction_x = randint(-100, 100) / 100
        self.direction_z = randint(-100, 100) / 100

        # 頭
        Entity(
            parent=self,
            model='sphere',
            color=color.red,
            scale=0.25,
            z=0.35
        )

        # 胴体
        Entity(
            parent=self,
            model='cube',
            color=color.red,
            scale=(0.12, 0.12, 1.4)
        )

        # 左前羽
        Entity(
            parent=self,
            model='cube',
            color=color.white,
            scale=(0.8, 0.03, 0.2),
            position=(-0.45, 0, 0.2)
        )

        # 右前羽
        Entity(
            parent=self,
            model='cube',
            color=color.white,
            scale=(0.8, 0.03, 0.2),
            position=(0.45, 0, 0.2)
        )

        # 左後羽
        Entity(
            parent=self,
            model='cube',
            color=color.white,
            scale=(0.8, 0.03, 0.2),
            position=(-0.45, 0, -0.2)
        )

        # 右後羽
        Entity(
            parent=self,
            model='cube',
            color=color.white,
            scale=(0.8, 0.03, 0.2),
            position=(0.45, 0, -0.2)
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

            position=(
                randint(-40, 40),
                0.75,
                randint(-40, 40)
            )
        )

        self.spawn_time = time.time()

        # 胴体
        Entity(
            parent=self,
            model='cube',
            color=color.lime,
            scale=(0.5, 0.5, 1.5)
        )

        # 頭
        Entity(
            parent=self,
            model='sphere',
            color=color.lime,
            scale=0.45,
            z=0.9
        )

        # 左のカマ
        Entity(
            parent=self,
            model='cube',
            color=color.lime,
            scale=(0.12, 0.8, 0.12),
            position=(-0.35, 0.4, 0.5),
            rotation_z=35
        )

        # 右のカマ
        Entity(
            parent=self,
            model='cube',
            color=color.lime,
            scale=(0.12, 0.8, 0.12),
            position=(0.35, 0.4, 0.5),
            rotation_z=-35
        )

        # 左後ろ足
        Entity(
            parent=self,
            model='cube',
            color=color.green,
            scale=(0.1, 0.8, 0.1),
            position=(-0.4, -0.25, -0.3),
            rotation_z=25
        )

        # 右後ろ足
        Entity(
            parent=self,
            model='cube',
            color=color.green,
            scale=(0.1, 0.8, 0.1),
            position=(0.4, -0.25, -0.3),
            rotation_z=-25
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

            position=(
                randint(-40, 40),
                randint(5, 12),
                randint(-40, 40)
            )
        )

        self.spawn_time = time.time()

        self.direction_x = randint(-100, 100) / 100
        self.direction_z = randint(-100, 100) / 100

        # 頭
        Entity(
            parent=self,
            model='sphere',
            color=color.black,
            scale=0.35,
            z=0.5
        )

        # 胴体
        Entity(
            parent=self,
            model='cube',
            color=color.yellow,
            scale=(0.2, 0.2, 2.5)
        )

        # 尾の先
        Entity(
            parent=self,
            model='cube',
            color=color.black,
            scale=(0.18, 0.18, 1.2),
            z=-1.8
        )

        # 左前羽
        Entity(
            parent=self,
            model='cube',
            color=color.white,
            scale=(1.2, 0.03, 0.3),
            position=(-0.7, 0, 0.4)
        )

        # 右前羽
        Entity(
            parent=self,
            model='cube',
            color=color.white,
            scale=(1.2, 0.03, 0.3),
            position=(0.7, 0, 0.4)
        )

        # 左後羽
        Entity(
            parent=self,
            model='cube',
            color=color.white,
            scale=(1.2, 0.03, 0.3),
            position=(-0.7, 0, -0.4)
        )

        # 右後羽
        Entity(
            parent=self,
            model='cube',
            color=color.white,
            scale=(1.2, 0.03, 0.3),
            position=(0.7, 0, -0.4)
        )

        self.spawn_time = time.time()

        self.direction_x = randint(-100, 100) / 100
        self.direction_z = randint(-100, 100) / 100

    def update(self):

        # トンボよりかなり速い
        self.x += self.direction_x * 12 * time.dt
        self.z += self.direction_z * 12 * time.dt

        self.y += sin(time.time() * 8) * 0.01
        
        # フィールド端で反射
        if self.x > 50 or self.x < -50:
            self.direction_x *= -1

        if self.z > 50 or self.z < -50:
            self.direction_z *= -1

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
money_text = Text(
    text="Money: 0",
    position=(0.45, 0.45),
    scale=2,
    color=color.black
)
start_time = time.time()
# 制限時間
time_limit = 180
instruction_time = 10
game_started = False
start_delay = 5
countdown_text = Text(
    text="5",
    origin=(0,0),
    scale=5,
    color=color.red
)
# 終了判定
game_over = False
timer_text = Text(
    text="Time: 180",
    position=(0.45, 0.30),
    scale=2,
    color=color.black
)
finish_text = Text(
    text="FINISH!",
    origin=(0,0),
    scale=5,
    color=color.red,
    enabled=False
)
instruction_text = Text(
    text="Press WASD to move\nPress E to catch\nHold X to run",
    position=(0.0, 0.0),
    scale=1.5,
    color=color.black
)


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
    global game_over
    global game_started
    
    # 開始前のカウントダウン
    if not game_started:

        remaining = int(
            start_delay - (time.time() - start_time)
        ) + 1

        countdown_text.text = str(max(0, remaining))

        if time.time() - start_time >= start_delay:

            game_started = True
            countdown_text.enabled = False

        return
    
    # 残り時間を計算
    remaining_time = max(
        0,
        int(time_limit - (time.time() - start_time - start_delay))
    )
    timer_text.text = f"Time: {remaining_time}"
    # 操作説明を10秒後に消す
    if time.time() - start_time >= instruction_time:
        instruction_text.enabled = False
    
    if remaining_time <= 0 and not game_over:

        game_over = True

        finish_text.enabled = True

    if not game_over:
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
# フィールド外へ出られないようにする

    if player.x < -50:
        player.x = -50
    
    if player.x > 50:
        player.x = 50

    if player.z < -50:
        player.z = -50

    if player.z > 50:
        player.z = 50
        
# カメラの視点を調整し　プレイヤーを追跡する
    camera.position = (
        player.x,
        40,
        player.z - 30
    )
    camera.rotation_x = 45
    
    #butterfly.update()
    #camera.position = (0, 60, -60)
    #camera.look_at(player)


# 10秒ごとに蝶を出現
    if time.time() - last_spawn_time >= 10:

        butterflies.append(
         Butterfly()
        )

        last_spawn_time = time.time()
    # バッタスポーン
    if time.time() - last_grasshopper_spawn >= 20:

        grasshoppers.append(
            Grasshopper()
        )


        last_grasshopper_spawn = time.time()
    # トンボスポーン
    if time.time() - last_dragonfly_spawn >= 30:

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

    # 30秒で消える
        if time.time() - giant_dragonfly.spawn_time >= 30:

            destroy(giant_dragonfly)
            giant_dragonflies.remove(giant_dragonfly)

def input(key):

    global money
    
    if game_over:
        return

    # Eキーを押したら
    if key == 'e':

        # 蝶一覧を調べる
        for butterfly in butterflies[:]:

            # プレイヤーとの距離を計算
            if distance(net_ring, butterfly) <= 10:

                # 報酬
                money += 100

                print(f"蝶を捕獲！ 所持金: {money}円")
                money_text.text = f"Money: {money}"

                # 蝶を削除
                destroy(butterfly)
                butterflies.remove(butterfly)
        for grasshopper in grasshoppers[:]:

            if distance(net_ring, grasshopper) <= 8:

                money += 300

                print(f"バッタ捕獲！ 所持金: {money}円")
                money_text.text = f"Money: {money}"

                destroy(grasshopper)
                grasshoppers.remove(grasshopper)
        for dragonfly in dragonflies[:]:

            if distance(net_ring, dragonfly) <= 8:

                money += 500

                print(f"トンボ捕獲！ 所持金: {money}円")
                money_text.text = f"Money: {money}"

                destroy(dragonfly)
                dragonflies.remove(dragonfly)
        for mantis in mantises[:]:
            if distance(net_ring,mantis)<= 8:
                money += 1000
                print(f"カマキリ捕獲！ 所持金:{money}円")
                money_text.text = f"Money: {money}"
                destroy(mantis)
                mantises.remove(mantis)
        for giant_dragonfly in giant_dragonflies[:]:

            if distance(net_ring, giant_dragonfly) <= 8:

                money += 3000

                print(f"オニヤンマ捕獲！ 所持金: {money}円")
                money_text.text = f"Money: {money}"

                destroy(giant_dragonfly)
                giant_dragonflies.remove(giant_dragonfly)


# ==================================================
# ゲーム開始
# ==================================================

app.run()
