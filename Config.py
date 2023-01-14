import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "27447602"))
    API_HASH = os.environ.get("API_HASH", "45cf07cc2561b3df04404af2ab284cbe")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5589942517:AAFhR1PsoraWAhTybxXuk0eXG5nsvSfXkbg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQBMDYqXz29bMIOQvxjPf9oaMOdTKNiI1KLVSk1qIf5sAn54JD9jO-8DHSB1_OPl7HGs81fIIf2ktBTlonv9K1g50s3Vro8SkN8kOpNIKP8wmNhl2cp179S8CP2PsbnvjQacbWnUjh5qqpPLCqhADZ4cBZ-yQvRH98y1WRwN18QkKAS6AxyRV_t6A99TcTpg3xvxMrCvPA9Mj9yRUL_1MCDXtbavuF9N4EbbSkRb8FJN9ldvPTwfSsA257-6cIyBekxr4m2Q2_ZvGuYexmPNmbh646qRoTya200p0pzv1SxsMyyxopx4ETlFp-7U4dtH3MdJK0W0477_lPZkLLG5yyMbQq7QWAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ApibotAk")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"
