#encoding=utf-8
import qrcode
import time
'''
二维码制作完成后可以在这个地址：草料二维码扫描器   https://cli.im/deqr/  扫描显示变量rq中内容
下面这段话是用来控制二维码图像大小，像素等
QRCode参数详细说明：
version: 一个整数，范围为1到40，表示二维码的大小（最小值是1，是个12×12的矩阵），如果想让程序自动生成，将值设置为 None 并使用 fit=True 参数即可。
error_correction: 二维码的纠错范围，可以选择4个常量：
ERROR_CORRECT_L 7%以下的错误会被纠正
ERROR_CORRECT_M (default) 15%以下的错误会被纠正
ERROR_CORRECT_Q 25 %以下的错误会被纠正
ERROR_CORRECT_H. 30%以下的错误会被纠正
boxsize: 每个点（方块）中的像素个数
border: 二维码距图像外围边框距离，默认为4，而且相关规定最小为4
'''
#获取当前系统时间并格式化
sj = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#改成自己需要的格式，文字加上系统时间
rq = '制作日期为: '+sj
#本地路径变量
img_file = r'g:\tmp\own11.png'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2
)
qr.add_data(rq)
#qr.make(fit=True)
img = qr.make_image()
#图片保存到本地
img.save(img_file)
#显示二维码，微信扫一扫可以显示，http://jiema.wwei.cn/这个二维码在线扫出来的汉字为乱码
#img.show()