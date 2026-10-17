import unittest

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_returns_json(self):
        self.assertStartsWith(emotion_detector(
            "Some neutral text.").strip(), "emotion_predictions")
