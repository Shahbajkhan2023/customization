from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p'


    def get_page_size(self, request):
         # Get the page size from the query parameter
        page_size = request.query_params.get(self.page_size_query_param, self.page_size)
        try:
            page_size = int(page_size)
        except ValueError:
            page_size = self.page_size

        # Limit the page size to the maximum allowed size
        return min(page_size, self.max_page_size)