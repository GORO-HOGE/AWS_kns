#1.テンプレートを出力（レンダー）するのには不要なので消し
#https://qiita.com/Bashi50/items/b9666030a058795c7dd8

#from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect  # 追加
from .forms import TestForm  # part4追加
from .models import Employee  # import追加(part5追加)
from .forms import EmployeeAdd  # part5追加



def index(request):
    #1.と同じ
    #return HttpResponse("Hello World!")

    my_dict = {
        'insert_something':"views.pyのinsert_something部分です。",
        'name':'KAIRIN',
        'test_titles': ['title 1', 'title 2', 'title 3'],  # 追加
        'form': TestForm(),  # part4追加
        'insert_forms': '初期値',  # part4追加
    }

    # ---- part4追加 ----
    if (request.method == 'POST'):
        my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '\n整数型:' + request.POST['num']
        my_dict['form'] = TestForm(request.POST)
    # ---- part4追加 ----

    return render(request, 'webtestapp/index.html', my_dict)


def info(request):
    #employees = Employee.objects.values_list('id','name','department')
    employees = Employee.objects.all()
    infodata = Employee.objects.all()
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    my_dict2 = {
        'title': 'テスト',
        'employees': employees,
        'header':header
    }
    return render(request, 'webtestapp/info.html',my_dict2)

#ユーザ新規作成
def create(request):
    message = ''  # 初期表示ではカラ
    if (request.method == 'POST'):
        form = EmployeeAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/info')
        else:
            message = '再入力して下さい'
    modelform_dict = {
        'title':'modelformテスト',
        'form': EmployeeAdd(),
        'message': message,  # エラーメッセージ
    }
    return render(request, 'webtestapp/create.html', modelform_dict)

#ユーザ情報更新
def update(request, num):
    message = ''
    employee_obj = Employee.objects.get(id=num)
    if (request.method == 'POST'):
        employee = EmployeeAdd(request.POST, instance=employee_obj)
        if employee.is_valid():
            employee.save()
            return redirect(to='/info')
        else:
            message = '再入力して下さい'
    update_dict = {
        'title': '登録情報更新画面',
        'id': num,
        'form': EmployeeAdd(instance=employee_obj),
        'message': message,
    }
    return render(request, 'webtestapp/update.html', update_dict)

#ユーザ情報削除
def delete(request, num):
    header = ['ID','名前','メール','性別','部署','社歴','作成日']
    message = ''
    employee_obj = Employee.objects.get(id=num)
    if (request.method == 'POST'):
        employee_obj.delete()
        return redirect(to='/info')
    delete_dict = {
        'title': '削除画面',
        'header': header,
        'id': num,
        'employee': employee_obj,
        'message': message,
    }
    return render(request, 'webtestapp/delete.html', delete_dict)