import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.abspath(os.path.join(log_dir, "running_logs.log"))

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
#os.makedirs(log_dir, exist_ok=True)

#open(log_filepath, 'a').close()
try:
	logging.basicConfig(
		level=logging.INFO,
		format=logging_str,
		handlers=[
			logging.FileHandler(log_filepath),
			logging.StreamHandler(sys.stdout)
		]
	)
	logger = logging.getLogger("textSummarizerLogger")
	logger.info("Welcome to our custom logging")
except Exception as e:
	print(f"Error setting up logging: {e}")

print("Log file path:", log_filepath)