from django.contrib.auth.models import User
from django.db import connection
from django.db import models
from django.test import TestCase
from django.test.utils import override_settings

from django_warlock.backend.base import WarlockSchemaEditor

from .factories import UserFactory


class BackendBasicTests(TestCase):
    def test_backend_smoke_test(self):
        self.assertIsInstance(UserFactory.create(), User)


class SchemaEditorIntegrationTests(TestCase):
    def test_schema_editor_is_the_correct_class(self):
        self.assertIsInstance(connection.schema_editor(), WarlockSchemaEditor)

    def add_field_statements(self):
        new_field = models.NullBooleanField()
        new_field.set_attributes_from_name("has_dog")
        with connection.schema_editor(collect_sql=True) as editor:
            editor.add_field(User, new_field)
        return editor.collected_sql

    def test_create_column_sql(self):
        self.assertEqual(
            self.add_field_statements(),
            [u'ALTER TABLE `auth_user` ADD COLUMN `has_dog` bool NULL;'],
        )

    @override_settings(WARLOCK_ENABLED=True)
    def test_create_column_sql_warlock(self):
        self.assertEqual(
            self.add_field_statements(),
            [u'ALTER TABLE `auth_user` ADD COLUMN `has_dog` bool NULL, ALGORITHM=INPLACE, LOCK=NONE;'],
        )

    def add_foreign_key_statements(self):
        new_field = models.ForeignKey(
            User,
            related_name='children',
            on_delete=models.deletion.CASCADE,
        )
        new_field.set_attributes_from_name("father")
        with connection.schema_editor(collect_sql=True) as editor:
            editor.add_field(User, new_field)
        return editor.collected_sql

    def test_add_foreign_key(self):
        self.assertEqual(
            self.add_foreign_key_statements(),
            [
                'ALTER TABLE `auth_user` ADD COLUMN `father_id` integer NOT NULL;',
                'ALTER TABLE `auth_user` ADD CONSTRAINT'
                ' `auth_user_father_id_ce759166_fk_auth_user_id` FOREIGN KEY (`father_id`)'
                ' REFERENCES `auth_user` (`id`);'
            ],
        )

    @override_settings(WARLOCK_ENABLED=True)
    def test_create_column_sql_warlock(self):
        self.assertEqual(
            self.add_foreign_key_statements(),
            [
                'ALTER TABLE `auth_user` ADD COLUMN `father_id` integer NOT NULL'
                ', ALGORITHM=INPLACE, LOCK=NONE;',
                'ALTER TABLE `auth_user` ADD CONSTRAINT'
                ' `auth_user_father_id_ce759166_fk_auth_user_id` FOREIGN KEY (`father_id`)'
                ' REFERENCES `auth_user` (`id`), ALGORITHM=INPLACE, LOCK=NONE;'
            ],
        )
