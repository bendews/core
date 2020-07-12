"""Constant for AWS component."""
DOMAIN = "aws"

ATTR_OBJECTS = "objects"
ATTR_LABELS = "labels"

DATA_CONFIG = "aws_config"
DATA_HASS_CONFIG = "aws_hass_config"
DATA_SESSIONS = "aws_sessions"

CONF_ACCESS_KEY_ID = "aws_access_key_id"
CONF_CONTEXT = "context"
CONF_CREDENTIAL_NAME = "credential_name"
CONF_CREDENTIALS = "credentials"
CONF_NOTIFY = "notify"
CONF_IMAGE_PROCESSING = "image_processing"
CONF_PROFILE_NAME = "profile_name"
CONF_REGION = "region_name"
CONF_SECRET_ACCESS_KEY = "aws_secret_access_key"
CONF_SERVICE = "service"
CONF_VALIDATE = "validate"

CONF_COLLECTION_ID = "collection_id"
CONF_IDENTIFY_FACES = "identify_faces"
CONF_DETECTION_ATTRIBUTES = "detection_attributes"
CONF_SAVE_FILE_FOLDER = "save_file_folder"
CONF_SAVE_FILE_TIMESTAMP = "save_file_timestamp"

EVENT_OBJECT_DETECTED = "image_processing.detect_object"
EVENT_LABEL_DETECTED = "image_processing.detect_label"
