;PRO WRITE_3EMB_FRACTIONS
;This module is part of a sequence to combine 2-,3-,and 4-endmember models
;Writes output fractions for winning 3-endmember models
;
;Three-endmember simple models are as follows:
;   mod1:  sand + GV + shade
;   mod2:  mud + GV + shade
;   mod3:  NPV + GV + shade
;   mod4:  sand + mud + shade
;   mod5:  sand + NPV + shade
;   mod6:  mud + NPV + shade
;   
;Input files:  
;SMA output for simple 3-endmember models 
;-- E:\ls5\20150519\3em_1
;-- E:\ls5\20150519\3em_2
;-- E:\ls5\20150519\3em_3
;-- E:\ls5\20150519\3em_4
;-- E:\ls5\20150519\3em_5
;-- E:\ls5\20150519\3em_6
;Winning 3emb model numbers 
;-- E:\ls5\20150519\win_3emb
;
;Output files:
;Sand fraction -- ...\EMF\sub_sand_3emb_fract
;Mud fraction --  ...\EMF\sub_mud_3emb_fract
;NPV fraction -- ...\EMF\sub_npv_3emb_fract
;GV fraction -- ...\EMF\sub_gv_3emb_fract
;Shade fraction -- ...\EMF\sub_shad_3emb_fract

pro write_3emb_fractions

cd,'E:\ls5\20150519'

;specify input files
mod1_3emb_filename = $
  'E:\ls5\20150519\3em_1'
envi_open_file,mod1_3emb_filename, r_fid=fid1
envi_file_query,fid1,ns=ns,nl=nl,nb=nb,data_type=data_type1,dims=dims1,interleave=interleave
map_info=envi_get_map_info(fid=fid1)

mod2_3emb_filename = $
  'E:\ls5\20150519\3em_2'
envi_open_file,mod2_3emb_filename, r_fid=fid2

mod3_3emb_filename = $
  'E:\ls5\20150519\3em_3'
envi_open_file,mod3_3emb_filename, r_fid=fid3

mod4_3emb_filename = $
  'E:\ls5\20150519\3em_4'
envi_open_file,mod4_3emb_filename, r_fid=fid4

mod5_3emb_filename = $
  'E:\ls5\20150519\3em_5'
envi_open_file,mod5_3emb_filename, r_fid=fid5

mod6_3emb_filename = $
  'E:\ls5\20150519\3em_6'
envi_open_file,mod6_3emb_filename, r_fid=fid6

win_mod_filename = $
  'E:\ls5\20150519\win_3emb'
envi_open_file,win_mod_filename, r_fid=fid7
envi_file_query,fid7,data_type=data_type2

;specify output file
sand_outfile='E:\ls5\20150519\EMF\sub_sand_3emb_fract'
mud_outfile='E:\ls5\20150519\EMF\sub_mud_3emb_fract'
npv_outfile='E:\ls5\20150519\EMF\sub_npv_3emb_fract'
gv_outfile='E:\ls5\20150519\EMF\sub_gv_3emb_fract'
shade_outfile='E:\ls5\20150519\EMF\sub_shad_3emb_fract'
openw,lun1,sand_outfile, /Get_lun
openw,lun2,mud_outfile, /Get_lun
openw,lun3,npv_outfile, /Get_lun
openw,lun4,gv_outfile, /Get_lun
openw,lun5,shade_outfile, /Get_lun

;create array to store band values for each pixel
mod1_arr = fltarr(ns,3)
mod2_arr = fltarr(ns,3)
mod3_arr = fltarr(ns,3)
mod4_arr = fltarr(ns,3)
mod5_arr = fltarr(ns,3)
mod6_arr = fltarr(ns,3)
sand_arr = fltarr(ns)
mud_arr = fltarr(ns)
npv_arr = fltarr(ns)
gv_arr = fltarr(ns)
shad_arr = fltarr(ns)

FOR j=0L,nl-1 DO BEGIN
   ;set dims for model_data slice
   dims2=[-1L,0L,ns-1,j,j]
   
   mod1_data = envi_get_slice(/BIL,fid=fid1,line=j,pos=[0L,1L,2L])
   mod2_data = envi_get_slice(/BIL,fid=fid2,line=j,pos=[0L,1L,2L])
   mod3_data = envi_get_slice(/BIL,fid=fid3,line=j,pos=[0L,1L,2L])
   mod4_data = envi_get_slice(/BIL,fid=fid4,line=j,pos=[0L,1L,2L])
   mod5_data = envi_get_slice(/BIL,fid=fid5,line=j,pos=[0L,1L,2L])
   mod6_data = envi_get_slice(/BIL,fid=fid6,line=j,pos=[0L,1L,2L])
   mod_num = envi_get_data(dims=dims2,fid=fid7,pos=0L)
   
   sand_arr = (mod_num eq 1)*mod1_data(*,0)+(mod_num eq 4)*mod4_data(*,0)+$
    (mod_num eq 5)*mod5_data(*,0)
         
   mud_arr = (mod_num eq 2)*mod2_data(*,0)+(mod_num eq 4)*mod4_data(*,1)+$
    (mod_num eq 6)*mod6_data(*,0)
   
   npv_arr = (mod_num eq 3)*mod3_data(*,0)+(mod_num eq 5)*mod5_data(*,1)+$
    (mod_num eq 6)*mod6_data(*,1)
   
   gv_arr = (mod_num eq 1)*mod1_data(*,1)+ (mod_num eq 2)*mod2_data(*,1)+$
    (mod_num eq 3)*mod3_data(*,1)
   
   shad_arr = (mod_num eq 1)*mod1_data(*,2)+(mod_num eq 2)*mod2_data(*,2)+$
    (mod_num eq 3)*mod3_data(*,2)+(mod_num eq 4)*mod4_data(*,2)+$
    (mod_num eq 5)*mod5_data(*,2)+(mod_num eq 6)*mod6_data(*,2)
   
   writeu,lun1,sand_arr
   writeu,lun2,mud_arr
   writeu,lun3,npv_arr
   writeu,lun4,gv_arr
   writeu,lun5,shad_arr
ENDFOR

;write headers for output images
envi_setup_head,data_type=data_type1,fname=sand_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid8,/write
envi_setup_head,data_type=data_type1,fname=mud_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid9,/write
envi_setup_head,data_type=data_type1,fname=npv_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid10,/write
envi_setup_head,data_type=data_type1,fname=gv_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid11,/write
envi_setup_head,data_type=data_type1,fname=shade_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid12,/write

Free_lun,lun1,lun2,lun3,lun4,lun5
END
