import i_theta
import image_testing
from math import pi

if __name__ == '__main__':

	image = image_testing.get_image4()

	print("The original image was: ", image)
	size = len(image)

	angles = []
	# convert all rgb pixel values into angles in [0, pi/2]
	for i in range(size):
		for j in range(size):
			angles.append((image_testing.rgb_to_theta(image[i][j])))

	print("The angles for the original image: ", angles)

	new_angles = i_theta.run_4(angles)

	print("The returned angles are: ", new_angles)

	im = []
	i = 0
	# converting all the recovered angles, back into rgb values
	for ang in new_angles:

		rgb = image_testing.theta_to_rgb(ang)
		print(rgb)
		if (i % 4 == 0):
			row = []

		row.append(rgb)

		if (i % 4 == 3):
			im.append(row)

		i += 1

	new_image = image_testing.make_image(im)

	for i in range(6):
		new_image = image_testing.double_size4(new_image)

	image_testing.show_image(new_image, "Four_w16_100-000-000_SHIFTED")
	


