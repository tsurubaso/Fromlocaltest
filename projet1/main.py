import bpy
import random
defs = bpy.data.texts["defs.py"].as_module()

#Toutes les variables
#le calcul des points des lamps
xl=10
yl=10
zl=10
#Locations spheres
x=0
y=0
z=0
#volume de la sphere
g=0.1
#les groups that we will use later
meshgr=[]
emptygr=[]
lampgr=[]
cameragr=[]
piotrgr=[]
Douchkagr=[]
#la camera
camera= bpy.context.scene.objects['Camera']
cameragr.append(camera)



#Le programme en lui meme
defs.addLamp((xl,yl,zl))
lampgr.append(bpy.context.object)
defs.addLamp((-xl,-yl,zl))
lampgr.append(bpy.context.object)
defs.addLamp((-xl,yl,-zl))
lampgr.append(bpy.context.object)
defs.addLamp((xl,-yl,-zl))
lampgr.append(bpy.context.object)

defs.makeEmpty((x,y,z))
emptygr.append(bpy.context.object)

x,y,z,g,meshgr,Douchkagr,piotrgr=defs.bouclePlanet((x,y,z))
x,y,z,g,meshgr,Douchkagr,piotrgr=defs.bouclePlanet((x,y,z))
x,y,z,g,meshgr,Douchkagr,piotrgr=defs.bouclePlanet((x,y,z))
x,y,z,g,meshgr,Douchkagr,piotrgr=defs.bouclePlanet((x,y,z))
x,y,z,g,meshgr,Douchkagr,piotrgr=defs.bouclePlanet((x,y,z))
x,y,z,g,meshgr,Douchkagr,piotrgr=defs.bouclePlanet((x,y,z))
x,y,z,g,meshgr,Douchkagr,piotrgr=defs.bouclePlanet((x,y,z))
x,y,z,g,meshgr,Douchkagr,piotrgr=defs.bouclePlanet((x,y,z))


#Inversion des elements de la liste de sphere
meshgr.reverse()

#La boucle pour parenter et ajouter les Keyframes
for it in range (0, len(meshgr)-1):
    defs.makeparent (meshgr[it+1], meshgr[it])
    it=it+1
    h,j,k=0,0,0
    for iframe in range (1, 1200, 100):
        rer=random.uniform(-1,1)
        rer2=random.uniform(-.5,.5)
        rer3=random.uniform(-.5,.5)
        h=h+rer
        j=j+rer2
        k=k+rer3
        meshgr[it].rotation_euler=((h, j, k))
        meshgr[it].keyframe_insert(data_path="rotation_euler", frame=iframe)
        
        

#La boucle pour Empty et ajouter les Keyframes
for iv in range (0, len(piotrgr)):
    bpy.ops.object.select_all(action='DESELECT')
    scal=0.5
    scal2=0.5
    for iframe in range (1, 1200, 100):
        scal=scal+random.uniform(.01,0.05)
        scal2=scal+random.uniform(.01,0.05)
        
        rer=random.uniform(-0.01,0.01)
        rer2=random.uniform(-.01,.01)
        rer3=random.uniform(-.01,.01)
        
        u=random.uniform(-.02,0.2)
        
        u2=random.uniform(-0.01,0.1)
        u3=random.uniform(-0.01,0.1)
        u4=random.uniform(-0.01,0.1)
        
        u5=random.uniform(-1,1)
        u6=random.uniform(-1,1)
        u7=random.uniform(-1,1)
        
        u8=random.uniform(-1,1)
        u9=random.uniform(-1,1)
        u10=random.uniform(-1,1)
        
        bpy.context.scene.frame_set(iframe)
        
    
        (h,j,k)=meshgr[iv].location

        
        
        
        
        
        
        h=h+rer
        j=j+rer2
        k=k+rer3
        Douchkagr[iv].location=((h, j, k))
        Douchkagr[iv].keyframe_insert(data_path="location", frame=iframe)
        Douchkagr[iv].scale=(scal,scal,scal)
        Douchkagr[iv].keyframe_insert(data_path="scale", frame=iframe)
        Douchkagr[iv].rotation_euler=(u5,u6,u7)
        Douchkagr[iv].keyframe_insert(data_path="rotation_euler", frame=iframe)
        (h,j,k)=meshgr[iv].location
        h=h+u2
        j=j+u3
        k=k+u4
        piotrgr[iv].location=((h, j, k))
        piotrgr[iv].keyframe_insert(data_path="location", frame=iframe)
        piotrgr[iv].scale=(scal2,scal2,scal2)
        piotrgr[iv].keyframe_insert(data_path="scale", frame=iframe)
        piotrgr[iv].rotation_euler=((u8,u9,u10))
        piotrgr[iv].keyframe_insert(data_path="rotation_euler", frame=iframe)
        #print (piotrgr[iv])
        #print (piotrgr[iv].scale)
        #print (piotrgr[iv].rotation_euler)
        

#camera principale sur Empty
defs.targetobj(emptygr[0],camera)

#les Lamps sur des spheres aux hasard
for up in lampgr:
    qsph = random.randint(0,len(meshgr)-1)
    
    defs.targetobj(meshgr[qsph],up)


#Premier traveling La camera d'origine
bpy.ops.curve.primitive_bezier_circle_add(radius=15, enter_editmode=False, align='WORLD', location=(0, 0, 0))
path = bpy.context.object 
camera.select_set(True)
path.select_set(True)
bpy.context.view_layer.objects.active = path
bpy.ops.object.parent_set(type='FOLLOW') #follow paths
bpy.context.object.data.path_duration = 1100

#deux autres travelings
defs.cameraTravelingSimpleShp(10.0,0.0, 9.0)
cameragr.append(bpy.context.object)
defs.cameraTravelingSimpleShp(5.0,0.0, 10.0)
cameragr.append(bpy.context.object)

#Ajout de cameras
defs.addCameraShp(-xl,-yl,-zl)
cameragr.append(bpy.context.object)
defs.addCameraShp(xl,yl,-zl)
cameragr.append(bpy.context.object)
defs.addCameraShp(xl,-yl,zl)
cameragr.append(bpy.context.object)
defs.addCameraShp(-xl,yl,zl)
cameragr.append(bpy.context.object)

defs.putMarkers(cameragr)



#On passe sur Cuycle
bpy.data.scenes['Scene'].render.engine = 'CYCLES'
         
#Cinema!! Allonger la duree du film
bpy.data.scenes['Scene'].frame_end = 1100

bpy.data.scenes['Scene'].frame_current = 1

#Adding something to reduce noise
bpy.context.view_layer.cycles.use_denoising = True
#the rest does not work
#bpy.context.view_layer.cycles.denoising_store_passes = True
#bpy.context.view_layer.cycles.use_adaptive_sampling = True
#bpy.context.view_layer.cycles.samples = 700













    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#I really want to do it this way but no time
#https://www.youtube.com/watch?v=K02hlKyoWNI
#the simple way that works
