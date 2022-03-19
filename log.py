from config import logging

# defining location of the logfile
log_file = "./log_actions.log"

# Configure logging
logging.basicConfig(filename=log_file,
                    format="[%(asctime)s] %(message)s",
                    filemode="w",
                    level=logging.DEBUG)

logging.getLogger().addHandler(logging.StreamHandler())

# to handle error exceptions from matplotlib
logging.getLogger('matplotlib.font_manager').disabled = True


# stop logging
logging.shutdown()
