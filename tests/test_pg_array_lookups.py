from django.test import TestCase
from .models import TestModel


class TestAll(TestCase):

    def test_exact_found(self):
        TestModel.objects.create(ints=[1, 1, 1])
        self.assertTrue(TestModel.objects.filter(ints__all=1))

    def test_exact_not_found(self):
        TestModel.objects.create(ints=[1, 1, 2])
        self.assertFalse(TestModel.objects.filter(ints__all=1))

    def test_lt_found(self):
        TestModel.objects.create(ints=[1, 2, 3])
        self.assertTrue(TestModel.objects.filter(ints__all__lt=4))

    def test_lt__not_found(self):
        TestModel.objects.create(ints=[1, 2, 3])
        self.assertFalse(TestModel.objects.filter(ints__all__lt=3))

    def test_gt_found(self):
        TestModel.objects.create(ints=[1, 2, 3])
        self.assertTrue(TestModel.objects.filter(ints__all__gt=0))

    def test_gt_not_found(self):
        TestModel.objects.create(ints=[1, 2, 3])
        self.assertFalse(TestModel.objects.filter(ints__all__gt=1))


class TestAny(TestCase):

    def setUp(self):
        TestModel.objects.create(ints=[1, 3, 5])

    def test_exact_found(self):
        self.assertTrue(TestModel.objects.filter(ints__any=1))

    def test_exact_not_found(self):
        self.assertFalse(TestModel.objects.filter(ints__any=2))

    def test_lt_found(self):
        self.assertTrue(TestModel.objects.filter(ints__any__lt=2))

    def test_lt__not_found(self):
        self.assertFalse(TestModel.objects.filter(ints__any__lt=1))

    def test_gt_found(self):
        self.assertTrue(TestModel.objects.filter(ints__any__gt=4))

    def test_gt_not_found(self):
        self.assertFalse(TestModel.objects.filter(ints__any__gt=5))
