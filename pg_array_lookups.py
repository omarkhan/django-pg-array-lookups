from django.contrib.postgres.fields import ArrayField
from django.db.models import Lookup, Transform, lookups

__author__ = 'Omar Khan'
__email__ = 'omar@omarkhan.me'
__version__ = '0.1.1'


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


class AnyStringMatcherMixin(object):
    def matcher(self, alias):
        return alias

    def as_sql(self, compiler, connection):
        lhs, lhs_params = compiler.compile(self.lhs.lhs)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        rhs = self.get_rhs_op(connection, rhs)
        params = lhs_params + rhs_params
        query = '(SELECT EXISTS(SELECT * FROM UNNEST({0}) AS val WHERE {1} {2}))'
        return query.format(lhs, self.matcher('val'), rhs), params


class AllStringMatcherMixin(object):
    def matcher(self, alias):
        return alias

    def as_sql(self, compiler, connection):
        lhs, lhs_params = compiler.compile(self.lhs.lhs)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        rhs = self.get_rhs_op(connection, rhs)
        params = lhs_params + rhs_params
        query = '(SELECT NOT EXISTS(SELECT * FROM UNNEST({0}) AS val WHERE {1} NOT {2}))'
        return query.format(lhs, self.matcher('val'), rhs), params


class CaseInsensitiveMixin(object):
    def matcher(self, alias):
        return 'UPPER({0})'.format(alias)


@Any.register_lookup
class AnyContains(AnyStringMatcherMixin, lookups.Contains):
    pass


@All.register_lookup
class AllContains(AllStringMatcherMixin, lookups.Contains):
    pass


@Any.register_lookup
class AnyIContains(CaseInsensitiveMixin, AnyStringMatcherMixin,
                   lookups.IContains):
    pass


@All.register_lookup
class AllIContains(CaseInsensitiveMixin, AllStringMatcherMixin,
                   lookups.IContains):
    pass


@Any.register_lookup
class AnyStartsWith(AnyStringMatcherMixin, lookups.StartsWith):
    pass


@All.register_lookup
class AllStartsWith(AllStringMatcherMixin, lookups.StartsWith):
    pass


@Any.register_lookup
class AnyIStartsWith(CaseInsensitiveMixin, AnyStringMatcherMixin,
                     lookups.IStartsWith):
    pass


@All.register_lookup
class AllIStartsWith(CaseInsensitiveMixin, AllStringMatcherMixin,
                     lookups.IStartsWith):
    pass


@Any.register_lookup
class AnyEndsWith(AnyStringMatcherMixin, lookups.EndsWith):
    pass


@All.register_lookup
class AllEndsWith(AllStringMatcherMixin, lookups.EndsWith):
    pass


@Any.register_lookup
class AnyIEndsWith(CaseInsensitiveMixin, AnyStringMatcherMixin,
                   lookups.IEndsWith):
    pass


@All.register_lookup
class AllIEndsWith(CaseInsensitiveMixin, AllStringMatcherMixin,
                   lookups.IEndsWith):
    pass
