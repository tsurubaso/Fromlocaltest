import bpy
import random

meshgr=[]
cameragr=[]
piotrgr=[]
Douchkagr=[]

#l'ensemble des def 
def addLamp(loc):
    bpy.ops.object.add(radius=1.0, type='LIGHT', enter_editmode=False, align='WORLD', location=loc, rotation=(0.0, 0.0, 0.0))
    bpy.context.object.data.type = 'SUN'
    bpy.context.object.data.energy = 7
    
    
def my_custom_random():
  exclude=[1]
  randInt = random.randint(0,6)
  return my_custom_random() if randInt in exclude else randInt 

def makeparent (Objet1, Objet2):
    bpy.ops.object.select_all(action='DESELECT')
    Objet1.select_set(True)
    Objet2.select_set(True)
    bpy.context.view_layer.objects.active = Objet1
    bpy.ops.object.parent_set(type='OBJECT') #follow paths
     
   
def makeEmpty(loc3):
    #creation of Empty
    empt=bpy.ops.object.empty_add(type='SPHERE', align='WORLD', location=loc3)

def targetobj(obj1,obj2):
    targetobj = obj1
    objetverstarget = obj2
    ttc = objetverstarget.constraints.new(type='TRACK_TO')
    ttc.target = targetobj
    ttc.track_axis = 'TRACK_NEGATIVE_Z'
    ttc.up_axis = 'UP_Y'
    
    #Not in use for now
def addCamera(size, mid, pimp):
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(size, mid, pimp), rotation=(0, 0, 0))
    cameraNew = bpy.context.object 
    #to put in main.py
    #targetobj(emptygr[0],cameraNew)
    
def addCameraShp(size, mid, pimp):
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(size, mid, pimp), rotation=(0, 0, 0))
    cameraNew = bpy.context.object 
    qsph = random.randint(0,len(meshgr)-1)
    print(qsph)
    targetobj(meshgr[qsph],cameraNew)
    #targetobj(emptygr[0],cameraNew)
    
    #Not in use for now
def cameraTravelingSimple(size, mid, pimp):
    bpy.ops.curve.primitive_bezier_circle_add(radius=size, enter_editmode=False, align='WORLD', location=(0, 0, pimp))
    path = bpy.context.object 
    addCamera(size, mid, pimp)
    cameraNew2=bpy.context.object
    path.select_set(True)
    cameraNew2.select_set(True)
    bpy.context.view_layer.objects.active = path
    bpy.ops.object.parent_set(type='FOLLOW') #follow paths
    bpy.context.object.data.path_duration = 1100
    #to put in main.py
    #targetobj(emptygr[0],cameraNew2)
    
def cameraTravelingSimpleShp(size, mid, pimp):
    bpy.ops.curve.primitive_bezier_circle_add(radius=size, enter_editmode=False, align='WORLD', location=(0, 0, pimp))
    path = bpy.context.object 
    addCameraShp(size, mid, pimp)
    cameraNew2=bpy.context.object
    path.select_set(True)
    cameraNew2.select_set(True)
    bpy.context.view_layer.objects.active = path
    bpy.ops.object.parent_set(type='FOLLOW') #follow paths
    bpy.context.object.data.path_duration = 1100
    #On peut utiliser le return comme pour les mesh, ici autre methode
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = cameraNew2
    
def putMarkers(cameragr):
    #work on Sequence Camera
    nyo=0
    pinyu=len(cameragr)*100
    for mip in range (1,pinyu,100):
        bpy.data.scenes['Scene'].frame_current = mip
        marker=bpy.data.scenes['Scene'].timeline_markers.new(cameragr[nyo].name, frame=mip)
        marker.camera = cameragr[nyo]
        nyo=nyo+1


    
    