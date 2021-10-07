#logan cruz
#mc demo position
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos=mc.player.getPos()
mc.postToChat(pos)
mc.postToChat("your X position " + str(pos.x))
mc.postToChat("your Y position " + str(pos.y))
mc.postToChat("your Z position " + str(pos.z))