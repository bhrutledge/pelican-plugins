import os
import unittest
import img_class

from PIL import Image


class ImgClassTest(unittest.TestCase):

    def get_img_path(self, filename):
        return os.path.join(
            os.path.dirname(__file__), 'test_data', filename)

    def test_portrait(self):
        orientation = img_class.get_orientation(Image.new('RGB', (100, 200)))
        self.assertEqual(orientation, 'portrait')

    def test_landscape(self):
        orientation = img_class.get_orientation(Image.new('RGB', (200, 100)))
        self.assertEqual(orientation, 'landscape')

    def test_content(self):
        pass
        # actual = img_class.add_classes(content)
        # self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()

