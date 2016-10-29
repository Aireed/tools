# -*- coding:utf-8 -*-
"""
---------------------------------------------------------------
File Name :  'table_2_image'.py
Description: 

Author:  'wangtao'
Date: '2016/10/29' '14:21'
---------------------------------------------------------------
"""
from PIL import Image, ImageFont, ImageDraw

def PIL_text_to_image():
    font = ImageFont.truetype("msyh.ttf", 18)

    # 1 读取数据，获取一个list
    datalist = [
        [8, "dreamweaver网页制作","王苗苗"],
        [8, "风控趣味运动会", "张春峰"],
        [8, "从逾期客户属性中提炼重审规划", "冯亭亭/王苗苗"],
    ]


    # 获取字符串的高度,
    line_height = font.getsize(datalist[0][1])[1]
    img_height = line_height * (len(datalist) + 1)

    # 由于图片宽度不确定大小，指定一个最大值
    max_width = 2000

    im = Image.new("RGB", (max_width, img_height), (255, 255, 255))
    dr = ImageDraw.Draw(im)

    # 初始坐标,
    x = [5, 70, 700,]   # 每一个数字代表每一个字段的起始x, 需要的时候根据实际情况往后调
    y = 5

    # 遍历要打印的数据，一行一行的划
    for fields in datalist:
        for idx, item in enumerate(fields):
            newitem = "|{0}".format(item)
            dr.text((x[idx], y), newitem.decode("utf-8"), font=font, fill="#000000")
        # 行高加一下
        y += line_height

    im.save(r"E:\pygame_jpg\1.1.jpg")

if __name__ == "__main__":
    PIL_text_to_image()