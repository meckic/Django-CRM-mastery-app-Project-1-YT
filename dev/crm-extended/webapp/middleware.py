# to hadle exeptions
from django.middleware.common import MiddlewareMixin
from django.http import HttpResponse
#from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

#def my_view(request):
response_content = f"<!DOCTYPE html> <html> <head> <title>No permission!</title> </head> <body> <h1>You do not have permissions!</h1><p>Please go back to the prev page.</p></body></html>"

class GlobalExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        # Customize error handling logic here
        #error_message = messages.success(request, "Account created successfully!")
        error_message = "You are not authorized to execute the command!"
        #return HttpResponse(f"An error occurred: {error_message} Please return to prev page.", status=500)
        return HttpResponse(response_content, content_type='text/html')
        
        
        