from django.shortcuts import render, redirect
from wms import models
from wms.utils.pagination import Pagination
from wms.utils.form import AdminModelForm


def admin_list(request):
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["username__contains"] = search_data

    queryset = models.Admin.objects.filter(**data_dict).order_by("-id")
    page_object = Pagination(request, queryset, page_size=2)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "search_data": search_data
    }
    return render(request, "admin_list.html", context)


# def admin_add(request):
#     title = "新建管理员"
#     if request.method == "GET":
#         form = AdminModelForm()
#         return render(request, "change.html", {"form": form, "title": title})

#     form = AdminModelForm(data=request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("/admin_list/")
#     return render(request, "change.html", {"form": form, "title": title})

#
# def admin_edit(request, nid):
#     row_object = models.Admin.objects.filter(id=nid).first()
#     if not row_object:
#         return redirect("/admin_list/")
#     title = "编辑管理员"
#
#     if request.method == "GET":
#         form = AdminModelForm(instance=row_object)
#         return render(request, "change.html", {"form": form, "title": title})
#     form = AdminModelForm(instance=row_object, data=request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("/admin_list/")
#     return render(request, "change.html", {"form": form, "title": title})
#
#
# def admin_delete(request, nid):
#     models.Admin.objects.filter(id=nid).delete()
#     return redirect("/admin_list/")
#
#
# def admin_reset(request, nid):
#     row_object = models.Admin.objects.filter(id=nid).first()
#     if not row_object:
#         return redirect("/admin_list/")
#     title = "重置密码 - {}".format(row_object.username)
#     if request.method == "GET":
#         form = AdminResetModelForm(instance=row_object)
#         return render(request, "change.html", {"form": form, "title": title})
#     form = AdminResetModelForm(instance=row_object, data=request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect("/admin_list/")
#     return render(request, "change.html", {"form": form, "title": title})
