#-*-coding:utf-8-*-
#文件名: ch.py
# code from http://my.oschina.net/u/1180306/blog/279818
# Matplotlib输出中文显示问题
def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
    
    """
    use as:
    #-*-coding:utf-8-*-
    import ch
    ch.set_ch()
    from matplotlib import pyplot as plt
    plt.title(u'显示中文')
    plt.show()
    """