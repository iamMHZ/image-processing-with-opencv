from HazmatDetector import HazmatDetector

detector = HazmatDetector()

detector.read_templates(
    'D:\Programming\Python-Workpace\BigProject\patternRecognition\hazmatDetection\hazmatImagetemplates')

detector.start_live_hazmat_detection(0)
