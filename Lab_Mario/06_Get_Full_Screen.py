# 06.get_full_screen
import retro
import numpy as np

env = retro.make(game='SuperMArioBros-Nes', state='Level1-1')
env.reset()

ram = env.get_ram()

# https://datacrystal.romhacking.net/wiki/Super_Mario_Bros.:RAM_map
# 0x0500-0x069F	Current tile (Does not effect graphics)
# ram[시작: 끝 + 1]
# [이상:미만] 이여서 +1 해줘야함
full_screen_tiles = ram[0x0500:0x069F+1]

print(full_screen_tiles.shape)
print(full_screen_tiles)

full_screen_tile_count = full_screen_tiles.shape[0]

# 정수여야 해서 / 2개
full_screen_page1_tile = full_screen_tiles[0:full_screen_tile_count//2].reshape((13, 16))
full_screen_page2_tile = full_screen_tiles[full_screen_tile_count//2:].reshape((13, 16))

full_screen_tiles = np.concatenate((full_screen_page1_tile, full_screen_page2_tile), axis=1).astype(np.int)

print(full_screen_tiles)

# Empty = 0x00
# Fake = 0x01
# Ground = 0x54
# Top_Pipe1 = 0x12
# Top_Pipe2 = 0x13
# Bottom_Pipe1 = 0x14
# Bottom_Pipe2 = 0x15
# Flagpole_Top =  0x24
# Flagpole = 0x25
# Coin_Block1 = 0xC0
# Coin_Block2 = 0xC1
# Coin = 0xC2
# Breakable_Block = 0x51