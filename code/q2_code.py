# coding=gbk
import cv2  #����opencvģ��
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("test3.png")  #����ͼƬ��ͼƬ���ڳ�������Ŀ¼
cv2.imshow("img", img)

img_shape = img.shape  # ͼ���С(565, 650, 3)
print(img_shape)
h = img_shape[0]
w = img_shape[1]
# ��ɫͼ��ת��Ϊ�Ҷ�ͼ��3ͨ����Ϊ1ͨ����
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
# ���ͼ��Ҷ�ֵ��ȥԭͼ�񣬼��ɵõ���ת��ͼ��
gray = 255 - gray


#ʹ�þֲ���ֵ�Ĵ���㷨����ͼ���ֵ��
dst = cv2.adaptiveThreshold(gray,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,101, 1)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3, 3))#��̬ѧȥ��
dst=cv2.morphologyEx(dst,cv2.MORPH_OPEN,element)  #������ȥ��

contours, hierarchy = cv2.findContours(dst,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)  #������⺯��
cv2.drawContours(dst,contours,-1,(120,0,0),2)  #��������

count=0 #��������
ares_avrg=0  #����ƽ��
#�����ҵ������д���
for cont in contours:
    ares = cv2.contourArea(cont)#�����Χ��״�����
    if ares<80:   #�������С��10����״
        continue
    count+=1    #���������1
    ares_avrg+=ares
    print("{}-window:{}".format(count,ares),end="  ") #��ӡ��ÿ�����������
    rect = cv2.boundingRect(cont) #��ȡ��������
    print("x:{} y:{}".format(rect[0],rect[1]))#��ӡ����
    cv2.rectangle(img,rect,(255,0,255),1)#���ƾ���
    y=10 if rect[1]<10 else rect[1] #��ֹ��ŵ�ͼƬ֮��
    cv2.putText(img,str(count), (rect[0]+8, y+14), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 255), 1) #�ڴ������Ͻ�д�ϱ��


print("����ƽ�����:{}".format(round(ares_avrg/ares,2))) #��ӡ��ÿ�����������


cv2.namedWindow("imagshow", 2)   #����һ������
cv2.imshow('imagshow', img)    #��ʾԭʼͼƬ

cv2.namedWindow("dst", 2)   #����һ������
cv2.imshow("dst", dst)  #��ʾ�Ҷ�ͼ
cv2.imshow("img", img)

#plt.hist(gray.ravel(), 256, [0, 256]) #����Ҷ�ֱ��ͼ
#plt.show()


cv2.waitKey()
