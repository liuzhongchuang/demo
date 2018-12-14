# @Time    : 2018/12/3 0003 15:54
# @Author  : lzc
# @File    : face_photo_from_camera.py

#人脸识别库
import dlib
#数据处理库
import numpy as np
# 图片处理库opencv
import cv2
#读写文件流
import os
import shutil

#初始化dlib人脸检测器
detector = dlib.get_frontal_face_detector()

#初始化68 点特征预测器
predictor = dlib.shape_predictor('lib/shape_predictor_68_face_landmarks.dat')

#使用OpenCV调用摄像头
cap = cv2.VideoCapture(0)

#设置视频的大小参数
cap.set(3, 480)

#定义人脸头像的保存路径
face_path = 'data/data_face_photo_from_camera/'

# 定义当前人脸图像保存文件夹目录
current_face_dir = ''

#人脸图片截图次数
face_count = 0


# 每次启动的时候删除之前人脸识别图片的文件夹
def delFloder():
    folders_dir = os.listdir(face_path)
    for i in range(len(folders_dir)):
        shutil.rmtree(face_path + folders_dir[i])#有文件也会删除

#每次启动程序删除文件夹，不删出的话，可以屏蔽下面一行
delFloder()

#当摄像头打开的时候
while cap.isOpened():
    #默认摄像头640 x 480
    flag, img_rd = cap.read()

    # 接受外部一个输入命令
    kk = cv2.waitKey(1)
    #图片颜色空间转换函数，人脸图片
    img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)

    # 判断有多少个人脸
    faces = detector(img_gray, 0)

    #如果有不同的人脸分类，创建不同的文件夹n 表示新建, 现在假定一个人的头像放到一个文件夹里面
    if kk == ord('n'):
        current_face_dir = face_path + 'person_'+ str(face_count)
        # for dir in (os.listdir(face_path))
        os.mkdir(current_face_dir)
        print('创建新的人脸文件夹:',current_face_dir)

    font = cv2.FONT_HERSHEY_COMPLEX

    # 如果检测到人脸
    if len(faces) > 0:
        for k, d in enumerate(faces):
            #计算人脸矩形大小
            pos_start = tuple([d.left(), d.top()])
            pos_end = tuple([d.right(), d.bottom()])

            #计算矩形的宽高
            width = (d.right() - d.left())
            height = (d.bottom() - d.top())

            #设置矩形框框的颜色,默认正常情况是纯白色
            color_rec = (255, 255, 255)

            ww = int(width/2)
            hh = int(height/2)


            #判断人脸是否在矩形框框之中
            if (d.right() + ww > 640) or (d.bottom() + hh > 480) or (d.left() - ww) < 0 or (d.top() - hh < 0):
                # 在摄像机中显示超出范围的提示信息
                cv2.putText(img_rd, 'out of range',(20,300), font, 0.8, (255,255,255),1,cv2.LINE_AA)
                #如果人脸超出矩形框范围，那么修改框框颜色为纯红色
                color_rec = (0,0,255)
            else:
                color_rec = (255,255,255)


            #绘制任务头像框
            cv2.rectangle(img_rd, tuple([d.left() - ww, d.top() -hh]), tuple([d.right() + ww, d.bottom()+ hh]), color_rec,2)

            #根据人脸的大小绘制一张空图
            img_blank = np.zeros(( int(height*2),width*2 , 3),np.uint8)

            #如果按下了s键，那么保存摄像头中人脸图形到本地目录，路径就是上面新建的文件夹
            if kk == ord('s'):
                # 截一次图后，截图次数累计
                face_count=face_count+1
                for i in range(height * 2):
                    for j in range(width * 2):
                        img_blank[i][j] = img_rd[d.top() -hh +i][d.left() - ww +j]
                cv2.imwrite(current_face_dir+'/img_face_' + str(face_count)+'.jpg', img_blank)
                print('=======================图片写入本地')


    #在显示的摄像头窗口上增加一些文字说明
    cv2.putText(img_rd, 'Face Count'+str(len(faces)), (20, 20), font, 1, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.putText(img_rd, 'N:create Folder', (20, 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.putText(img_rd, 'S:Save Face Photo', (20, 80), font, 1, (0, 255, 0), 1, cv2.LINE_AA)


    #将摄像头窗口显示出来
    cv2.imshow('camera', img_rd)
