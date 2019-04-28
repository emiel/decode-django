import re

from django import forms
from django.core.validators import RegexValidator
from django.shortcuts import render


input_re = re.compile(r"^[1-9]+$")


class DecodeForm(forms.Form):

    input_str = forms.CharField(
        label="Input", max_length=30, validators=[RegexValidator(regex=input_re)]
    )


def decode(request):
    result = None

    if request.method == "POST":
        form = DecodeForm(request.POST)
        if form.is_valid():
            input_str = form.cleaned_data["input_str"]
            result = input_str
    else:
        form = DecodeForm()

    return render(request, "app/index.html", {"form": form, "result": result})
