from app import app
from StringIO import StringIO
from io import BytesIO
import unittest
import json
from flask import Request, Response

from werkzeug import FileStorage
from werkzeug.datastructures import MultiDict

class AppTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass

    def test_video_upload(self):

        response = self.app.post(
            '/upload',
            data={
                'file': file,
            },
            content_type='multipart/form-data'
        )

        resp = json.loads(response.data)
        self.assertIn("Uploaded", resp.get('status'))

    def test_video_upload_correct_extension(self):
        pass

    def test_video_upload_incorrect_extesion(self):
        pass

    def test_video_upload_size_check(self):
        pass

    def test_get_images(self):
        response = self.app.get(
            '/files',
            follow_redirects=True
        )

        resp = json.loads(response.data)
        print resp
        self.assertIn("OK", resp.get('status'))



if __name__ == "__main__":
    unittest.main()
