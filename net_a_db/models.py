from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

#使っていない
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    icon = models.ForeignKey(
        'icon', default=1, on_delete=models.SET_DEFAULT)
    website = models.URLField(null=True, blank=True)
    picture = models.FileField(upload_to='user/', null=True, blank=True)

    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    icon = models.ForeignKey('Icon', default=1, on_delete=models.SET_DEFAULT)
    # アイコンへの参照を追加
    """icon = models.ForeignKey('icon', default=1, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username"""

#テーブル定義
#使ってない
class UserInfo(models.Model):
    icon = models.ForeignKey(
        'icon', default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=254, db_index=True)
    password = models.CharField(max_length=128)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)



class FishInfo(models.Model):
    GENDER_CHOICES = [
        ('1', '不明'),
        ('2', 'オス'),
        ('3', 'メス'),
    ]

    CATEGORY_CHOICES = [
        ('1', ''),
        ('2', 'アロワナ'),
        ('3', 'ポリプテルス'),
        ('4', 'プレコ'),
        ('5', 'パクー（メチニスなど）'),
        ('6', 'カラシン(テトラなど)'),
        ('7', 'プラティ・卵生メダカなど'),
        ('8', 'ローチ'),
        ('9', 'エンゼルフィッシュ'),
        ('10', 'ディスカス'),
        ('11', 'シクリッド'),
        ('12', 'コリドラス'),
        ('13', '淡水エイ'),
        ('14', 'ベタ'),
        ('15', 'ナマズ'),
        ('16', 'フグ'),
        ('17', '川のエビ、貝、カニ'),
        ('18', '汽水魚'),
        ('19', 'その他熱帯魚'),
        ('20', 'メダカ'),
        ('21', '金魚'),
        ('22', '鯉'),
        ('23', '川魚'),
        ('24', 'その他淡水魚'),
        ('25', 'スズメダイ'),
        ('26', 'ヤッコ'),
        ('27', 'チョウチョウウオ'),
        ('28', 'ハギ'),
        ('29', 'ギンポ'),
        ('30', 'ベラ'),
        ('31', 'ハゼ'),
        ('32', 'ハタ'),
        ('33', 'フグ'),
        ('34', 'エイ、サメ'),
        ('35', 'タコ、イカ'),
        ('36', 'クラゲ、ナマコ、ヒトデなど'),
        ('37', '海のエビ、貝、カニ'),
        ('38', '一般に食用魚等の魚種'),
        ('39', 'その他海水魚'),
    ]

    TEMP_CHOICES = [
        ('1', '26'),
        ('2', '10'),
        ('3', '14'),
        ('4', '17'),
        ('5', '20'),
        ('6', '22'),
        ('7', '24'),
        ('8', '25'),
        ('9', '27'),
        ('10', '28'),
        ('11', '29'),
        ('12', '30'),
        ('13', '31'),
        ('14', '33'),
    ]
    
    AQUARIUM_SIZE_CHOICES = [
        ('1', '60'),
        ('2', '20'),
        ('3', '30'),
        ('4', '45'),
        ('5', '70'),
        ('6', '90'),
        ('7', '100'),
        ('8', '120'),
        ('9', '150'),
        ('10', '180'),
        ('11', '200'),
        ('12', '240'),
        ('13', '300'),
        ('14', '400'),
        ('15', '500'),
    ]
        
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    #previewのカラムを追加
    preview = models.ImageField(upload_to='upload_img/')
    movie = models.FileField(upload_to='upload_video/', null=True, blank=True)
    info = models.TextField(max_length=1000, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDER_CHOICES)
    #categoryのカラムを追加
    category = models.CharField(max_length=20, null=True, blank=True, choices=CATEGORY_CHOICES)
    fish_mixed = models.TextField(max_length=200, null=True, blank=True)
    temp = models.CharField(max_length=20, null=True, blank=True, choices=TEMP_CHOICES)
    fish_size = models.CharField(max_length=20, null=True, blank=True)
    aquarium_size = models.CharField(max_length=20, null=True, blank=True, choices=AQUARIUM_SIZE_CHOICES)
    material = models.TextField(max_length=200, null=True, blank=True)
    food = models.TextField(max_length=200, null=True, blank=True)
    #goodのカラムを追加
    good = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    fish = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)
    #Metaクラスを追加
    class Meta:
        unique_together = ('user', 'fish') 


class History(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    fish = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class Icon(models.Model):
    icon_file_name = models.ImageField(upload_to='icon_img/')
    icon_name = models.CharField(max_length=50)
    icon_text = models.CharField(max_length=200, null=True, blank=True)#iconに新しくテキストを追加
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class FishPhoto(models.Model):
    fish_info = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE, default=1)
    fish_file_name = models.ImageField(upload_to='upload_img/')
    display_number = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

#下記テーブルの追加、ユーザー情報にIcon情報を入れられないため
class Icon_items(models.Model):
    icon = models.ForeignKey(
        'icon', on_delete=models.CASCADE)
    fish_info = models.ForeignKey(
        'fishinfo', on_delete=models.CASCADE)
    icon_set = models.IntegerField(default=0, null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)
"""
アップデートに伴う、アイコンの所持情報テーブル
from django.conf import settings

class UserIcon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    obtained_at = models.DateTimeField(auto_now_add=True)  # アイコンを取得した日時
    is_active = models.BooleanField(default=False)  # このアイコンが現在選択されているか

    class Meta:
        unique_together = ('user', 'icon')  # 同じアイコンを複数持たないようにする
"""

"""
ER図通りのIconの設定


class Icon(models.Model):
    icon_file_name = models.ImageField(upload_to='icon_img/')
    icon_name = models.CharField(max_length=50)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

"""
"""
Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Sales(models.Model):
    fee = models.IntegerField()
"""