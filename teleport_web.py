from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
#x = 110
#y = 10
#z= 12
mc.player.setTilePos(x,y,z)
