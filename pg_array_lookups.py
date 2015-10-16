from django.contrib.postgres.fields import ArrayField
from django.db.models import Lookup, Transform

__author__ = 'Omar Khan'
__email__ = 'omar@omarkhan.me'
__version__ = '0.1.0'


@ArrayField.register_lookup
class All(Transform):
    lookup_name = 'all'

    def as_sql(self, compiler, connection):
        lhs, params = compiler.compile(self.lhs)
        return 'ALL ({0})'.format(lhs), params


@ArrayField.register_lookup
class Any(Transform):
    lookup_name = 'any'

    def as_sql(self, compiler, connection):
        lhs, params = compiler.compile(self.lhs)
        return 'ANY ({0})'.format(lhs), params


class BaseLookup(Lookup):
    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = rhs_params + lhs_params
        return '{0} {1} {2}'.format(rhs, self.operator, lhs), params


@All.register_lookup
@Any.register_lookup
class Exact(BaseLookup):
    lookup_name = 'exact'
    operator = '='


@All.register_lookup
@Any.register_lookup
class LessThan(BaseLookup):
    lookup_name = 'lt'
    operator = '>'


@All.register_lookup
@Any.register_lookup
class GreaterThan(BaseLookup):
    lookup_name = 'gt'
    operator = '<'
