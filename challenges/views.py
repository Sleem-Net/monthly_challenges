from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "No alcohol this month! ",
    "february":"No alcohol this month! "  ,
    "march":"No alcohol this month! ",
    "april":"No alcohol this month! ",
    "may":"More excercise this month! ",
    "june":"More running this month! ",
    "july":"More Food this month! ",
    "october":"More Python this month! ",
    "november":"No meat this month! ",
    "december": None
    
}

# Create your views here.
def index(request):
    list_items= ""
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{ capitalized_month }</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

    
    # return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound('<h1>This is not a valid month</h1>')
        


    