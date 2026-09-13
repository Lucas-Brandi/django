from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def _style_form(form):
    for field in form.fields.values():
        css = field.widget.attrs.get("class", "")
        field.widget.attrs["class"] = f"{css} form-control".strip()
    return form


def register(request):
    if request.method == "POST":
        form = _style_form(UserCreationForm(request.POST))
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created.")
            form = _style_form(UserCreationForm())
    else:
        form = _style_form(UserCreationForm())

    return render(
        request,
        "users/register.html",
        {
            "form": form,
            "title": "Register",
        },
    )
