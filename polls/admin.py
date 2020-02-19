from django.contrib import admin

# Register your models here.


from .models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question_text','pub_date')

    list_per_page = 50

    #直接修改
    list_editable = ['question_text']

    #点击关键字进入修改,元组
    #list_display_links = ('question_text',)

    #筛选器
    #过滤
    #list_filter = ('')
    #搜索字段
    search_fields = ('question_text',)
    #详细时间分层筛选
    date_hierarchy = 'pub_date'




class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id','question','choice_text','votes')

    list_per_page = 50

    list_editable = ['question','choice_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.site_header = '后台'
admin.site.site_title = '后台的标题'