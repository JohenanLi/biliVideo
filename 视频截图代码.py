import os
import sys
import xlwt,math
from moviepy.editor import VideoFileClip
 
file_dir = u"D:\BaiduNetdiskDownload\中南大学教学视频\中南大学教学视频" #定义文件目录
 
class FileCheck():
 
    def __init__(self):
        self.file_dir = file_dir
    
    def get_filesize(self,filename):
        u"""
        获取文件大小（M: 兆）
        """
        file_byte = os.path.getsize(filename)
        return self.sizeConvert(file_byte)
 
    def get_file_times(self,filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename)
        file_time = self.timeConvert(clip.duration)
        return file_time
 
    def sizeConvert(self,size):# 单位换算
        K, M, G = 1024, 1024**2, 1024**3
        if size >= G:
            return str(size/G)+'G Bytes'
        elif size >= M:
            return str(size/M)+'M Bytes'
        elif size >= K:
            return str(size/K)+'K Bytes'
        else:
            return str(size)+'Bytes'
    

 
def get_all_file(file_dir,dirsList):
    u"""
    获取视频下所有的文件
    """
        
    for root, dirs, files in os.walk(file_dir): 
        print("--------")
        print(root)
        print(files)
        dirsList = dirs
        return dirsList,files

def get_file_times(filename):
        u"""
        获取视频时长（s:秒）
        """
        clip = VideoFileClip(filename)
        time = math.ceil(clip.duration)
        return time



dirsList = []
files = []
dirsList,files = get_all_file(file_dir,dirsList)
file = []
for i in range(len(dirsList)):
    m = file_dir+'\\'+dirsList[i]
    file.append(m)
    print(file[i])
for i in range(len(file)):
    dirsList,mm = get_all_file(file[i],dirsList)
    files.append(mm)
for i in range(10):
    print("--------------------------------------------")
print(file)
for m in range(len(files)):
    for n in range(len(files[m])):
        aaa = file[m] +"\\" +files[m][n]
        print(aaa)
        cmd = "ffmpeg  -i "+ aaa + " -ss 1.000 -vframes 1 "+ "C:\\Users\\59919\\Desktop\\images\\"+str(m+1) +"\\"+str(n+1)+".png"
        print(cmd)
        os.system(cmd)
        print("1111")
