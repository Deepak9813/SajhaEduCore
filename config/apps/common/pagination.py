from rest_framework.pagination import PageNumberPagination

from math import ceil

class CustomPagination(PageNumberPagination):
    """Custom pagination class with additional pagination metadata."""
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "page"
    max_page_size = 100
   

    def get_paginated_response(self, data): 
        total_page = ceil(self.page.paginator.count/self.page_size)
       
        return {
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "page_size": self.get_page_size(self.request),
            "results": data,
            "total_page":total_page
        }