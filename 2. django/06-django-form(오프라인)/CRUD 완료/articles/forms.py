from django import forms
from .models import Article

# form 태그 vs django ModelForm 
# 후자가 유효성 검사 용이 
class ArticleForm(forms.ModelForm):

    # Meta : 폼 구조 자동생성 
    # 단점: css 적용불가, 위젯 사용 
    class Meta:
        # model = Article() : Article is not callable
        model = Article
        fields = '__all__'
        # fields = ('title', 'content', )

