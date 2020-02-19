

default_app_config = 'polls.apps.PollsConfig'



# 我们可以在通过设置verbose_name字段，来指定app在后台显示的名称。你可能会发现，仅仅增加verbose_name之后，仍然没有效果。别慌，还需要一个小的设置就ok了！
# 在导入app时，django会检查每个在INSTALLED_APPS中的app的default_app_config变量，如果没有设置，django会使用基类AppConfig，因此我们只需要在init.py中指定default_app_config即可
