import cv2

test_img_01_loc = './training_images/training_01.jpg'


def process_image(file_loc):
    img = cv2.imread(file_loc, cv2.IMREAD_GRAYSCALE)
    blurred_img = cv2.bilateralFilter(img, 11, 21, 39)
    edge_img = cv2.Canny(blurred_img, 10, 20)
    return blurred_img, edge_img

test_img_01, edge_img_01 = process_image(test_img_01_loc)


while True:
    cv2.imshow('edge img 01', edge_img_01)
    cv2.waitKey(25)

# orb_orig = cv2.ORB_create()
# kp_orig = orb_orig.detect(test_img_04, None)
# kp_orig, des_orig = orb_orig.compute(test_img_04, kp_orig)
# kp_img_orig = cv2.drawKeypoints(test_img_04, kp_orig, None, color=(0,255,0), flags=0)

# orb_edge = cv2.ORB_create()
# kp_edge = orb_edge.detect(edge_img_04, None)
# kp_edge, des_edge = orb_edge.compute(edge_img_04, kp_edge)
# kp_img_edge = cv2.drawKeypoints(edge_img_04, kp_edge, None, color=(0,255,0), flags=0)

