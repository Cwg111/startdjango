from django import forms
from django.core import validators


class MessageBoardForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        min_length=2,
        label="标题",
        error_messages={
            "min_length": "标题最小长度不能小于2个",
            "max_length": "标题最大长度不能大于20个",
        },
    )
    content = forms.CharField(widget=forms.Textarea, label="内容")
    email = forms.EmailField(label="邮箱")


class RegisterForm(forms.Form):
    telephone = forms.CharField(
        validators=[validators.RegexValidator(r"^1[3-9]\d{9}$", "手机号码格式错误")]
    )
    pwd1=forms.CharField(min_length=6,max_length=16,label="密码")
    pwd2=forms.CharField(min_length=6,max_length=16,label="确认密码")
    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")
        if telephone == "19894239272":
            raise forms.ValidationError("手机号码已存在")
        else:
            return telephone
    
    def clean(self):
        # 调用父类的clean方法
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("pwd1")
        pwd2 = cleaned_data.get("pwd2")
        if pwd1 != pwd2:
            raise forms.ValidationError("密码不一致")
        else:
            return cleaned_data