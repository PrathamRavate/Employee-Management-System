from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError
from attendances.fixtures.fixture_mapping import (
    group_permission_mapping,
    permissions
    )


class Command(BaseCommand):
    help = 'Create groups, permissions and map permissions to group'

    def handle(self, *args, **options):
        # Create groups and permissions
        for group_data in group_permission_mapping:
            group_name = group_data['name']
            group, created = Group.objects.get_or_create(name=group_name)

            for permission_data in permissions:
                content_type = ContentType.objects.get(
                    app_label=permission_data['app_label'],
                    model=permission_data['model']
                )
                for permission in permission_data['permissions']:
                    try:
                        perm, created = Permission.objects.get_or_create(
                            codename=permission['codename'],
                            name=permission['name'],
                            content_type=content_type
                        )
                    except IntegrityError:
                        self.stdout.write(self.style.WARNING(f"Permission '{permission['name']}' already exists."))

        # Map permissions to groups
        for group_data in group_permission_mapping:
            group = Group.objects.get(name=group_data['name'])
            group_permissions = group_data['permissions']
            permissions_to_add = Permission.objects.filter(codename__in=group_permissions)
            group.permissions.add(*permissions_to_add)
