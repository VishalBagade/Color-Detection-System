import cv2
import pandas as pd
import imutils

img_path=input("enter Image path")
clicked = False
r = g = b = x_pos = y_pos = 0
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)



def get_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


def onmouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

img=cv2.imread(img_path)
winname="Color Detection System"
cv2.namedWindow(winname,cv2.WINDOW_NORMAL)
cv2.setMouseCallback(winname, onmouse_click)

while True:
       
    cv2.imshow(winname,img)
    
    
    if clicked:

        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = get_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        
        if r + g + b <= 500:
            cv2.putText(img, text, (50, 50), 3, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        else:
            cv2.putText(img, text, (50, 50), 3, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # To break loop press q
    key=cv2.waitKey(20)
    if key==ord('q'):
        break
cv2.destroyAllWindows()