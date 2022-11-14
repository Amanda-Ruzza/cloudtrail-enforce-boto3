# AWS Cloudtrail Enforcement Boto3 Script

This Python script automates Cloudtrail enforcement as an AWS Security implementation. If ran on its own through the CLI, it needs a hard-coded 'Cloudtrail Trail Name.'
The **Cloudformation** YML template fixes this deficiency by creating a **Lambda Function** with a ``start logging`` command that is triggered by an **EventBridge Rule** anytime a Cloudtrail ``StopLogging`` API call is made on the Trail. 
The Cloudformation templates automatically reads the current Cloudtrail Trail's ARN, creates IAM permissions and a Lambda execution role, making this a fully automated solution 

## Known Issues

## Future Improvements
Implement this Boto3 Script into a Terraform Modular Deployment, as an alternative for Cloudformation 