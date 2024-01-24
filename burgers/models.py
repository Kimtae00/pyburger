from django.db import models

# Create your models here.

# 모델 클래스 정의
class Burger(models.Model):
  # 문자열 타입의 버거 이름 정의
  name = models.CharField(max_length=20)
  # 정수 타입의 가격, 칼로리 정의
  price = models.IntegerField(default=0)
  calories = models.IntegerField(default=0)
  
  def __str__(self):
    return self.name
  
  
