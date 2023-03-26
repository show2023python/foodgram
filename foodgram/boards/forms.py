from django import forms
from .models import Products


class StoreInputForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['picture','store_name', 'kinds',
                  'zip_code', 'place_prefecture',
                  'place_another','comments',
                  'main_comments']
        labels = {
            'picture': '写真',
            'store_name': '店名',
            'kinds': 'ジャンル',
            'zip_code': '郵便番号',
            'place_prefecture': '住所（○○県○○市）',
            'place_another': '住所（その他）',
            'comments': '一覧表示コメント',
            'main_comments': '詳細時表示コメント',
        }


class ProductUpdateForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Products
        fields = ['id','picture','store_name', 'kinds',
                  'zip_code', 'place_prefecture',
                  'place_another','comments',
                  'main_comments']
        labels = {
            'picture': '写真',
            'store_name': '店名',
            'kinds': 'ジャンル',
            'zip_code': '郵便番号',
            'place_prefecture': '住所（○○県○○市）',
            'place_another': '住所（その他）',
            'comments': '一覧表示コメント',
            'main_comments': '詳細時表示コメント',
        }



