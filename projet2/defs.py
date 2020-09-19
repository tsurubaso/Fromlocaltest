import bpy
import random


#l'ensemble des def 
def addLamp(loc):
    bpy.ops.object.add(radius=1.0, type='LIGHT', enter_editmode=False, align='WORLD', location=loc, rotation=(0.0, 0.0, 0.0))
    bpy.context.object.data.type = 'SUN'
    bpy.context.object.data.energy = 3
    
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
    
def addCameraShp(pio, mid, pimp):
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(pio, mid, pimp), rotation=(0, 0, 0))
    cameraNew=bpy.context.object
    return cameraNew

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
    return cameraNew2
    
def putMarkers(cameragr):
    #work on Sequence Camera
    nyo=0
    pinyu=len(cameragr)*100
    for mip in range (1,pinyu,100):
        bpy.data.scenes['Scene'].frame_current = mip
        marker=bpy.data.scenes['Scene'].timeline_markers.new(cameragr[nyo].name, frame=mip)
        marker.camera = cameragr[nyo]
        nyo=nyo+1


#to create curve
#this for reference
#coords_list = [[0,1,2], [1,2,3], [-3,2,1], [0,0,-4]]
#create_curve(coords_list)
#cordo camera

def create_curve(coords_list, cordocam):
    #add curve
    crv = bpy.data.curves.new('crv', 'CURVE')
    crv.dimensions = '3D'
    crv.resolution_u = 2
    spline = crv.splines.new(type='NURBS')
    spline.points.add(len(coords_list) - 1) 
    for p, new_co in zip(spline.points, coords_list):
        p.co = (new_co + [1.0])
    spline.use_endpoint_u = True
    spline.use_endpoint_v = True
    newCurve = bpy.data.objects.new('CurveNya', crv)
    bpy.data.collections['Collection'].objects.link(newCurve)
    print(newCurve)
    #add camera
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(cordocam), rotation=(0, 0, 0))
    cameraNew=bpy.context.object
    print(cameraNew)
    #Donc parent Curve and camera
    bpy.ops.object.select_all(action='DESELECT')
    newCurve.select_set(True)
    cameraNew.select_set(True)
    bpy.context.view_layer.objects.active = newCurve
    bpy.ops.object.parent_set(type='FOLLOW') 
    bpy.context.object.data.path_duration = 1100
    return cameraNew

    
    