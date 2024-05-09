from django.db import models


# Create your models here.
from django.contrib.auth.models import User



class Profile(models.Model):
    # 新建立的Profile model跟User之間是一對一的關係，下面這行就是在兩者之間建立關係
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_img.jpg", upload_to="profile_pic")
    # 這個image欄位是用來儲存使用者上傳的圖片檔案的路徑
    # upload_to參數是用來指定圖片檔案的儲存路徑
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
    # 可以用user.username的值顯示