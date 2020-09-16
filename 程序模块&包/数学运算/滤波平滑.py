from scipy.signal import medfilt #中值滤波
from scipy.signal import savgol_filter #Savitzky-Golay 滤波

# Savitzky-Golay 滤波器实现曲线平滑
delA1 = savgol_filter(delA1, 501, 1) #501是窗口长度，该值需为正奇整数；1是对窗口内的数据点进行1阶多项式拟合

# 中值滤波是将每一点的值设置为该点某邻域窗口内的所有点的中值。这里的n就是邻域的大小
delA1 = medfilt(delA1,501) # n=501
