from rest_framework import serializers


class GetAllEmployeeProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    contact = serializers.CharField()
    joining_date = serializers.DateField()
    salary = serializers.CharField()
    address = serializers.CharField()
    department = serializers.CharField()
    position = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)


class CreateProfileRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    contact = serializers.CharField()
    joining_date = serializers.DateField()
    salary = serializers.CharField()
    address = serializers.CharField()
    department = serializers.CharField()
    position = serializers.CharField()


class CreateProfileResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    contact = serializers.CharField()
    joining_date = serializers.DateField()
    salary = serializers.CharField()
    address = serializers.CharField()
    department = serializers.CharField()
    position = serializers.CharField()


class GetAllleaveResponseserializer(serializers.Serializer):
    leave_code = serializers.CharField()
    profile = serializers.CharField()
    leave_type = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    reason = serializers.CharField()
    status = serializers.CharField()


class CreateLeaveRequestSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()
    leave_type = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    reason = serializers.CharField()


class CreateLeaveResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    leave_code = serializers.CharField()
    profile_id = serializers.IntegerField()
    leave_type = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    reason = serializers.CharField()
    status = serializers.CharField()


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class GetProfileResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    contact = serializers.CharField()
    joining_date = serializers.DateField()
    salary = serializers.CharField()
    address = serializers.CharField()
    department = serializers.CharField()
    position = serializers.CharField()


class GetleaveResponseserializer(serializers.Serializer):
    leave_code = serializers.CharField()
    profile = serializers.CharField()
    leave_type = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    reason = serializers.CharField()
    status = serializers.CharField()


class GetLeaveRangeRequestSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
