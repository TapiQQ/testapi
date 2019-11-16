def handle(req):
    """
	This will be a health check function for all uMEC API endpoints

	Arg: req is a placeholder, doesn't do anything
	***TODO: how to call handler function in OpenFaas without arguments***

	Returns status of all uMEC APIs deployed in Junction challenge:
	
	uMEC MEC011 Application Enablement API: http://micromec.org:32000
	uMEC Sensors API: http://micromec.org:32001
	uMEC Detection API: http://micromec.org:32002
	uMEC Lights API: http://micromec.org:32003
	uMEC Camera API: http://micromec.org:32004
	
	Healthcheck: Considers endpoint alive if response status code is 2XX, else considers it dead.
	
	***UNTESTED in the Openfaas Platform, only in regular Python Interpreter***
	
	Ret: Generic success message
	
    """

    import requests

    try:
        response = requests.get("https://micromec.org:32000").status_code
        if response in range(200,226):
            print("uMEC MEC011 Application Enablement API is alive! Response:" + str(response))
        else:
            print("uMEC MEC011 Application Enablement API is dead! Response:" + str(response))
    except:
        print("Error in trying to access uMEC MEC011 Application Enablement API!")


    try:
        response = requests.get("https://micromec.org:32001").status_code
        if response in range(200,226):
            print("uMEC Sensors API is alive! Response:" + str(response))
        else:
            print("uMEC Sensors API is dead! Response:" + str(response))
    except:
        print("Error in trying to access uMEC Sensors API!")


    try:
        response = requests.get("https://micromec.org:32002").status_code
        if response in range(200,226):
            print("uMEC Detection API is alive! Response:" + str(response))
        else:
            print("uMEC Detection API is dead! Response:" + str(response))
    except:
        print("Error in trying to access uMEC Detection API!")


    try:
        response = requests.get("https://micromec.org:32003").status_code
        if response in range(200,226):
            print("uMEC Lights API is alive! Response:" + str(response))
        else:
            print("uMEC Lights API is dead! Response:" + str(response))
    except:
        print("Error in trying to access uMEC Lights API")

    try:
        response = requests.get("https://micromec.org:32004").status_code
        if response in range(200,226):
            print("uMEC Camera API is alive! Response:" + str(response))
        else:
            print("uMEC Camera API is dead! Response:" + str(response))
    except:
        print("Error in trying to access uMEC Camera API")


    return "Function finished successfully"

