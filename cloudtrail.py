import boto3

def Start_Logging(name): # The 'name' is referring to the Cloudtrail name
    cloudtrail_client = boto3.client('cloudtrail')
    response = cloudtrail_client.start_logging(
        Name=name
    )
    print(response)
    return True

def Get_Cloudtrail_Status(name):
    cloudtrail_client = boto3.client('cloudtrail')
    try:
        response = cloudtrail_client.get_trail_status(
            Name=name
        )
    except cloudtrail_client.exceptions.TrailNotFoundException:
        raise NameError("That Cloudtrail Trail was not found")
    return response.get('IsLogging')

def Stop_Logging(name):
    cloudtrail_client = boto3.client('cloudtrail')
    response = cloudtrail_client.stop_logging(
        Name=name
    )
    print(response)
    return True

# This is the main function that triggers the test
if __name__ == "__main__":
    Name = 'october-log-events'
    # Stop_Logging(Name)
    if not Get_Cloudtrail_Status(Name):
        Start_Logging(Name)
    else:
        print("Logging already enabled")