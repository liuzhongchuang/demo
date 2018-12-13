from django.db import models
# Create your models here.

"""
定义一个作者类
"""
class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)


"""
创建一个博客文章类
"""
class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    counter = models.IntegerField(default=0)
    pubDate = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

#自己创建新的管理器
class DepartmentManager():
    # 自定义个新增部门的方法
    def creat_dept(self, name, create_date):
        dept = Department()
        dept.name = name
        dept.create_date = create_date
        dept.save()

    # 自定义一个根据id查询部门的方法
    def getDeptById(self, name):
        return Department.objects.all().filter(name__contains=name)

#部门类
class Department(models.Model):
    name = models.CharField(max_length=20)
    create_date = models.DateField(auto_now_add=True)
    # 配置自定义的模型管理器（在外部可以用过该属性operate_Dept进一步来调用creat_dept()和getDeptById()）
    operate_Dept = DepartmentManager()

'''
 枚举 choices，数据库里面存放0和1，但是到前端的时候显示成对应的男和女。0_男， 1_女
 取值使用get_Foo_display()取男或女，Foo表示字段名称。比如下面获取sex即为get_sex_display()
'''
class Person(models.Model):
    sex_choice = (
        ('0','男'),
        ('1','女')
    )
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=sex_choice)
