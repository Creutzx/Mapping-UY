import arcpy

mxd = arcpy.mapping.MapDocument(r'\\DEQHQ1\TMDL\TMDL_WR\MidCoast\GIS\Figures\Upper_Yaquina_Maps\Upper_Yaquina_TMDL_Layout_Elevation_BRC.mxd')
#current view?
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyr = arcpy.mapping.ListLayers(mxd, "", df)
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.name == "up_yaq_elev":
        lyr.name = "Elevation"
        lyr.visible = True

arcpy.RefreshTOC()
arcpy.RefreshActiveView()
mxd.save()
