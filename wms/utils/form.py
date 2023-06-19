from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from wms import models
from wms.utils.bootstrap import BootStrapModelForm
from wms.utils.encrypt import md5


# class UserModelForm(BootStrapModelForm):
#     name = forms.CharField(min_length=3, label="用户名")
#
#     class Meta:
#         model = models.UserInfo
#         fields = ["name", "password", "age", 'account', 'create_time', "gender", "depart"]
#
#
# class PrettyModelForm(BootStrapModelForm):
#     mobile = forms.CharField(
#         label="手机号",
#         validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
#     )
#
#     class Meta:
#         model = models.PrettyNum
#         fields = ["mobile", "price", "level", "status"]
#
#     def clean_mobile(self):
#         text_mobile = self.cleaned_data["mobile"]
#         exists = models.PrettyNum.objects.filter(mobile=text_mobile).exists()
#         if exists:
#             raise ValidationError
#         return text_mobile
#
#
# class DepartModelForm(BootStrapModelForm):
#     title = forms.CharField(label="部门", max_length=8)
#
#     class Meta:
#         model = models.Department
#         fields = ["title"]
#
#
class AdminModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = "__all__"

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        # return md5(pwd)
        return pwd
#
#
# class AdminResetModelForm(BootStrapModelForm):
#     confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput(render_value=True))
#
#     class Meta:
#         model = models.Admin
#         fields = ["password", "confirm_password"]
#         widgets = {"password": forms.PasswordInput(render_value=True)}
#
#     def clean_password(self):
#         pwd = self.cleaned_data.get("password")
#         md5_pwd = md5(pwd)
#         exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd)
#         if exists:
#             raise ValidationError("密码与以前的密码相同")
#         return md5_pwd
#
#     def clean_confirm_password(self):
#         pwd = self.cleaned_data.get("password")
#         confirm = md5(self.cleaned_data.get("confirm_password"))
#         if confirm != pwd:
#             raise ValidationError("密码不一致")
#
#
# class AccountModelForm(BootStrapModelForm):
#     username = forms.CharField(
#         label="用户名",
#         widget=forms.TextInput,
#         required=True
#     )
#     password = forms.CharField(
#         label="密码",
#         widget=forms.PasswordInput,
#         required=True
#     )
#     code = forms.CharField(
#         label="验证码",
#         widget=forms.TextInput,
#         required=True
#     )
#
#     class Meta:
#         model = models.Admin
#         fields = ["username", "password", "code"]
#
#     def clean_password(self):
#         pwd = self.cleaned_data.get("password")
#         return md5(pwd)
#
#
# class TaskModelForm(BootStrapModelForm):
#     class Meta:
#         model = models.Task
#         fields = "__all__"
#         widgets = {
#             "detail": forms.TextInput
#         }
#
#
# class OrderModelForm(BootStrapModelForm):
#     class Meta:
#         model = models.Order
#         exclude = ["oid", "admin"]
#
#
# class CityModelForm(BootStrapModelForm):
#     bootstrap_fields = ['img']
#
#     class Meta:
#         model = models.City
#         fields = "__all__"
