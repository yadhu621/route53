import os
import sys
import logging
import pathlib
from route53 import Route53

def main():
    """
    main() function
    """
    # Create log directory if not present
    pathlib.Path('../log/').mkdir(parents=True, exist_ok=True)

    # Setup logger
    log_format = '%(asctime)s %(levelname)s %(module)s : %(message)s'
    stdout_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler("../log/application.log")
    handlers = [stdout_handler, file_handler]

    logging.basicConfig(level=logging.INFO, format=log_format, handlers=handlers)
    logger = logging.getLogger(__name__)

    # Get Environment variables
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    hosted_zone_id = os.environ.get("HOSTED_ZONE_ID")

    if aws_access_key_id is None:
        logger.info("AWS_ACCESS_KEY_ID environment variable is not set. Exiting...")
        exit()

    if aws_secret_access_key is None:
        logger.info("AWS_SECRET_ACCESS_KEY environment variable is not set. Exiting...")
        exit()

    if hosted_zone_id is None:
        logger.info("HOSTED_ZONE_ID environment variable is not set. Exiting...")
        exit()

    Route53().add_cname("app.italia.it","vip-prod.cloud.com")    

if __name__ == "__main__":
    main()
