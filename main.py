import kmean
import easygui
from PIL import Image
import numpy as np

if __name__ == '__main__':
    image = Image.open('face.jpg')  # 200 * 220
    image.show()

    array = np.asarray(image, dtype='int64')
    rows = len(array)
    cols = len(array[0])

    flat_array = array.reshape(rows * cols, 3)
    k = int(easygui.enterbox("What should be the value of k?"))
    print("Value of k is", k)

    print("Applying Kmean...")
    centroids = (kmean.k_mean(flat_array.tolist(), k))

    print("Compressing...")
    flat_array = kmean.compress_image(centroids, flat_array.tolist())
    flat_array = np.array(flat_array)
    print("Done!")

    array = np.array(flat_array.reshape(rows, cols, 3))
    compressed_image = Image.fromarray(array.astype(np.uint8))
    compressed_image.show()
    compressed_image.save('compressed' + str(k) + '.jpg')
