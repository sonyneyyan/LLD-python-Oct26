from rest_framework.response import Response
from rest_framework import status

def get_object(model_class, **kwargs):
    """
    Custom function to retrieve an object or return a 404 response.
    
    Parameters:
    -----------
    - model_class: 
        The Django model class to query (e.g., Book or Author).
    - **kwargs: 
        Arbitrary keyword arguments representing the query parameters 
        (e.g., id=book_id or name='John Doe').

    Returns:
    --------
    - If the object is found, it returns the instance of the model class.
    - If the object is not found, it returns a Response object with:
        {
            "<model_name_lower>": "Not found"
        }
      and a status code of 404 (Not Found).

    Raises:
    -------
    - No exceptions are propagated; instead, a 404 response is returned for 
      missing objects.
    
    Example Usage:
    --------------
    book = get_object(Book, id=1)  # Gets book with id=1, or returns 404.
    author = get_object(Author, name="J.K. Rowling")  # Same logic for Author.
    """
    try:
        obj = model_class.objects.get(**kwargs)
        return obj  # Return the object if found.
    except model_class.DoesNotExist:
        return Response(
            {model_class.__name__.lower(): "Not found"},
            status=status.HTTP_404_NOT_FOUND
        )
