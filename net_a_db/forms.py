from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import FishInfo, Icon, UserProfile
#from net_a_db.models import Profile, Icon

#新規登録
class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")    

#新規登録アイコン用
class ProfileForm(forms.ModelForm):
    icon = forms.ModelChoiceField(queryset=Icon.objects.all(), label='アイコン', required=False)

    class Meta:
        model = UserProfile
        fields = ('icon',)

class LoginForm(forms.Form):
    username = forms.CharField(label='名前', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'setting_input'}),
            'email': forms.EmailInput(attrs={'class': 'setting_input'}),
        }

from django import forms
from django.conf import settings

class FishInfoForm(forms.ModelForm):
    GENDER_CHOICES = [
        (1, '不明'),
        (2, 'オス'),
        (3, 'メス'),
    ]

    CATEGORY_CHOICES = [
        (1, ''),
        (2, 'アロワナ'),
        (3, 'ポリプテルス'),
        (4, 'プレコ'),
        (5, 'パクー（メチニスなど）'),
        (6, 'カラシン(テトラなど)'),
        (7, 'プラティ・卵生メダカなど'),
        (8, 'ローチ'),
        (9, 'エンゼルフィッシュ'),
        (10, 'ディスカス'),
        (11, 'シクリッド'),
        (12, 'コリドラス'),
        (13, '淡水エイ'),
        (14, 'ベタ'),
        (15, 'ナマズ'),
        (16, 'フグ'),
        (17, '川のエビ、貝、カニ'),
        (18, '汽水魚'),
        (19, 'その他熱帯魚'),
        (20, 'メダカ'),
        (21, '金魚'),
        (22, '鯉'),
        (23, '川魚'),
        (24, 'その他淡水魚'),
        (25, 'スズメダイ'),
        (26, 'ヤッコ'),
        (27, 'チョウチョウウオ'),
        (28, 'ハギ'),
        (29, 'ギンポ'),
        (30, 'ベラ'),
        (31, 'ハゼ'),
        (32, 'ハタ'),
        (33, 'フグ'),
        (34, 'エイ、サメ'),
        (35, 'タコ、イカ'),
        (36, 'クラゲ、ナマコ、ヒトデなど'),
        (37, '海のエビ、貝、カニ'),
        (38, '一般に食用魚等の魚種'),
        (39, 'その他海水魚'),
    ]

    TEMP_CHOICES = [
        (1, '26'),
        (2, '10'),
        (3, '14'),
        (4, '17'),
        (5, '20'),
        (6, '22'),
        (7, '24'),
        (8, '25'),
        (9, '27'),
        (10, '28'),
        (11, '29'),
        (12, '30'),
        (13, '31'),
        (14, '33'),
    ]
    
    AQUARIUM_SIZE_CHOICES = [
        (1, '60'),
        (2, '20'),
        (3, '30'),
        (4, '45'),
        (5, '70'),
        (6, '90'),
        (7, '100'),
        (8, '120'),
        (9, '150'),
        (10, '180'),
        (10, '200'),
        (11, '240'),
        (12, '300'),
        (13, '400'),
        (14, '500'),
    ]

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '魚の名前', 'class': 'input-style'}), label="名前")
    preview = forms.ImageField(label="プレビュー画像", required=False)
    movie = forms.FileField(label="動画", required=False)
    info = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '飼育情報', 'class': 'textarea-style'}), label="飼育情報", required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="性別", required=False, widget=forms.Select())
    category = forms.ChoiceField(choices=CATEGORY_CHOICES,label="＃タグ", required=False, widget=forms.Select())
    fish_mixed = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '混泳できた魚', 'class': 'textarea-style'}), label="混泳情報", required=False)
    temp = forms.ChoiceField(choices=TEMP_CHOICES, label="適正温度", required=False)
    fish_size = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'int-style'}), label="魚のサイズ", required=False, min_value=1)
    aquarium_size = forms.ChoiceField(choices=AQUARIUM_SIZE_CHOICES, label="水槽サイズ", required=False)
    material = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'レイアウト、使用器具', 'class': 'textarea-style'}), label="レイアウト情報", required=False)
    food = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '餌', 'class': 'textarea-style'}), label="餌", required=False)

    class Meta:
        model = FishInfo
        fields = ['name', 'preview', 'movie', 'info', 'gender', 'category', 
                'fish_mixed', 'temp', 'fish_size', 'aquarium_size', 'material', 'food']
        # categoryフィールドの値を取得し、対応する表示値を返します。
        def clean_category(self):
        # categoryフィールドの値を取得し、対応する表示値を返します。
            category = self.cleaned_data.get('category')
            for key, label in self.fields['category'].choices:
                if key == category:
                    return label
            return category