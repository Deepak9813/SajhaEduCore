from apps.common.pagination import CustomPagination

class PaginationMixin:
    """Reusable mixin that provides pagination functionality for API views."""
    pagination_class = CustomPagination

    def paginate_queryset(self, queryset, request):
        self.paginator = self.pagination_class()
        return self.paginator.paginate_queryset(queryset, request, view=self)
    

    def get_paginated_response(self, data):
        return self.paginator.get_paginated_response(data)
    




