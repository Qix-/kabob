from unittest import TestCase

from kabob import _


class KabobTestCase(TestCase):
    def _T(self, obj, kbb):
        from kabob.wand import Kabob
        self.assertIsInstance(kbb, Kabob)
        return [x for x in kbb(obj)]


class TestKabob(KabobTestCase):
    def test_contains(self):
        fixture = [dict(bar=10), dict(bar=15), dict(foo=100), dict(bar=13), dict(barr=552)]

        self.assertEqual(self._T(fixture, _.contains('bar')), [
            dict(bar=10), dict(bar=15), dict(bar=13)])
        self.assertEqual(self._T(fixture, _.contains('foo')), [
            dict(foo=100)])
        self.assertEqual(self._T(fixture, _.contains('barr')), [
            dict(barr=552)])
        self.assertEqual(self._T(fixture, _.contains('foo', 'bar')), [])

    def test_getattr(self):
        class TestClass(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        fixture = [TestClass(10, 15), TestClass(4, 44), TestClass(19, 20)]

        self.assertEqual(self._T(fixture, _.x), [10, 4, 19])
        self.assertEqual(self._T(fixture, _.y), [15, 44, 20])

    def test_getattr_nested(self):
        class TestValue(object):
            def __init__(self, v):
                self.value = v

        class TestClass(object):
            def __init__(self, x, y):
                self.x = TestValue(x)
                self.y = TestValue(y)

        fixture = [TestClass(10, 15), TestClass(4, 44), TestClass(19, 20)]

        self.assertEqual(self._T(fixture, _.x.value), [10, 4, 19])
        self.assertEqual(self._T(fixture, _.y.value), [15, 44, 20])

    def test_getitem(self):
        fixture = [
            dict(bar=10, foo=15),
            dict(bar=65, foo=22),
            dict(bar=19, foo=11),
            dict(bar=99, foo=24)
        ]

        self.assertEqual(self._T(fixture, _['bar']), [10, 65, 19, 99])
        self.assertEqual(self._T(fixture, _['foo']), [15, 22, 11, 24])

    def test_or(self):
        fixture = [
            dict(foo=dict(bar=10)),
            dict(foo=dict(bar=15)),
            dict(foo=dict(bar=119)),
        ]

        self.assertEqual(self._T(fixture, _['foo'] | _['bar']), [10, 15, 119])

    def test_multi(self):
        fixture = [dict(bar=10), dict(bar=15), dict(foo=100), dict(bar=13), dict(barr=552)]

        self.assertEqual(self._T(fixture, _(_.contains('foo'), _.contains('bar'))), [
            dict(foo=100), dict(bar=10), dict(bar=15), dict(bar=13)])
        self.assertEqual(self._T(fixture, _(_.contains('foo'), _.contains('barr'))), [
            dict(foo=100), dict(barr=552)])
