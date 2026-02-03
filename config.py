from typing import Self
from pathlib import Path
from pydantic import HttpUrl, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    base_url: HttpUrl
    screenshot_dir: DirectoryPath

    @classmethod
    def create_settings(cls) -> Self:
        screenshot_dir = Path("screenshots/")
        screenshot_dir.mkdir(exist_ok=True)
        return Settings(screenshot_dir=screenshot_dir)
