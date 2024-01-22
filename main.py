import cv2

image = cv2.imread('img2/RF4.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)

contours, _= cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_image = image.copy()

for contour in contours:
    
    moments = cv2.moments(contour)
    
    if moments["m00"] != 0:
        
        cX = int(moments["m10"] / moments["m00"])
        cY = int(moments["m01"] / moments["m00"])
        
        cv2.circle(contour_image, (cX, cY), 5, (0, 0, 0), -1)
        
        cv2.putText(contour_image, f"({cX}, {cY})", (cX - 50, cY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

cv2.imshow('Image with Contours', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()









