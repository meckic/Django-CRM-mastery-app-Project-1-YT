# to hadle exeptions
from django.middleware.common import MiddlewareMixin
from django.http import HttpResponse
#from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

response_content = f"""
<!DOCTYPE html> 
<html> 
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title> Error </title>
        <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/flatly/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="css/styles.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    </head>
    <body> 
        <div class="container">
            <br>
                <p id="message-timer" class="alert alert-success float-center text-center message-text"> 
                    <i class="fa fa-check" aria-hidden="true"></i> &nbsp; You are not authorized to execute that action!
                </p>
             <br>
                <p id="message-timer" class="alert alert-success float-center text-center message-text"> 
                    <i class="fa fa-check" aria-hidden="true"></i> &nbsp; Please navigate to the prev page!
                </p>
        </div>
    </body>
</html>
"""



class GlobalExceptionHandlerMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        # Customize error handling logic here
        #error_message = "You are not authorized to execute the command!"
        #return HttpResponse(f"An error occurred: {error_message} Please return to prev page.", status=500)
        return HttpResponse(response_content, content_type='text/html')
        
        
        