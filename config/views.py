# -*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

# from django.http import HttpResponse
from django.shortcuts import render
from burgers.models import Burger
import pandas as pd 

def main(request):
    # return HttpResponse("안녕하세요, pyburger입니다.") # 이 코드를 HTML로 처리
    return render(request, "main.html")

#p.48
def burger_list(request):
    # burgers = Burger.objects.all() # DB에서 정보를 가져옴
    burgers = Burger.objects.all().values()
    data = pd.DataFrame(burgers)
    print(data)
    # print("전체 햄버거 목록:", burgers)
    # Template
    context = {
        # "burgers" : burgers, 
        "burgers" : data.to_html(classes="table table-dark table-hover", 
        index=False, justify="match-parent")
    }

    return render(request, "burger_list.html", context)

def burger_search(request):
  # print(request.GET)
  keyword = request.GET.get("keyword")
  # print(keyword)
  
  # keyword 값이 주어진 경우
  if keyword is not None:
    # keyword 값으로 검색된 QuerySet을 할당
    burgers = Burger.objects.filter(name__contains=keyword)
  
  # 주소표시줄을 통해 keyword가 주어지지 않아, None이 할당된 경우
  else:
    # 검색 결과가 없는 것과 같은 빈 QuerySet을 할당
    burgers = Burger.objects.none()
  
  # burgers = Burger.objects.filter(name__contains=keyword) # DB에서 데이터를 가져오는 작업
  # print(burgers)
  
  # 결괏값을 HTML로 데이터 전달해주기
  context = {
    "burgers" : burgers,
  }
  
  return render(request, "burger_search.html", context = context)
