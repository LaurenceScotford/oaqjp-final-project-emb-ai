import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_joy(self): 
        self.assertEqual(emotion_detector("I am glad this happened")[0]["dominant_emotion"], "joy")

    def test_anger(self): 
        self.assertEqual(emotion_detector("I am really mad about this")[0]["dominant_emotion"], "anger")

    def test_disgust(self):
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")[0]["dominant_emotion"], "disgust")

    def test_sadness(self):
        self.assertEqual(emotion_detector("I am so sad about this")[0]["dominant_emotion"], "sadness")

    def test_fear(self):
        self.assertEqual(emotion_detector("I am really afraid that this will happen")[0]["dominant_emotion"], "fear")

unittest.main()
