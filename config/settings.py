from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DELTA_API_KEY: str = "CSfbcCxkUWtrrstU4LRqmZrIp1tHyg"
    DELTA_API_SECRET: str = "8MAGKlTR0UF73EYkhKtYWFKpNKKejRdHoSO0qBsvokHtBe93HUxxVUO8LveA"

    BASE_URL: str = "https://api.delta.exchange"

    DATABASE_URL: str = "sqlite:///btc_engine.db"

    MODE: str = "BACKTEST"

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()