# step 2 - add 1
import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
# step 1 - add 1
# 地面
ground = Entity(model='plane',scale=60,texture='white_cube',texture_scale=(60,60),color=color.light_gray,collider='box')
# step 1 - add 2
# プレイヤー
player = FirstPersonController()
# Step 2 - add 2
# 敵
enemies = []
for i in range(8):
    enemy = Entity(model='sphere',color=color.blue,scale=2,collider='box',position=(random.randint(-20,20),0.75,random.randint(10,25)))
    enemies.append(enemy)
# step 3 - add 1
score = 0
score_text = Text(text='Score: 0',position=(-0.85,0.45),scale=2)
# step 3 - add 2
def input (key):
    global score
    if key == 'left mouse down':
        if mouse.hovered_entity in enemies:
            enemy = mouse.hovered_entity
            enemies.remove(enemy)
            destroy(enemy)
            score += 1
            score_text.text = 'Score: '+str(score)
# step 4 - add 1
def update():
    for enemy in enemies:
        enemy.look_at_2d(player.position,'y')
        enemy.position += enemy.forward * time.dt
# step 1 - add 3
# 空
Sky()
app.run()