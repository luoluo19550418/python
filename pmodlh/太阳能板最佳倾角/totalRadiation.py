# totalRadiation.py

import numpy as np

def Gt(beta, n, bjtime, lloc, psi):
	lst = 120; Gsc = 1353; rho = 0.2; h = 3.2

	B = (360 * (n - 81)) / 364
	E = 9.87 * np.sin(np.radians(2 * B)) - 7.53 * np.cos(np.radians(B)) - 1.5 * np.sin(np.radians(B))
	E = E / 60 #min convert hour

	if bjtime == 1:
		bjtime = 25
	loctime = bjtime + E + (lloc - lst) / 15 #真太阳时：当地时间
	omega = 15 * (loctime - 12) #太阳时角

	delta = 23.45 * np.sin(np.radians(360 * (284 + n) / 365)) #太阳赤纬角
	cosAlpha = np.sin(delta * (np.pi/180)) * np.sin(psi * (np.pi/180)) + np.cos(delta * (np.pi/180)) * np.cos(psi * (np.pi/180)) * np.cos(omega * (np.pi/180)) #太阳天顶角

	#大气外
	Gon = Gsc * (1 + 0.033 * np.cos(np.radians((360 * n) / 365))) #大气外总辐射
	G0 = Gon * cosAlpha #大气外切平面

	#水平面
	a0 = 0.4237 - 0.00821 * (6-h)**2
	a1 = 0.5055 - 0.00595 * (6.5-h)**2
	k = 0.2711 - 0.01858 * (2.5-h)**2
	taub = a0 + a1 * np.exp(-k / cosAlpha) #直射透过比
	taud = 0.2710 - 0.293 * taub #散射透过比
	Gcb = G0 * taub #直接辐射
	Gcd = G0 * taud #散射辐射
	G = Gcd + Gcb #水平面

	#倾斜面
	omega_s = np.arccos(-np.tan(np.radians(psi)) * np.sin(np.radians(delta))) #水平面日落时角
	omega_st = min([omega_s, np.arccos(-np.tan(np.radians(psi-beta)) * np.sin(np.radians(delta)))]) #倾斜面日落时角
	Rb = (np.cos(np.radians(psi - beta)) * np.cos(np.radians(delta)) * np.sin(np.radians(omega_st)) + np.radians(omega_st) * np.sin(np.radians(psi - beta)) * np.sin(np.radians(delta))) / (np.cos(np.radians(psi)) * np.cos(np.radians(delta)) * np.sin(np.radians(omega_s)) + np.radians(omega_s) * np.sin(np.radians(psi)) * np.sin(np.radians(delta)))
	Rd = (1 + np.cos(np.radians(beta))) / 2
	Rrho = (rho * (1 - np.cos(np.radians(beta)))) / 2
	Gt = Gcb * Rb + Gcd * Rd + G * Rrho

	return Gt
