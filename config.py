from sample_config import Config


class Development(Config):
  #get this values from the my.telegram.org
  APP_ID = 1822414
  API_HASH = "46f1888d3f68396bad08c92ac4d7f00a"
  # the name to display in your alive message
  ALIVE_NAME = "AmarnathCdj"
  # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
  DB_URI = "postgres://svmvvnbpvnhlnm:13882276b3337b50b30be2d000bad9cb467b294f5714b867bfa4b201f994541c@ec2-54-217-224-85.eu-west-1.compute.amazonaws.com:5432/d6rjhg7d6nqj8e"
  #After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
  STRING_SESSION = "1BVtsOIgBuxbp6HU1bRBeYEdSmNVKcuTjR8C5chKx2BqzyaIRTImT0Qj6YM-p-st0m_wTVORWMvRm1mT8CUcqRLhD52wfGhW203eoqsMrnDPMunoY7dkMjfFa80u-SFw8bMV8BA-rYHOyv1NhrPJijqkXGIqX3NSUUtYIE3lbM52r3Cavc17XR-k6OkTayCx8N2WaWjS_egO8XKJOr-jVkf_piwabAf2zLNXLea3IPZ5HF7IWy-YtJ1tIjdnh98biiMldh7wLTfwFyI-Ui0Rqfqz6nrFJazftue5QY-yHsNj9L9T2UhqsEHKlaV2Ox-NiLDvBmnBRUrnEKi3L_0EXfehIQypxvuw="
  #create a new bot in @botfather and fill the following vales with bottoken and username respectively
  TG_BOT_TOKEN_BF_HER = "1478864022:AAEVF8-KFJ4auxrPhfJWmjVfWy_OBvjC-R8"
  TG_BOT_USER_NAME_BF_HER = "Anieroyebot"
  #create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
  PRIVATE_GROUP_BOT_API_ID = -1001433850650
  #command handler 
  COMMAND_HAND_LER = "."
  #sudo enter the id of sudo users userid's in that array
  SUDO_USERS = []
  # command hanler for sudo
  SUDO_COMMAND_HAND_LER = "."
