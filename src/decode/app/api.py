import re

from django.http import JsonResponse

from . import codec

input_re = re.compile(r"^\d+$")


def decode(request):
    """
    Decode endpoint
    """
    input = request.GET.get("input", "")

    match = input_re.match(input)
    if match:
        result = list(codec.decode(input))
        return JsonResponse({"result": result})
    else:
        return JsonResponse({"error": "invalid input"}, status=400)
