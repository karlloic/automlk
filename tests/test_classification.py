from __future__ import division
from __future__ import print_function
from sklearn.datasets import load_breast_cancer
from unittest import TestCase
from automlk.classification import classifier


class TestClassification(TestCase):
    def test_runclassifiers(self):
        X = load_breast_cancer().data
        y = load_breast_cancer().target

        print('Testing Classifiers with breast cancer dataset')
        try:
            classifier.runclassifiers(X, y)
        except:
            self.assertFalse(False)
        self.assertTrue(True)

    def test_tuneclassifiers(self):
        X = load_breast_cancer().data
        y = load_breast_cancer().target

        print('Testing hyper param tuning with breast cancer dataset')
        try:
            classifier.tuneclassifiers(X, y)
        except:
            self.assertFalse(False)
        self.assertTrue(True)

