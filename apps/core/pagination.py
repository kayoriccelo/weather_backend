from rest_framework.pagination import PageNumberPagination as DrfPageNumberPagination


class PageNumberPagination(DrfPageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000