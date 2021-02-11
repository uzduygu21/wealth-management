import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.paginator import Paginator

from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Contact, Account, Quiz

# Create your views here.


def index(request):
    return render(request, "finance/index.html")


def questions(request):
    questions = Contact.objects.order_by("-contactdate").all()
    paginator = Paginator(questions, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "finance/questions.html", {'page_obj': page_obj})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "finance/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "finance/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "finance/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password,
                                            first_name=first_name, last_name=last_name)
            user.save()
        except IntegrityError:
            return render(request, "finance/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "finance/register.html")


@login_required
@csrf_exempt
def contact(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)
    data = json.loads(request.body.decode("utf-8"))
    question = data.get("question", "")
    name = request.user.get_full_name()
    email = request.user.email
    try:
        contact = Contact(name=name, email=email, question=question)
        contact.save()
    except:
        return render(request, "finance/login.html")
    return JsonResponse({"message": "Posted successfully."}, status=201)


@login_required
@csrf_exempt
def account(request):
    users = User.objects.all()

    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        accountnum = data.get("accountnum", "")
        amount = data.get("amount", "")
        bank = data.get("bank", "")
        user = request.user
        try:
            account = Account(accountnum=accountnum,
                              amount=amount, bank=bank, user=user)
            account.save()
        except:
            return render(request, "finance/login.html")
    accounts = Account.objects.filter(user=request.user)
    all_accounts = Account.objects.all()
    return render(request, "finance/client.html", {
        "users": users,
        "accounts": accounts,
        "all_accounts": all_accounts
    })


@login_required
@csrf_exempt
def quiz(request):
    quizes = Quiz.objects.order_by("-quizdate").all()
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        score = data.get("score", "")
        user = request.user
        try:
            q = Quiz(score=score, user=user)
            q.save()
        except:
            return render(request, "finance/login.html")
    return render(request, "finance/quiz.html", {
        "quizes": quizes
    })

@login_required
@csrf_exempt
def del_edit(request, account_id):
    account = Account.objects.filter(id=account_id).values()
    if request.method == "DELETE":
        Account.objects.filter(id=account_id).delete()
        return JsonResponse({
            "accounts": list(account)
        })
    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        acct = Account.objects.get(pk=account_id)
        accountnum = data.get("accountnum", "")
        bank = data.get("bank", "")
        amount = data.get("amount", "")
        try:
            acct.accountnum = accountnum
            acct.bank = bank
            acct.amount = amount
            acct.save()
        except:
            return render(request, "finance/client.html")
        return JsonResponse({
            "accounts": list(account)
        })
    else:
        return JsonResponse({
            "error": "DELETE or POST request required."
        }, status=400)
