from django.shortcuts import render

# Create your views here.
def help(request):
    help_dict = {
        "help_msg" : "How can we help you?",
    }
    return render(request, "HelpApp/index.html", context=help_dict)