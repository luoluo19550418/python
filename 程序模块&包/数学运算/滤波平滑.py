from scipy.signal import medfilt #中值滤波
from scipy.signal import savgol_filter #Savitzky-Golay 滤波

# Savitzky-Golay 滤波器实现曲线平滑
delA1 = savgol_filter(delA1, 501, 1) #501是窗口长度，该值需为正奇整数；1是对窗口内的数据点进行1阶多项式拟合

# 中值滤波是将每一点的值设置为该点某邻域窗口内的所有点的中值。这里的n就是邻域的大小
delA1 = medfilt(delA1,501) # n=501


# 参考：
https://blog.csdn.net/weixin_42782150/article/details/107176500?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduend~default-2-107176500.nonecase&utm_term=python%E5%A6%82%E4%BD%95%E8%AE%A9%E6%9B%B2%E7%BA%BF%E5%B9%B3%E6%BB%91
https://www.zhihu.com/question/24079334
