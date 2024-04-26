

# Define group permissions mapping
group_permission_mapping = [
    {
        "name": "attendance",
        "permissions": [
            "add_attendance"
            "view_attendance"
        ]
    },
]

permissions = [
    {
        "app_label": "attendances",
        "model": "attendance",
        "permissions": [
            {"name": "can view attendance", "codename": "attendance_view"},
            {"name": "can add attendance", "codename": "attendance_add"},
        ]
    }
]
