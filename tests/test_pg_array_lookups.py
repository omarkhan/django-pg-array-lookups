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

    def test_contains_found(self):
        TestModel.objects.create(strings=['spanish', 'inquisition'])
        self.assertTrue(TestModel.objects.filter(strings__all__contains='is'))

    def test_contains_not_found(self):
        TestModel.objects.create(strings=['spanish', 'inquisition'])
        self.assertFalse(TestModel.objects.filter(strings__all__contains='nish'))

    def test_icontains_found(self):
        TestModel.objects.create(strings=['SPANISH', 'inquisition'])
        self.assertTrue(TestModel.objects.filter(strings__all__icontains='is'))

    def test_icontains_not_found(self):
        TestModel.objects.create(strings=['SPANISH', 'inquisition'])
        self.assertFalse(TestModel.objects.filter(strings__all__icontains='nish'))

    def test_startswith_found(self):
        TestModel.objects.create(strings=['spam', 'spam and eggs'])
        self.assertTrue(TestModel.objects.filter(strings__all__startswith='spam'))

    def test_startswith_not_found(self):
        TestModel.objects.create(strings=['spam', 'eggs'])
        self.assertFalse(TestModel.objects.filter(strings__all__startswith='spam'))

    def test_istartswith_found(self):
        TestModel.objects.create(strings=['SPAM', 'spam and eggs'])
        self.assertTrue(TestModel.objects.filter(strings__all__istartswith='spam'))

    def test_istartswith_not_found(self):
        TestModel.objects.create(strings=['SPAM', 'eggs'])
        self.assertFalse(TestModel.objects.filter(strings__all__istartswith='spam'))

    def test_endswith_found(self):
        TestModel.objects.create(strings=['spam', 'ham'])
        self.assertTrue(TestModel.objects.filter(strings__all__endswith='am'))

    def test_endswith_not_found(self):
        TestModel.objects.create(strings=['spam', 'eggs'])
        self.assertFalse(TestModel.objects.filter(strings__all__endswith='am'))

    def test_iendswith_found(self):
        TestModel.objects.create(strings=['SPAM', 'ham'])
        self.assertTrue(TestModel.objects.filter(strings__all__iendswith='am'))

    def test_iendswith_not_found(self):
        TestModel.objects.create(strings=['SPAM', 'eggs'])
        self.assertFalse(TestModel.objects.filter(strings__all__iendswith='am'))


class TestAny(TestCase):

    def test_exact_found(self):
        TestModel.objects.create(ints=[1, 3, 5])
        self.assertTrue(TestModel.objects.filter(ints__any=1))

    def test_exact_not_found(self):
        TestModel.objects.create(ints=[1, 3, 5])
        self.assertFalse(TestModel.objects.filter(ints__any=2))

    def test_lt_found(self):
        TestModel.objects.create(ints=[1, 3, 5])
        self.assertTrue(TestModel.objects.filter(ints__any__lt=2))

    def test_lt__not_found(self):
        TestModel.objects.create(ints=[1, 3, 5])
        self.assertFalse(TestModel.objects.filter(ints__any__lt=1))

    def test_gt_found(self):
        TestModel.objects.create(ints=[1, 3, 5])
        self.assertTrue(TestModel.objects.filter(ints__any__gt=4))

    def test_gt_not_found(self):
        TestModel.objects.create(ints=[1, 3, 5])
        self.assertFalse(TestModel.objects.filter(ints__any__gt=5))

    def test_contains_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertTrue(TestModel.objects.filter(strings__any__contains='arr'))

    def test_contains_not_found(self):
        TestModel.objects.create(strings=['DEAD', 'PARROT'])
        self.assertFalse(TestModel.objects.filter(strings__any__contains='arr'))

    def test_icontains_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertTrue(TestModel.objects.filter(strings__any__icontains='ARR'))

    def test_icontains_not_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertFalse(TestModel.objects.filter(strings__any__icontains='shrubbery'))

    def test_startswith_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertTrue(TestModel.objects.filter(strings__any__startswith='par'))

    def test_startswith_not_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertFalse(TestModel.objects.filter(strings__any__startswith='PAR'))
        self.assertFalse(TestModel.objects.filter(strings__any__startswith='arr'))

    def test_istartswith_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertTrue(TestModel.objects.filter(strings__any__istartswith='PAR'))

    def test_istartswith_not_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertFalse(TestModel.objects.filter(strings__any__istartswith='ARR'))

    def test_endswith_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertTrue(TestModel.objects.filter(strings__any__endswith='rot'))

    def test_endswith_not_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertFalse(TestModel.objects.filter(strings__any__endswith='ROT'))
        self.assertFalse(TestModel.objects.filter(strings__any__endswith='arr'))

    def test_iendswith_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertTrue(TestModel.objects.filter(strings__any__iendswith='ROT'))

    def test_iendswith_not_found(self):
        TestModel.objects.create(strings=['dead', 'parrot'])
        self.assertFalse(TestModel.objects.filter(strings__any__iendswith='ARR'))
