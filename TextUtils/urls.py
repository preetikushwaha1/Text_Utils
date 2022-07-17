
from django.urls import path
from TextUtils import views

urlpatterns = [

    path('removePunctuation/', views.remove_punctuation_fun, name="Remove_Punctuation"),
    path('capitalizefirst/', views.capitalize_first_fun, name="Capitalize_First"),
    path('newlineremover/', views.new_line_remover_fun, name="New_Line_Remover"),
    path('spaceremover/', views.space_remover_fun, name="Space_Remover"),
    path('charcount/', views.char_count_fun, name="Char_Count"),


]