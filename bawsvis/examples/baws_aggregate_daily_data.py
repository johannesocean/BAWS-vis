# Copyright (c) 2020 SMHI, Swedish Meteorological and Hydrological Institute 
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2020-08-31 09:48

@author: a002028
"""
from bawsvis.utils import generate_filepaths
from bawsvis.session import Session
from bawsvis.data_handler import raster_aggregation


# if __name__ == "__main__":
#     # Set path to data directory
#     data_path = r'C:\Temp\baws_tempo\data_2021\corrected_geometries'
#
#     # Create the Session object
#     s = Session(data_path=data_path)
#
#     # If we want to save data to a specific location, we set the export path here.
#     # s.setting.set_export_directory(path=None)
#
#     # Generate filepaths
#     generator = generate_filepaths(s.data_path, pattern='cyano_daymap_', endswith='.tiff')
#
#     # Loop through the file-generator and aggregate the data.
#     # aggregation is a numpy 2d-array
#     aggregation = raster_aggregation(generator)
#
#     # Export the aggragation in a tiff file.
#     # WARNING! tiff files only handles integer data with values <=100.
#     # The benefit of tiff-files are the super compressed format
#     s.export_data(data=aggregation, file_name='aggregation_2021.tiff')

if __name__ == "__main__":
    # Set path to data directory
    # data_path = r'C:\Temp\baws_reanalys\clipped_archive\corrected_geoms'
    # data_path = r'C:\Temp\baws_reanalys\2022\corrected_geoms'
    data_path = r'..\data\prod\BAWS\algproduktion\Manuell_algtolkning'

    # Create the Session object
    s = Session(data_path=data_path)

    # If we want to save data to a specific location,
    # we set the export path here.
    s.setting.set_export_directory(
        path=r'C:\Temp\baws_reanalys\aggragated_archive')

    # If we want to save data to a specific location,
    # we set the export path here.
    # s.setting.set_export_directory(path=None)

    # for year in range(2002, 2021):
    year = 2022
    generator = generate_filepaths(s.data_path, pattern=f'cyano_daymap_{year}',
                                   endswith='.tiff')

    # Loop through the file-generator and aggregate the data.
    # aggregation is a numpy 2d-array
    aggregation = raster_aggregation(generator, only_surface=False)

    # Export the aggragation in a tiff file.
    # WARNING! tiff files only handles integer data with values <=100.
    # The benefit of tiff-files are the super compressed format
    s.export_data(
        data=aggregation,
        file_name=f'not_corrected_aggregation_{year}.tiff'
    )
