from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 5
    # page_size_query_param = 'end'
    # page_query_param = 'p'
    max_page_size = 100
    
class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    # limit_query_param = 'limit'
    # offset_query_param = 'start'
    max_limit = 10

class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created' #-created means decending to assending and without - reverse order
    cursor_query_param = 'record'
    
    
    
    
    
    
# last page link: http://127.0.0.1:8000/watch/filter/?page=last    
# GET offset example: https://api.example.org/accounts/?limit=100&offset=400