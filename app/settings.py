from pydantic import AnyUrl, BaseSettings, PostgresDsn, validator
import os


class Settings(BaseSettings):
    ##################
    # HTML Settings  #
    ##################
    BASE_ENDPOINT: str = "/"
    CLASSIFICATION_ENDPOINT: str = "/process-classification"
    HTML_UPLOAD_FIELD_NAME: str = "sign-lang-photo"

    ##################
    # Classification #
    #     access     #
    ##################
    AZURE_CLASSIFICATION_ENDPOINT: str = ""
    AZURE_CLASSIFICATION_API_KEY: str = ""
    CLASSIFICATION_THRESHOLD: float = 0.5



    # Allow to use local .env file with secrets or other variables
    class Config:
        case_sensitive = True
        env_file = os.environ.get("SETTINGS_ENV", ".env")

settings = Settings()