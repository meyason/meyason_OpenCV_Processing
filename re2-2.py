#パッケージの継承
import cv2
import numpy as np

#画像の読み込み
img1 = cv2.imread("rand.png")
img2 = cv2.imread("tem.png")

#グレースケール化
img_R = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img_T = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#8bitから64bitに
R = np.float64(img_R)
T = np.float64(img_T)

#ZNCC
Ta = T - np.average(T)

#ZNCCの最大値を求めるための評価値
RzP = 0 #初期値0

#ラスタスキャン
for i in range(70):
    for j in range(70):
        
        #類似度マップによる評価画像の切り出し
        RC = R[j:j+21, i:i+31]
        Ra = RC - np.average(RC)
        
        RzC = np.sum(Ra*Ta) / np.sqrt(np.sum(Ra**2))\
                            / np.sqrt(np.sum(Ta**2))
        
        #RzCが最大値なら座標と評価値更新
        if RzC>RzP:
            Xt = i
            Yt = j
            RzP = RzC
        
        #OpenCVを用いたやり方
        #
        #Rmap[i, j] = RzC
        #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(Rmap)
        #Xt = max_loc[0]
        #Yt = max_loc[1]
        
print("Xt, Yt", Xt, Yt)

                
            
            
        