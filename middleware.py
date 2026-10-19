class NgrokSkipWarningMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Aggiunge header per saltare l'avviso ngrok
        if 'ngrok' in request.get_host():
            response['ngrok-skip-browser-warning'] = 'true'
        return response
