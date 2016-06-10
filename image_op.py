'''
    transfrom origin code from http://zhidao.baidu.com/link?url=-WcVhQyySGKRHgi08eZg1b_XhgxXIsyXnM2DMd76_qzOgTwEUQA5ZLhK5R1HIyeQBhYkwi7V7i5TmyEau1DY_-g7Y4pydgugiVheKeTajLi
    use code to transfrom a picture to specific size

    indir = "D:/CsTech/CV/image/origin"
    outdir = "D:/CsTech/CV/image/transform"
    image_op.convertjpg_batch(indir,outdir,width=64,height=64)
'''
from PIL import Image
from scipy.misc import imread
import numpy as np
import os.path
import glob
def convertjpg(jpgfile,outdir,width=64,height=64):
    img=Image.open(jpgfile)   
    new_img=img.resize((width,height),Image.BILINEAR)   
    new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))

def convertjpg_batch(indir,outdir,width=64,height=64):
    for jpgfile in glob.glob(indir + "/*.jpg"):
        convertjpg(jpgfile, outdir)

def readimage(fname):
    x_image = imread(fname)
    x_image = x_image.reshape(1, *x_image.shape)
    return x_image
    
def readimage_batch(indir):
    x_image_batch = []
    name = []
    for jpgfile in glob.glob(indir + "/*.jpg"):
        name.append(jpgfile[len(indir)+1:])
        x_image_batch.append(readimage(jpgfile))
    return x_image_batch, name
        
        
def test_convertjpg_batch():
    indir = "D:/CsTech/CV/image/origin"
    outdir = "D:/CsTech/CV/image/transform"
    convertjpg_batch(indir,outdir,width=64,height=64)

def test_readimage_batch():
    indir = "D:/CsTech/CV/image/transform"
    x_image_batch, name = readimage_batch(indir)
    return x_image_batch, name

