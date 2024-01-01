from django.shortcuts import render
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
from django.http import HttpResponse, JsonResponse


def index(request):
    prods = []
    categories = Product.objects.values("category")
    cats = {item["category"] for item in categories}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil(n / 4 - n // 4)
        prods.append([prod, range(1, nSlides), nSlides])

    dic = {"allProds": prods}
    return render(request, "shop/shop.html", dic)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        desc = request.POST["desc"]

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        try:
            updates = []
            updates.append({"name": name, "email": email})
            response = json.dumps(updates, default=str)
            return HttpResponse(response)

        except Exception as e:
            print("Error:", e)
            return HttpResponse("{}")

    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == "POST":
        orderId = request.POST["orderId"]
        email = request.POST["email"]
        print(orderId, email)
        data = {}
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if order.exists():
                orderUpdate = OrderUpdate.objects.filter(order_id=orderId)
                updates = []

                for item in orderUpdate:
                    updates.append({
                            "desc": item.update_desc,
                            "time": item.timestamp
                         })

                data["updates"] = updates
                data["order"] = order.first().items_json
                print(data)
                return JsonResponse(data)
            return JsonResponse({})

        except Exception as e:
            print("ERROR:", e)
            return JsonResponse({})

    return render(request, "shop/tracker.html")


def queryMatch(query, p):
    if (
        query.lower() in p.product_name.lower()
        or query in p.desc.lower()
        or query in p.subcategory.lower()
        or query in p.category.lower()
    ):
        return True
    return False


def search(request):
    categories = Product.objects.values("category")
    cats = {item["category"] for item in categories}
    if request.method == "POST":
        query = request.POST["search"]
        products = Product.objects.all()

        for p in products:
            if (
                query.lower() in p.product_name.lower()
                or query in p.desc.lower()
                or query in p.subcategory.lower()
                or query in p.category.lower()
            ):
                cats.add(p)

        print(cats)

    prods = []

    for cat in cats:
        product = Product.objects.filter(category=cat)
        prod = [p for p in product if queryMatch(query, p)]

        n = len(prod)
        nSlides = n // 4 + ceil(n / 4 - n // 4)

        if len(prod) != 0:
            prods.append([prod, range(1, nSlides), nSlides])

    dic = {"allProds": prods}

    return render(request, "shop/search.html", dic)


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "shop/prodView.html", {"product": product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get("itemsJson", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        amount = request.POST.get("amount", "")
        address = (
            request.POST.get("address1", "") + " " + request.POST.get("address2", "")
        )
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")
        phone = request.POST.get("phone", "")

        amount = int(amount)

        order = Order(
            items_json=items_json,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone,
            amount=amount,
        )
        order.save()
        thank = True
        id = order.order_id
        update_desc = "Your Order has been Placed!"
        orderUpdate = OrderUpdate.objects.create(order_id=id, update_desc=update_desc)
        orderUpdate.save()
        return render(request, "shop/checkout.html", {"thank": thank, "id": id})
    return render(request, "shop/checkout.html")
