from django.urls import path

# 1 method
# from applications.author.views import BookView

# 3 method
from applications.author.views import BookListView

urlpatterns = [
    # 1 method
    # path('books-list/', book_list),

    # 2 method
    # path('books-list/', BookView.as_view())

    # 3 method
    path('books-list/', BookListView.as_view())
]