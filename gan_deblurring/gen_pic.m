 %  生成带噪图片
 


clc;clear;close all
 
% cd ./ori_pic_4w
% dst_dir = '../noise_pic_4w/';

cd ./test_ori_2k
dst_dir = '../test_noise_2k/';

namelist = dir ('*.jpg');
len =500;
% 马赛克
for i =1:len 
    img=imread(namelist(i).name);
    pix_grp = 5;
    height = size(img,1);
    width = size(img,2);
    mosaic = imresize(img,[floor(height/pix_grp) floor(width/pix_grp)]);
    mosaic = imresize(mosaic,[height width],'nearest');
    imwrite(mosaic,[dst_dir,namelist(i).name])
    disp(namelist(i).name)
end
% 高斯
for i =len+1:2*len
   
    img=imread(namelist(i).name);
    gauss_Img= imnoise(img,'gaussian',0,0.01);
    imwrite(gauss_Img,[dst_dir,namelist(i).name])
    disp(namelist(i).name)
end
% 椒盐
for i =2*len+1:3*len
   
    img=imread(namelist(i).name);
    pepper_Img= imnoise(img,'salt & pepper');
    imwrite(pepper_Img,[dst_dir,namelist(i).name])
    disp(namelist(i).name)
end
% 运动
for i =3*len+1:4*len
    img=imread(namelist(i).name);
    H = fspecial('motion',20,45);
    Motion_img = imfilter(img,H,'replicate');
    imwrite(Motion_img,[dst_dir,namelist(i).name])
    disp(namelist(i).name)
end

%% 
