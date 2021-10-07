#logan cruz
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    
    tilePos=mc.player.getTilePos()
    mc.setBlock(tilePos.x,tilePos.y-1,tilePos.z, 19)