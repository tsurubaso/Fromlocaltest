import bpy
import random
defs = bpy.data.texts["defs.py"].as_module()

#Toutes les variables
#le calcul des points des lamps
xl=10
yl=10
zl=10
#Data
x=0
y=0
z=0


#les groups that we will use later
meshgr=[]
emptygr=[]
lampgr=[]
cameragr=[]

#la camera
camera= bpy.context.scene.objects['Camera']
cameragr.append(camera)

#On cree l'Empty first
defs.makeEmpty((x,y,z))
emptygr.append(bpy.context.object)


#Le programme en lui meme
defs.addLamp((xl,yl,zl))
lampgr.append(bpy.context.object)
defs.targetobj(emptygr[0],bpy.context.object)
defs.addLamp((-xl,-yl,zl))
lampgr.append(bpy.context.object)
defs.targetobj(emptygr[0],bpy.context.object)
defs.addLamp((-xl,yl,-zl))
lampgr.append(bpy.context.object)
defs.targetobj(emptygr[0],bpy.context.object)
defs.addLamp((xl,-yl,-zl))
lampgr.append(bpy.context.object)
defs.targetobj(emptygr[0],bpy.context.object)




#Premier traveling La camera d'origine
bpy.ops.curve.primitive_bezier_circle_add(radius=15, enter_editmode=False, align='WORLD', location=(0, 0, 0))
path = bpy.context.object 
camera.select_set(True)
path.select_set(True)
bpy.context.view_layer.objects.active = path
bpy.ops.object.parent_set(type='FOLLOW') #follow paths
bpy.context.object.data.path_duration = 1100

#deux autres travelings
cameraNew=defs.cameraTravelingSimpleShp(10.0,0.0, 9.0)
defs.targetobj(emptygr[0],cameraNew)
cameragr.append(bpy.context.object)
cameraNew=defs.cameraTravelingSimpleShp(5.0,0.0, 10.0)
defs.targetobj(emptygr[0],cameraNew)
cameragr.append(bpy.context.object)

#Ajout de cameras
cameraNew=defs.addCameraShp(-xl,-yl,-zl)
defs.targetobj(emptygr[0],cameraNew)
cameragr.append(bpy.context.object)
cameraNew=defs.addCameraShp(xl,yl,-zl)
defs.targetobj(emptygr[0],cameraNew)
cameragr.append(bpy.context.object)
cameraNew=defs.addCameraShp(xl,-yl,zl)
defs.targetobj(emptygr[0],cameraNew)
cameragr.append(bpy.context.object)
cameraNew=defs.addCameraShp(-xl,yl,zl)
defs.targetobj(emptygr[0],cameraNew)
cameragr.append(bpy.context.object)

defs.putMarkers(cameragr)

#On passe sur Cycle
bpy.data.scenes['Scene'].render.engine = 'CYCLES'
         
#Cinema!! Allonger la duree du film
bpy.data.scenes['Scene'].frame_end = 1100
bpy.data.scenes['Scene'].frame_current = 1

#Adding something to reduce noise
bpy.context.view_layer.cycles.use_denoising = True




