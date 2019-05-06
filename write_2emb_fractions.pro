;PRO WRITE_2EMB_FRACTIONS
;CREATED AND SUPPLIED BY R L POWELL, ED BY K WAECHTER FOR QB-OBIA VARZ STUDY
;This module is part of a sequence to combine 2-,3-,and 4-endmember models
;Writes output fractions for winning 2-endmember models
;Input files:  
;SMA output for 2-endmember models -- lib0130313\L5228r61-62_refl-v2_sub-20130314_2emb-v8_unconstr
;Winning 2emb model numbers -- win_2emb
;Output files:
;Sand fraction -- sub_sand_fract
;Mud fraction --  sub_mud_fract
;NPV fraction -- sub_npv_fract
;GV fraction -- sub_gv_fract
;Shade fraction -- sub_shad_fract

pro write_2emb_fractions

cd,'E:\ls5\20150519'

;specify input files
sma_2emb_filename = $
  'E:\ls5\20150519\2em_all'
envi_open_file,sma_2emb_filename, r_fid=fid1
envi_file_query,fid1,ns=ns,nl=nl,nb=nb,data_type=data_type1,dims=dims1,interleave=interleave
map_info=envi_get_map_info(fid=fid1)

win_mod_filename = $
  'E:\ls5\20150519\win_2emb'
envi_open_file,win_mod_filename, r_fid=fid2
envi_file_query,fid2,data_type=data_type2

;specify output file
sand_outfile='E:\ls5\20150519\EMF\sub_sand_2emb_fract'
mud_outfile='E:\ls5\20150519\EMF\sub_mud_2emb_fract'
npv_outfile='E:\ls5\20150519\EMF\sub_npv_2emb_fract'
gv_outfile='E:\ls5\20150519\EMF\sub_gv_2emb_fract'
shade_outfile='E:\ls5\20150519\EMF\sub_shad_2emb_fract'
openw,lun1,sand_outfile, /Get_lun
openw,lun2,mud_outfile, /Get_lun
openw,lun3,npv_outfile, /Get_lun
openw,lun4,gv_outfile, /Get_lun
openw,lun5,shade_outfile, /Get_lun

;create array to store band values for each pixel
sma_arr = fltarr(ns,2)
mod_num = lonarr(ns)
sand_arr = fltarr(ns)
mud_arr = fltarr(ns)
npv_arr = fltarr(ns)
gv_arr = fltarr(ns)
shad1_arr = fltarr(ns)
shad2_arr = fltarr(ns)
shad3_arr = fltarr(ns)
shad4_arr = fltarr(ns)
shad_tot_arr = fltarr(ns)

FOR j=0L,nl-1 DO BEGIN
   ;set dims for model_data slice
   dims2=[-1L,0L,ns-1,j,j]
   
   sma_data = envi_get_slice(/BIL,fid=fid1,line=j,pos=[0L,1L])
   mod_data = envi_get_data(dims=dims2,fid=fid2,pos=0L)
   
   sand_arr = (mod_data eq 1)*sma_data(*,0)
   ;shad1_arr = (mod_data eq 1)*sma_data(*,1)
         
   mud_arr = (mod_data eq 2)*sma_data(*,0)
   ;shad2_arr = (mod_data eq 2)*sma_data(*,1)
   
   npv_arr = (mod_data eq 3)*sma_data(*,0)
   ;shad3_arr = (mod_data eq 3)*sma_data(*,1)
   
   gv_arr = (mod_data eq 4)*sma_data(*,0)
   ;shad4_arr = (mod_data eq 4)*sma_data(*,1)
   
   ;shad_tot_arr = shad1_arr + shad2_arr + shad3_arr + shad4_arr
   shad_tot_arr = (mod_data eq 1)*sma_data(*,1)+(mod_data eq 2)*sma_data(*,1)+$
    (mod_data eq 3)*sma_data(*,1)+(mod_data eq 4)*sma_data(*,1)
   
   writeu,lun1,sand_arr
   writeu,lun2,mud_arr
   writeu,lun3,npv_arr
   writeu,lun4,gv_arr
   writeu,lun5,shad_tot_arr
ENDFOR

;write headers for output images
envi_setup_head,data_type=data_type1,fname=sand_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid3,/write
envi_setup_head,data_type=data_type1,fname=mud_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid4,/write
envi_setup_head,data_type=data_type1,fname=npv_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid5,/write
envi_setup_head,data_type=data_type1,fname=gv_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid6,/write
envi_setup_head,data_type=data_type1,fname=shade_outfile,map_info=map_info,$
   ns=ns,nl=nl,nb=1,interleave=0,offset=0,/open,r_fid=fid7,/write

Free_lun,lun1,lun2,lun3,lun4,lun5
END
