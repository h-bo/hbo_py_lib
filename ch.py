#-*-coding:utf-8-*-
#�ļ���: ch.py
# code from http://my.oschina.net/u/1180306/blog/279818
# Matplotlib���������ʾ����
def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # ָ��Ĭ������
    mpl.rcParams['axes.unicode_minus'] = False # �������ͼ���Ǹ���'-'��ʾΪ���������
    
    """
    use as:
    #-*-coding:utf-8-*-
    import ch
    ch.set_ch()
    from matplotlib import pyplot as plt
    plt.title(u'��ʾ����')
    plt.show()
    """