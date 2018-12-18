from django.shortcuts import render, redirect


def blog_redirect(request):
    return redirect("/", permanent=True)
