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

col_size = depth[0].size
row_size = len(depth)

skip = 4
x_size = col_size/skip
y_size = row_size/skip
array_size = x_size*y_size
output_size = 2
output_values = ["1 0", "0 1"]
current_output = output_values[0];
captured_size = 0

print("Column Size: " + str(col_size))
print("Row Size: " + str(row_size))

print("\nPress c to capture")
print("Press x to exit")

dArray = np.zeros((int(y_size), int(x_size)), dtype=np.uint8)
cv2.imshow('Capture Screen', dArray)

while True:
	depth = getDepthMap()
	keypress = cv2.waitKey(10)

	# print(keypress)
	if (keypress == ord('1')):
		current_output = output_values[0];
		print("Capturing Take Off - 1 0")
	if (keypress == ord('2')):
		current_output = output_values[1];
		print("Capturing Landing - 0 1")
	if (keypress == ord('x')):
		file = open("output/output.txt","a") 
		file.write(str(captured_size) + " " + str(int(array_size)) + " " + str(output_size) + "\n")
		file.close()
		break
	if (keypress == ord('c')):
		print("Caputuring Image...")
		print("Image # " + str(captured_size+1))
		print("Column Size: " + str(dArray[0].size))
		print("Row Size: " + str(len(dArray)))
		print("Array Size: " + str(array_size)) 

		# COMPUTATION FOR THE SHRINKED ARRAY VALUES
		a=0
		for x in range(0,row_size-1,skip):
			b=0
			for y in range(0,col_size-1,skip):
				dArray[a][b] = int(depth[x][y])
				b=b+1
			a=a+1

		cv2.imshow('Capture Screen', dArray)

		file = open("output/output.txt","a")

		for data in dArray:
			for data_slice in data:
				file.write(str(data_slice)+ " ")
			# file.write(depth)
		file.write("\n" + current_output + "\n")

		file.close()

		captured_size = captured_size + 1

	cv2.imshow('Stream Screen', depth)

