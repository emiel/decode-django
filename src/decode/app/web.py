import re

from django import forms
from django.contrib import messages
from django.core.validators import RegexValidator
from django.shortcuts import render

from .api_client import ApiClient


input_re = re.compile(r"^[1-9]+$")


class DecodeForm(forms.Form):

    input_str = forms.CharField(
        label="Input", max_length=30, validators=[RegexValidator(regex=input_re)]
    )


def _process(input_str, request):
    result = []
    api_client = ApiClient()

    try:
        response = api_client.decode(input_str)
    except Exception as err:
        messages.error(request, str(err))
    else:
        if response.status_code == 200:
            result = response.json()["result"]
        elif response.status_code == 400:
            messages.info(request, "Invalid input: {}".format(input_str))

    return result


def decode(request):
    result = []

    if request.method == "POST":
        form = DecodeForm(request.POST)
        if form.is_valid():
            input_str = form.cleaned_data["input_str"]
            result = _process(input_str, request)

    else:
        form = DecodeForm()

    return render(request, "app/index.html", {"form": form, "result": result})
