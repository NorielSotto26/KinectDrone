import freenect
import cv2
import numpy as np
"""
Grabs a depth map from the Kinect sensor and creates an image from it.
"""
def getDepthMap():	
	depth, timestamp = freenect.sync_get_depth()
 
	np.clip(depth, 0, 2**10 - 1, depth)
	depth >>= 2
	depth = depth.astype(np.uint8)
 
	return depth

depth = getDepthMap()
cv2.imshow('image', depth)

col_size = depth[0].size
row_size = len(depth)

print("Column Size: " + str(col_size))
print("Row Size: " + str(row_size))

print("Press x to exit")

while True:
	depth = getDepthMap()
	
	cv2.imshow('Stream Screen', depth)
	keypress = cv2.waitKey(1)
	print(keypress)
	if (keypress == ord('s')):
		break

