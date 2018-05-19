from django.http import JsonResponse


def check_data(data):
    for key, value in data.items():
        if value == '' or value is None:
            return True, key
    return False, ''
