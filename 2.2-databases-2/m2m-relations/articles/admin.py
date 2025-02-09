from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_of_true = []
        for form in self.forms:
            list_of_true.append(form.cleaned_data.get('is_main', None))
        if list_of_true.count(True) > 1:
            raise ValidationError('Главным может быть только один тег')
        if list_of_true.count(True) < 1:
            raise ValidationError('Вывберите один тег главным')        
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
    list_display = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']