# Replace these paths with your layout template and shapefile paths
layout_template_path = "C:/Users/BerkayAkpinar/Desktop/Kungrad-OHL/Paftalar/ExportLayout.qgz"
shapefile_path = "C:/Users/BerkayAkpinar/Desktop/Kungrad-OHL/Paftalar/ExportGrid.shp"

# Load the shapefile
layer = QgsVectorLayer(shapefile_path, "Rectangular Shapefile", "ogr")

if not layer.isValid():
    print("Error: Invalid layer!")
else:
    # Load the layout template
    project = QgsProject.instance()
    project.read(layout_template_path)
    
    # Access the layout
    layout = project.layoutManager().layoutByName('FinalExport')  # Replace 'YourLayoutName' with your layout name

    # Find the map item in the layout
    map_item = layout.itemById('Map 1')  # Replace 'YourMapItemId' with the actual ID of your map item
    
    if map_item is not None:
        # Loop through each feature in the shapefile
        for feature in layer.getFeatures():
            # Clone the extent of the map item for each feature
            map_extent = feature.geometry().boundingBox()
            map_item.setExtent(map_extent)
            
            # Export the layout to a PNG image
            # You can customize the output file path and format as needed
            layout_title = feature['RowNumber']  # Replace 'Name' with the actual attribute name for the title
            output_path = f"C:/Users/BerkayAkpinar/Desktop/Kungrad-OHL/Paftalar//{layout_title}.png"
            exporter = QgsLayoutExporter(layout)
            image_settings = QgsLayoutExporter.ImageExportSettings()
            image_settings.dpi = 1200  # Set DPI to 1200
            image_settings.imageWidth = 14031
            image_settings.imageHeight = 9921
            exporter.exportToImage(output_path, image_settings)