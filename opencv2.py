import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,  400)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

window_name = "gamma correction"
trackbar_name_gamma = "gamma"
window_name_blur = "gaussian blur"
trackbar_name_gaussian = "gaussian"
window_name_color = "color tone"
trackbar_name_H = "R"
trackbar_name_S = "G"
trackbar_name_V = "B"
window_size = cv2.WINDOW_NORMAL

# gamma correction
cv2.namedWindow(window_name, window_size) # create win with win name
# gamma track bar
cv2.createTrackbar(trackbar_name_gamma, window_name, 1, 50, nothing)
# cv2.setTrackbarPos(trackbar_name_gamma, window_name, 10)
# gaussian blur
cv2.namedWindow(window_name_blur, window_size) # create win with win name
# gaussian blur track bar
cv2.createTrackbar(trackbar_name_gaussian, window_name_blur, 0, 50, nothing)
# cv2.setTrackbarPos(trackbar_name_gaussian, window_name_blur, 1)

# color tone
cv2.namedWindow(window_name_color, window_size) # create win with win name
# color tone R track bar
cv2.createTrackbar(trackbar_name_H, window_name_color, 1, 255, nothing)
# color tone G track bar
cv2.createTrackbar(trackbar_name_S, window_name_color, 1, 255, nothing)
# color tone B track bar
cv2.createTrackbar(trackbar_name_V, window_name_color, 1, 255, nothing)

while(True):

    ret, frame = cap.read()
    if not ret: continue

    # gamma
    gamma = cv2.getTrackbarPos(trackbar_name_gamma, window_name) * 0.1
    if gamma == 0.0:
        gamma = 0.1
        cv2.setTrackbarPos(trackbar_name_gamma, window_name, 1)
    # look up table for gammma
    look_up_table = np.zeros((256, 1), dtype = "uint8")
    for i in range(len(look_up_table)):
        look_up_table[i][0] = (len(look_up_table)-1) * pow(float(i) / (len(look_up_table)-1), 1.0 / gamma)
    # look up table gamma correction
    gamma_correction_img = cv2.LUT(frame, look_up_table)

    # gaussian blur
    gaussian = cv2.getTrackbarPos(trackbar_name_gaussian, window_name_blur)
    if gaussian % 2 == 0:
        gaussian = gaussian + 1
        # cv2.setTrackbarPos(trackbar_name_gaussian, window_name_blur, 1)
    blur_img = cv2.GaussianBlur(frame, (gaussian, gaussian), 0)

    # color tone
    r = cv2.getTrackbarPos(trackbar_name_H, window_name_color)
    g = cv2.getTrackbarPos(trackbar_name_S, window_name_color)
    b = cv2.getTrackbarPos(trackbar_name_V, window_name_color)
    bgr_img = cv2.split(frame)
    color_tone_img = cv2.merge((bgr_img[0]*(g/255), bgr_img[1]*(b/255), bgr_img[2]*(r/255)))
    # display gamma in window
    # cv2.putText(gamma_correction_img, "gamma:" + str(gamma), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0),2)

    cv2.imshow(window_name, gamma_correction_img)  # show in the win
    cv2.imshow(window_name_blur, blur_img)
    cv2.imshow(window_name_color, color_tone_img)

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()
