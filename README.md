# 2015 Varzea Project Archive
### Contribution to _Land and resource use on the Amazon floodplain under evolving management systems and environmental change: Fish, forests, cattle, and settlements_, [LCLUC project record](https://lcluc.umd.edu/projects/land-and-resource-use-amazon-floodplain-under-evolving-management-systems-and-environmental)

*See [**Waechter_ProjectReport_20150822.pdf**](https://github.com/kewaechter/Varzea/blob/master/Waechter_ProjectReport_20150822.pdf) for full write-up.*  

This archive contains substantive deliverables and scripts used to generate a replicable detailed classification of floodplain vegetation in the Lower Amazon River Floodplain. The methods developed for this project use Quickbird 2 and Landsat5 TM scenes from an area at the Tapajos River and Amazon River confluence near Santarem, Para, Brasil (see qb20051029.kml for footprint of Quickbird 2 mosaicked scenes). 

Because the area of this study is extremely heterogeneous and very few cloud-free images exist in the timespan of high resolution multispectral sensors, usable optical data is rare. As such, a method is needed that can extract usable and defensible data from both older panchromatic imagery and contemporary multispectral imagery. This project addresses that objective by using a combination of pixel- and object-based image analysis.

## Pixel-Based Image Analysis
* Use _Multiple Endmember Spectral Mixture Analysis_ to identify constituent component of sub-pixel physical objects (< 30 meters in size).  
* A spectral library (__VarzeaLibrary_v8_20130313.sli__), assembled by Jason Isherwood (2013), was used to calculate endmember fractions in custom IDL scripts (__write_2emb_fractions.pro__, __write_3emb_fractions.pro__, __write_4emb_fractions.pro__). Trained samples include *green vegetation*, *non-photosynthetic vegetation*, *mud*, *sand*, *shade*.    
* In 90+% of cells, 3 endmembers fit the spectral signature regression best.  
* Following endmember fraction generation, fractions are disaggregated to woody vegetation image objects (_non-primitive image objects_) for incorporation to vector-based classification scheme.  
* Top of atmosphere radiance converted to surface reflectance with atmospheric corrections addressed in _Waechter_GEOG3230_FinalReport.pdf_.  

## Object-Based Image Analysis
* Use variety of object-based image processing to extract radiometric and pixel neighborhood differences into meaningful classification criteria.   
* STEP 1: Calculate a locally normalized roughness index and use in _Multiresolution Segmentation_ to generate image object primitives, distinguishing rough textures and smooth textures.  
* STEP 2: Control for edge effects and modifiable areal unit problem by experimenting with image object statistics:   
    * Normalized difference vegetation index, scale, compactness, shape/object dimensions ratio(s), spatial autocorrelation, urban built-up masking, variable and neighborhood brightnesses    
* STEP 3: Use delineated woody vegetation areas and spatial weighting to generate landscape patch objects (_segmented units_) for vegetation cover calculation. Use variable scale objects to calculate percent woody cover (proxy for cover using subclass cover rule).   
    * ArcPy script (_WoodyVegVectorClassification.py_) used to create ArcToolbox (_OBIA_Am.tbx_) for a short workflow for counting trees/woody vegetation objects within landscape patches (_descriptionpic.png_). Test data in _treeply.shp.zip_ and _SU.shp.zip_.  
    * More details in _Waechter_FinalReport.pdf_.   
* STEP 4: Use extracted endmember fraction (_shade_, _green vegetation_, _non-photosynthetic vegetation_) distributions to breakdown endmember fraction thresholds corresponding to desired lifeforms (e.g., shrub, tree, grass) in areas predominately covered by woody vegetation.   
* STEP 5: Combine _cover_ and _lifeform_ classifications for a combined detailed classification of floodplain vegetation. _See LCCS.vsd for classification scheme._     

## Results

Cover Classification: sparse, open, closed
* Kappa = .92 | SE = .04

Lifeform Classification: shrub, tree, herbaceous
* Kappa = .85 | SE = .04

Overall Land Cover Classification: tree|open, tree|closed, shrub|open, shrub|closed, herbaceous|sparse woody vegetation
* Kappa = .68 | SE = .03

[An archive of the data results is available for download.](https://drive.google.com/file/d/1TljO69Zex1mDeJ3vXfTy6t8ATnCSKyXr/view?usp=sharing) Readable metadata for results are housed in _Guide to A24LowerAmFP.gdb.pdf_. 
