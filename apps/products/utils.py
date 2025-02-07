from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank, SearchHeadline

from apps.products.models import Products

def query_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector('name', 'description')
    req_query = SearchQuery(query)
    
    result = (
        Products.objects.annotate(rank=SearchRank(vector, req_query))
        .filter(rank__gt=0)
        .order_by('-rank')
    )
    
    result = result.annotate(
        headline=SearchHeadline(
            'name',
            req_query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>'
        )
    )
    
    result = result.annotate(
        bodyline=SearchHeadline(
            'description',
            req_query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>'
        )
    )
    
    return result
    
    # keywords = [word for word in query.split() if len(word) > 2]
    
    # query_objects = Q()
    
    # for keyword in keywords:
    #     query_objects |= Q(name__icontains=keyword)
    #     query_objects |= Q(description__icontains=keyword)
        
    # return Products.objects.filter(query_objects)
