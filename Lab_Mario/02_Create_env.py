# 02. create_env.py
# 게임 환경 생성
import retro

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1')
env.reset()
# AI가 게임에서 죽으면 게임 껐다가 킴 -> reset 이 그냥 껐다가 키는것 보다 빠름

print(env)