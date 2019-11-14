def handle(req):
    """
	This will be a health check function for all uMEC API endpoints

	Arg: req is a placeholder, doesn't do anything

	returns status code of one API endpoint (detection)

    """

    import requests

    response = requests.get("http://192.168.20.106:32001/v1/models/")

    return response.status_code

