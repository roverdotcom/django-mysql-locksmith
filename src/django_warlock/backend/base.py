from functools import wraps

from django.conf import settings
from django.db.backends.mysql import base


def warlock_enabled_property(func):
    @property
    @wraps(func)
    def wrapper(self):
        if getattr(settings, 'WARLOCK_ENABLED', False):
            return func(self)

        return getattr(
            super(WarlockSchemaEditor, self),
            func.__name__
        )
    return wrapper


class WarlockSchemaEditorMixin(object):
    @warlock_enabled_property
    def sql_create_column(self):
        return "ALTER TABLE %(table)s ADD COLUMN %(column)s %(definition)s, ALGORITHM=INPLACE, LOCK=NONE"

    @warlock_enabled_property
    def sql_create_fk(self):
        return (
            "ALTER TABLE %(table)s ADD CONSTRAINT %(name)s FOREIGN KEY"
            " (%(column)s) REFERENCES %(to_table)s (%(to_column)s)%(deferrable)s"
            ", ALGORITHM=INPLACE, LOCK=NONE"
        )


class WarlockSchemaEditor(WarlockSchemaEditorMixin, base.DatabaseSchemaEditor):
    pass


class WarlockDatabaseWrapperMixin(object):
    SchemaEditorClass = WarlockSchemaEditor


class DatabaseWrapper(
        WarlockDatabaseWrapperMixin,
        base.DatabaseWrapper):
    pass
