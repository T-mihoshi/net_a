from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def tag_list(request):
    return render(request, 'tag_list.html')
def setting(request):
    return render(request, 'setting.html')
def search(request):
    return render(request, 'search.html')
def privacy(request):
    return render(request, 'privacy.html')
def net_a_tutorial(request):
    return render(request, 'net_a_tutorial.html')
def my_page(request):
    return render(request, 'my_page.html')
def my_fish(request):
    return render(request, 'my_fish.html')
def index(request):
    return render(request, 'index.html')
def history(request):
    return render(request, 'history.html')
def genre_list(request):
    return render(request, 'genre_list.html')
def favorite_list(request):
    return render(request, 'favorite_list.html')
def fish_info(request):
    return render(request, 'fish_info.html')
def edit_fish(request):
    return render(request, 'edit_fish.html')
def base(request):
    return render(request, 'base.html')
def registration(request):
    return render(request, 'registration.html')
def base_root(request):
    return render(request, 'base_root.html')
def first(request):
    return render(request, 'first.html')


from net_a_db.forms import UserForm, LoginForm, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#新規登録
def register(request):
    error_message = ""
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            UserProfile.objects.create(user=user, icon_id=1)
            login(request, user)  # ユーザーをログインさせる
            return redirect('first')
        else:
            if 'password1' in user_form.errors:
                error_message = 'パスワードは6文字以上で入力してください。'
            elif 'username' in user_form.errors:
                error_message = '存在するユーザーです。'
            else:
                error_message = '入力を確認してください、入力が正しくありません。'
    else:
        user_form = UserForm()
    return render(request, 'registration.html', {'user_form': user_form, 'error_message': error_message})

#ログイン
def user_login(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        #ユーザーが存在するか、パスワードがあっているか
        if user:
                login(request, user)
                return redirect('index')
        else:
            error_message = '入力が間違っています'
            return render(request, 'login.html', context={'login_form': login_form, 'error_message': error_message})
    return render(request, 'login.html', context={'login_form': login_form})

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm

#ユーザー情報編集
from django.contrib import messages

@login_required
def setting_edit(request):
    error_message = None
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'プロフィールが更新されました。')
            return redirect('setting')
        else:
            error_message = '入力に間違いがあります'
    else:
        user_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'setting_edit.html', {'user_form': user_form, 'error_message': error_message})

"""@login_required
def setting_edit(request):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('setting')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'setting_edit.html', {'user_form': user_form})"""

#パスワード編集
@login_required
def setting_password(request):
    error_message = None
    if request.method == 'POST':
        password_form = PasswordChangeForm(data=request.POST, user=request.user)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # パスワード変更後にセッションを維持
            messages.success(request, 'パスワードが変更されました。')
            return redirect('setting')
        else:
            error_message = 'フォームにエラーがあります。'
    else:
        password_form = PasswordChangeForm(user=request.user)
    return render(request, 'setting_password.html', {'password_form': password_form, 'error_message': error_message})



from .forms import FishInfoForm
from .models import FishInfo, History

#投稿機能
def add_fish(request):
    error_message = ''  # エラーメッセージを初期化
    if request.method == 'POST':
        fish_info_form = FishInfoForm(request.POST, request.FILES)
        if fish_info_form.is_valid():
            if not request.POST.get('name') or not request.FILES.get('preview'):
                error_message = '写真は必須です。'
                return render(request, 'add_fish.html', {'fish_info_form': fish_info_form, 'error_message': error_message})
            else:
                fish_info = fish_info_form.save(commit=False)
                fish_info.user = request.user
                fish_info.category = fish_info_form.cleaned_data.get('category')
                fish_info_form.save()
                return redirect('my_fish')
        else:
            error_message = 'フォームにエラーがあります。'
    else:
        fish_info_form = FishInfoForm()
    return render(request, 'add_fish.html', {'fish_info_form': fish_info_form, 'error_message': error_message})

#投稿編集
@login_required
def edit_fish_info(request, fish_id):
    fish_info = get_object_or_404(FishInfo, id=fish_id, user=request.user)
    error_message = ''  # エラーメッセージ用の変数を初期化
    if request.method == "POST":
        fish_info_form = FishInfoForm(request.POST, request.FILES, instance=fish_info)
        if fish_info_form.is_valid():
            fish_info_form.save()
            return redirect('my_fish')  # 魚情報の詳細ページへリダイレクト
        else:
            error_message = 'フォームにエラーがあります。'  # フォームのバリデーションエラー時のメッセージ
    else:
        fish_info_form = FishInfoForm(instance=fish_info)
    return render(request, 'edit_fish_info.html', {
        'fish_info_form': fish_info_form,
        'fish_info': fish_info,
        'error_message': error_message  # エラーメッセージをテンプレートに渡す
    })



@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def info(request):
    return HttpResponse('ログインしています')

#indexの色々な情報を表示
def index(request):
    fish_infos = FishInfo.objects.order_by('-create_at')
    fish_infos_size = FishInfo.objects.filter(fish_size__gte=23).order_by('-create_at').all()
    fish_infos_favorites = FishInfo.objects.order_by('-good')
    return render(request, 'index.html', {
        'fish_infos': fish_infos,
        'fish_infos_size': fish_infos_size,
        'fish_infos_favorites': fish_infos_favorites,
        })

#下記、もっと見る[最新の投稿、大きい魚、人気の魚]
def fish_new_list(request):
    fish_new_list = FishInfo.objects.order_by('-create_at')
    return render(request, 'fish_new_list.html', {'fish_new_list': fish_new_list})

def fish_size_list(request):
    fish_size_list = FishInfo.objects.filter(fish_size__gte=23).order_by('-create_at').all()
    return render(request, 'fish_size_list.html', {'fish_size_list': fish_size_list})

def fish_favorite_list(request):
    fish_favorite_list = FishInfo.objects.order_by('-good')
    return render(request, 'fish_favorite_list.html', {'fish_favorite_list': fish_favorite_list})

#詳細情報、いいねカウント
from django.utils import timezone
def fish_info(request, fish_info_id):
    fish_info = get_object_or_404(FishInfo, pk=fish_info_id)
    favorites_count = Favorite.objects.filter(fish=fish_info).count()  # お気に入りの数をカウント
    if request.user.is_authenticated:
        history, created = History.objects.update_or_create(
            user=request.user,
            fish=fish_info,
            defaults={'update_at': timezone.now()}
        )
    return render(request, 'fish_info.html', {'fish_info': fish_info, 'good_count': favorites_count})

#閲覧履歴
def history(request):
    histories = History.objects.filter(user=request.user).order_by('-update_at')
    return render(request, 'history.html', {'histories': histories})

# ジャンルIDに対応するFishInfo レコードを取得
def genre(request, genre):
    fish_infos_genre = FishInfo.objects.filter(genre=genre)
    return render(request, 'genre_list.html', {'fish_infos_genre': fish_infos_genre})

#いいね機能
from .models import Favorite
def favorite_toggle(request, fish_info_id):
    user = request.user
    fish = get_object_or_404(FishInfo, pk=fish_info_id)
    favorite, created = Favorite.objects.get_or_create(user=user, fish=fish)

    if not created:
        favorite.delete()# すでにいいねが存在する場合は、いいねを削除
    return redirect('fish_info', fish_info_id=fish_info_id)  # 適切なビュー名に置き換えてください

#お気に入り画面表示
def favorite_list(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user).select_related('fish')
    fish_info_favorite = [favorite.fish for favorite in favorites]
    return render(request, 'favorite_list.html', {'fish_info_favorite': fish_info_favorite})

#自分の魚
def my_fish(request):
    my_fishs = FishInfo.objects.filter(user=request.user)
    return render(request, 'my_fish.html', {'my_fishs': my_fishs})
    

#検索機能
from django.db.models import Q
from django.urls import reverse
# フォームからのPOSTリクエストを処理するビュー
def search_fish_info(request):
    if request.method == 'POST':  # POSTリクエストを受け取った場合
        query = request.POST.get('q', '')  # フォームから検索クエリを取得
        return redirect(f"{reverse('search_results')}?q={query}")  # 検索クエリをURLパラメータに含めてリダイレクト
    return render(request, 'search_form.html')

# 検索結果を表示するビュー
def search_results(request):
    query = request.GET.get('q', '')  # GETリクエストから検索クエリを取得
    context = {'query': query}
    if query:  # 検索クエリに基づいてFishInfoオブジェクトを検索
        fish_info_search = FishInfo.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
        if not fish_info_search.exists():
            context['error'] = '該当する情報が見つかりません。'
        else:
            context['fish_info_search'] = fish_info_search
    return render(request, 'search.html', context)

#アイコン選択機能
from .models import UserProfile, Icon
from django.contrib.auth.decorators import login_required

@login_required
def icon_change(request):
    if request.method == 'POST':
        icon_id = request.POST.get('icon_id')
        new_icon = Icon.objects.get(id=icon_id)  # 修正した行
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.icon = new_icon
        user_profile.save()
        return redirect('setting')  # ユーザーの設定ページへリダイレクト
    else:
        icons = Icon.objects.all()
        return render(request, 'icon_change.html', {'icons': icons})

# #編集機能

# @login_required
# def edit_fish_info(request, fish_id):
#     fish_info = get_object_or_404(FishInfo, id=fish_id, user=request.user)
#     if request.method == "POST":
#         form = FishInfoForm(request.POST, request.FILES, instance=fish_info)
#         if form.is_valid():
#             form.save()
#             return redirect('my_fish')  # 魚情報の詳細ページへリダイレクト
#     else:
#         form = FishInfoForm(instance=fish_info)
#     return render(request, 'edit_fish_info.html', {'form': form, 'fish_info': fish_info})
    
"""
from .models import FishInfo
def fish_info(request):
    fish_infos = FishInfo.objects.filter(id=1).all()  # すべての FishInfo レコードを取得
    return render(request, 'fish_info.html', {'fish_infos': fish_infos})
"""
"""
オブジェクト化したい
for page in pages:
    def index(request):
        return render(request, str(page) + '.html')
        

"""

