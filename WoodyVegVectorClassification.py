###########################################################################
##################         Katy Waechter                 ##################
##################         GOAL: Take tree polygons      ##################
##################         and segmented objects to      ##################
##################         classify shrub and open       ##################
##################         woodland land cover classes.  ##################
###########################################################################
import os
import arcpy
import math
import arcpy.sa
arcpy.CheckOutExtension("spatial")

##SET WORKSPACE AND OVERWRITE AS NEEDED
from arcpy import env
env.workspace="E:\\3130\\final"
env.overwriteOutput=True

log.open("test.txt", "w+")
log.print("This is the log for my shrub and open woodland classification in the varzea.\n")

##define classes: points and polygons as trees and geographic units (GU)
class Point:
    "Common base class for all points"
    ##attribute list
    def __init__(self,coordX=0,coordY=0,name=""):
        self.x=coordX
        self.y=coordY
        self.name=name


class Polygon:
    "Common base class for all polygons"
    ##attribute list
    def __init__(self,SHAPE))
        self.shape= ...

class Centroid(Point):
    def __init__(self,coordX,coordY,name=""):
        Point.__init__(self)
        self.x=coordX
        self.y=coordY
        self.name=name
    ##define method in a class
    def CentroidDistance(self,pt):
        distance = pow((self.x-pt.x),2)+pow((self.y-pt.y),2)
        return math.sqrt(distance)

class Trees(Polygon):
    def __init__(self,points=[],area="",name=""):
        Polygon.__init__(self,points)
        self.area=SHAPE.area
        self.name=name
    def GetArea(self):
        i=0
        area=0
        while i<len(self.points):
            area=arcpy.getArea  #http://resources.arcgis.com/en/help/main/10.1/index.html#/PointGeometry/018z00000039000000/
            i=i+1
        return area
    def GetSizeClass(self):
        for tree in Trees:
            if self.area<=12:
                return "Small"
            elif self.area<=30:
                return "Medium"
            else:
                return: "Large"

class GU(Polygon):
    def __init__(self,points=[],area="",name=""): ##should area for polys be made as a sep fcn?
        Polygon.__init__(self,points)
        self.area=SHAPE.area
        self.name=name


##describe tree polygons
trees="trees.shp"
descTrees=arcpy.Describe(trees)
log(print "Tree file data type is ", desc.dataType)
log.close()



##CREATE PROCESSING AND OUTPUT FOLDERS
if not os.path.exists("E:\\3130\\final\\Processing"):
    os.makedirs("E:\\3130\\final\\Processing")
if not os.path.exists("E:\\3130\\final\\Output"):
    os.makedirs("E:\\3130\\final\\Output")
if not os.path.exists("E:\\3130\\final\\Output\\COA"):
    os.makedirs("E:\\3130\\final\\Output\\COA")
if not os.path.exists("E:\\3130\\final\Output\\Input"):
    os.makedirs("E:\\3130\\final\\Output\\Input")
##MAKE A LOG FILE TO SAVE PROCESS REPORTS
log=open("Output\\WORKLOG_README.txt", "w+")
log.write("This is the test log for my shrub and open woodland classification in the varzea.\n")
print "See log file in Output folder for report.\n"

#############################################################################
###################  DESCRIBE ORIGINAL QUICKBIRD 2 SCENE  ###################
#############################################################################
scene="QB20050705_50_2p5m.img"
rasterscene=arcpy.Describe(scene)
print "The scene used for this iteration: "+str(rasterscene.basename)+"\n"
print "\nScene file format: ", rasterscene.format, "\n"
print "\nScene band count: ", rasterscene.bandCount, "\n"
print "\nScene extent: ", rasterscene.extent, "\n" ##FUTURE:use to make mask shapefile for analysis extent
print "\nScene spatial reference: ", rasterscene.spatialReference, "\n"
MS_band1="QB20050705_50_2p5m.img\Orthorectified (Band 1)"
MS_band2="QB20050705_50_2p5m.img\Orthorectified (Band 2)"
MS_band3="QB20050705_50_2p5m.img\Orthorectified (Band 3)"
MS_band4="QB20050705_50_2p5m.img\Orthorectified (Band 4)"
##BAND 1
QBMS1band=arcpy.Describe(MS_band1)
MS1height = QBMS1band.meanCellHeight
MS1width = QBMS1band.meanCellWidth
print "\nThe spatial resolution of "+str(MS_band1)+" is "+str(MS1height)+" by "+str(MS1width)+".\n"
log.write("\nThe spatial resolution of multispectral bands is "+str(MS1height)+" by "+str(MS1width)+".\n")
##BAND 2
QBMS2band=arcpy.Describe(MS_band2)
MS2height = QBMS2band.meanCellHeight
MS2width = QBMS2band.meanCellWidth
print "\nThe spatial resolution of "+str(MS_band2)+" is "+str(MS2height)+" by "+str(MS2width)+".\n"
log.write("\nThe spatial resolution of multispectral bands is "+str(MS2height)+" by "+str(MS2width)+".\n")
##BAND 3
QBMS3band=arcpy.Describe(MS_band3)
MS3height = QBMS3band.meanCellHeight
MS3width = QBMS3band.meanCellWidth
print "\nThe spatial resolution of "+str(MS_band3)+" is "+str(MS3height)+" by "+str(MS3width)+".\n"
log.write("\nThe spatial resolution of multispectral bands is "+str(MS3height)+" by "+str(MS3width)+".\n")
##BAND 4
QBMS4band=arcpy.Describe(MS_band4)
MS4height = QBMS4band.meanCellHeight
MS4width = QBMS4band.meanCellWidth
print "\nThe spatial resolution of "+str(MS_band4)+" is "+str(MS4height)+" by "+str(MS4width)+".\n"
log.write("\nThe spatial resolution of multispectral bands is "+str(MS4height)+" by "+str(MS4width)+".\n")
#############################################################################

#############################################################################
############  TAKE SKELETON DATA FILES AND COMPUTE GEOMETRY INFO  ###########
#############################################################################
Segmented_Units = "SU.shp"
Tree_Crowns = "treeply.shp"
##Add Geometry Attributes to Segmented Units
arcpy.AddGeometryAttributes_management(Segmented_Units, "AREA", "METERS", "SQUARE_METERS", "PROJCS['WGS_1984_UTM_Zone_21S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['false_easting',500000.0],PARAMETER['false_northing',10000000.0],PARAMETER['central_meridian',-57.0],PARAMETER['scale_factor',0.9996],PARAMETER['latitude_of_origin',0.0],UNIT['Meter',1.0]]")
print "\nArea in square meters has been added to the Segmented Units shapefile attribute table.\n"
log.write("\nAdd Geometry Attributes to Segmented Units:\n"+str(arcpy.GetMessages()))
##Add Geometry Attributes to Tree Crowns
arcpy.AddGeometryAttributes_management(Tree_Crowns, "AREA;CENTROID_INSIDE", "METERS", "SQUARE_METERS", "PROJCS['WGS_1984_UTM_Zone_21S',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['false_easting',500000.0],PARAMETER['false_northing',10000000.0],PARAMETER['central_meridian',-57.0],PARAMETER['scale_factor',0.9996],PARAMETER['latitude_of_origin',0.0],UNIT['Meter',1.0]]")
print "\nArea in square meters and centroid point coordinates have been added to the Tree Crown shapefile attribute table.\n"
log.write("\nAdd Geometry Attributes to Tree Crowns:\n"+str(arcpy.GetMessages()))
##Use Near tool to calculate (1) distance (planar) to nearest tree, (2) tree FID, (3) and near angle
arcpy.Near_analysis(Tree_Crowns, Tree_Crowns, "", "NO_LOCATION", "NO_ANGLE", "PLANAR")
print "\nDistance to nearest tree has been calculated.\n"
log.write("\nNear tool to Find Between Tree Distance:\n"+str(arcpy.GetMessages()))
#############################################################################

#############################################################################
##################  CREATE TREE GAP TO TREE CROWN RATIO  ####################
#############################################################################
##CREATE FIELD TO CALCULATE APPROXIMATE DIAMETER
fc=Tree_Crowns
newfield="DIAMETER"
fieldtype="DOUBLE"
fieldname=arcpy.ValidateFieldName(newfield)
arcpy.AddField_management(fc,fieldname,fieldtype)
arcpy.CalculateField_management(fc,fieldname, "math.pow(!POLY_AREA! * 4 /math.pi, .5) * 2", "PYTHON")
print "\nBy assuming circle geometry, an approximate diameter of tree crowns has been calculated.\n"
log.write("\nCalculation of approximate tree crown diameter:\n"+str(arcpy.GetMessages()))
##CREATE FIELD TO CALCULATE TREE GAP TO CROWN DIAMETER RATIO
newfield1="GapCrRatio"
fieldtype1="DOUBLE"
fieldname1=arcpy.ValidateFieldName(newfield1)
arcpy.AddField_management(fc,fieldname1,fieldtype1)
arcpy.CalculateField_management(fc,fieldname1, "!NEAR_DIST! / !Diameter!", "PYTHON")
print "\nA tree gap to tree grown distance ratio has been computed.\n"
log.write("\nCalculation of tree gap to crown width ratio:\n"+str(arcpy.GetMessages()))
##CREATE NOMINATIVE FIELD TO INDICATE CLUSTERING BASED ON GAP-CROWN RATIO
##RULES: Ratios less than 30 are considered clustered, ratios less than 50 are considered random, ratios greater than 50 are considered dispersed
newfield5="GCR_Patter"
fieldtype5="STRING"
fieldname5=arcpy.ValidateFieldName(newfield5)
arcpy.AddField_management(fc,fieldname5,fieldtype5)
cursor=arcpy.da.UpdateCursor(fc, ["GapCrRatio", "GCR_Patter"])
for ratio in cursor:
    if ratio[0] <=30.0:
        ratio[1]="Clustered"
    elif ratio[0] <=50.0:
        ratio[1]="Random"
    else:
        ratio[1]="Dispersed"
    cursor.updateRow(ratio)
del ratio
del cursor
print "\nField indicating clustering based on gap-to-crown ratio has been created.\n"
log.write("\nField indicating clustering based on gap-to-crown ratio:\n"+str(arcpy.GetMessages()))
##CALCULATE AND REPORT SAMPLE STATISTICS FOR SAMPLE COMPARISON TO TABLE
CrownStats = "Output\\CrownStats.dbf"
arcpy.Statistics_analysis(Tree_Crowns, CrownStats, "POLY_AREA MEAN;POLY_AREA STD;NEAR_DIST MEAN;NEAR_DIST STD;Diameter MEAN;Diameter STD;GapCrRatio MEAN;GapCrRatio STD", "")
print "\nTree crown statistics have been exported to a table in the Output folder.\n"
log.write("\nTree crown statistics export to table:\n"+str(arcpy.GetMessages()))
#############################################################################
##########  CHECK SPATIAL AUTOCORRELATION AND CLUSTERING OF CROWNS ##########
#############################################################################
##Use Local Moran's I to explore Crown Area clustering
CrownArea = "Output\\COA\\CrnArea_LISA.shp"
arcpy.ClustersOutliers_stats(Tree_Crowns, "POLY_AREA", CrownArea, "INVERSE_DISTANCE", "EUCLIDEAN_DISTANCE", "NONE", "", "", "NO_FDR")
print "\nLocal Moran's I and Clustering has been identified using tree crown area.\n"
log.write("\nLocal Moran's I and Clustering has been identified using tree crown area:\n"+str(arcpy.GetMessages()))
##Use Local Moran's I to explore Nearest tree distance clustering
TreeDistance = "Output\\COA\\Near_LISA.shp"
arcpy.ClustersOutliers_stats(Tree_Crowns, "NEAR_DIST", TreeDistance, "INVERSE_DISTANCE", "EUCLIDEAN_DISTANCE", "NONE", "", "", "NO_FDR")
print "\nLocal Moran's I and Clustering has been identified using distance to nearest tree.\n"
log.write("\nLocal Moran's I and Clustering has been identified using distance to nearest tree:\n"+str(arcpy.GetMessages()))
##Use Local Moran's I to explore Gap-Crown ratio clustering
GCRatio = "Output\\COA\\GCRatio_LISA.shp"
arcpy.ClustersOutliers_stats(Tree_Crowns, "GapCrRatio", GCRatio, "INVERSE_DISTANCE", "EUCLIDEAN_DISTANCE", "NONE", "", "", "NO_FDR")
print "\nLocal Moran's I and Clustering has been identified using each tree's gap to crown distance ratio.\n"
log.write("\nLocal Moran's I and Clustering has been identified using gap-to-crown ratio:\n"+str(arcpy.GetMessages()))
#############################################################################

#############################################################################
####  CLASSIFY SEGMENTED UNITS BASED ON PERCENT OF UNITS THAT ARE TREED  ####
#############################################################################
##IDENTIFY TREE CROWNS BY SEGMENTED UNIT AND SU AREA
TreeSUIdentity = "Processing\\TreeSUIdentity.shp"
arcpy.Identity_analysis(Tree_Crowns, Segmented_Units, TreeSUIdentity, "ALL", "", "NO_RELATIONSHIPS")
print "\nTree crowns have been identified by segmented unit.\n"
log.write("\nTree crowns have been identified by segmented unit.\n"+str(arcpy.GetMessages()))
##SUMMARIZE CROWN AREA BY SEGMENTED UNIT
AreaTreeToSU = "Processing\\AreaTreeToSU.dbf"
arcpy.Statistics_analysis(TreeSUIdentity, AreaTreeToSU, "POLY_AREA SUM;POLY_ARE_1 MEAN", "FID_SU")
print "\nTree canopy area has been summed by segmented unit.\n"
log.write("\nTree canopy area has been summed by segmented unit.\n"+str(arcpy.GetMessages()))
##CALCULATE PERCENT OF SU COVERED BY TREE CROWN (PERCENT TREED)
fc2=AreaTreeToSU
newfield2="PCT_TREE"
fieldtype2="DOUBLE"
fieldname2=arcpy.ValidateFieldName(newfield2)
arcpy.AddField_management(fc2,fieldname2,fieldtype2)
arcpy.CalculateField_management(fc2,fieldname2, "!SUM_POLY_A! / !MEAN_POLY_!", "PYTHON")
print "\nPercent of segmented units covered by tree crown calculated.\n"
log.write("\nCalculation of percent of Segmented Units that are treed:\n"+str(arcpy.GetMessages()))
##JOIN TABLE WITH PERCENT TREED FIELD TO ORIGINAL SEGMENTED UNIT SHAPEFILE
arcpy.JoinField_management(Segmented_Units, "FID", AreaTreeToSU, "PCT_TREE", "PCT_TREE")
##MAKE NOMINATIVE FIELD TO INDICATE LAND COVER CLASS
##RULES: open woodland is 30-70% treed, forest is 70%+ treed, all else is other
fc3=Segmented_Units
newfield3="LC_CLASS"
fieldtype3="STRING"
fieldname3=arcpy.ValidateFieldName(newfield3)
arcpy.AddField_management(fc3,fieldname3,fieldtype3)
cursor=arcpy.da.UpdateCursor(fc3, ["PCT_TREE", "LC_CLASS"])
for unit in cursor:
    if unit[0] <=.3000:
        unit[1]="Other"
    elif unit[0] <=.7000:
        unit[1]="Open woodland"
    else:
        unit[1]="Forest"
    cursor.updateRow(unit)
del unit
del cursor
print "\nWoodland and forest units classified based on percent of tree cover.\n"
log.write("\nWoodland and tree classes assignment based on percent of area treed:\n"+str(arcpy.GetMessages()))
#############################################################################

###############################################################################
############# USE TREE CROWN POLYGONS TO CREATE TREE CENTROID FILE ############
###############################################################################
##SET THE LOCAL VARIABLES
in_Table = "treeply.dbf"
x_coords = "INSIDE_X"
y_coords = "INSIDE_Y"
out_Layer = "tree_centroids"
saved_Layer = "Processing\\TreeCentroids.lyr"
folder = "Output\\Input"
Centroids="Output\\Input\\tree_centroids.shp"
##SET THE SPATIAL REFERENCE
spRef = arcpy.SpatialReference(32721)##32721 is the authority code for UTM Z21S, WGS84; see http://resources.arcgis.com/en/help/main/10.1/018z/pdf/projected_coordinate_systems.pdf
##MAKE A TREE CENTROID EVENT LAYER
arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef)
##SAVE TO A LYR FILE
arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)
##APPLY GRADUATED SYMBOL SYMBOLOGY FOR TREE CENTROIDS
arcpy.ApplySymbologyFromLayer_management(saved_Layer, r"Z:\3130\final\blanks\tree_centroids.lyr")
##SAVE TO A SHAPEFILE
arcpy.FeatureClassToShapefile_conversion(out_Layer,folder)
print "\nTree centroids created.\n"
log.write("\nCreating tree centroids from crown database file:\n"+str(arcpy.GetMessages()))
##PRINT COUNT OF RECORDS
print "\nTree centroid count: "+str(arcpy.GetCount_management(Centroids))+"\n"
log.write("\nThere are "+str(arcpy.GetCount_management(Centroids))+" trees in this file.\n")
####MAKE NOMINATIVE FIELD TO INDICATE TREE SIZE
####RULES: small tree crowns are <150 square meters, medium tree crowns are <500 square meters, large tree crowns are >500 square meters
fc4=Centroids
newfield4="SIZE_CLASS"
fieldtype4="STRING"
fieldname4=arcpy.ValidateFieldName(newfield4)
arcpy.AddField_management(fc4,fieldname4,fieldtype4)
cursor=arcpy.da.UpdateCursor(fc4, ["POLY_AREA", "SIZE_CLASS"])
for tree in cursor:
    if tree[0] <=150:
        tree[1]="Small"
    elif tree[0] <=500:
        tree[1]="Medium"
    else:
        tree[1]="Large"
    cursor.updateRow(tree)
del tree
del cursor
print "\nTree crowns classified by size.\n"
log.write("\nTree crown sizes assignment:\n"+str(arcpy.GetMessages()))
#############################################################################

##SAVE COPIES OF PROCESSED DATA TO OUTPUT SUBDIRECTORY
Segmented_Units="SU.shp"
Tree_Crowns="treeply.shp"
P_Segmented_Units="Output\\Input\\SU.shp"
P_Tree_Crowns="Output\\Input\\treeply.shp"
arcpy.CopyFeatures_management(Segmented_Units, P_Segmented_Units)
arcpy.CopyFeatures_management(Tree_Crowns, P_Tree_Crowns)
print "\nBack up copies of the processed tree crown and segmented unit files have been saved.\n"
log.write("\nSaving back up copies of the processed tree crown and segmented unit files: \n"+str(arcpy.GetMessages()))

##CHECK IN SPATIAL ANALYST EXTENSION
arcpy.CheckInExtension("spatial")
print "\nSpatial Analyst extension checked back in.\n"

##DELETE PROCESSING FOLDER
import shutil
shutil.rmtree("Processing")
print "\nProcessing folder deleted.\n"

##CLOSE LOG FILE
log.close()
print "\nLog file closed."
