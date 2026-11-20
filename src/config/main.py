from typing import TypedDict


class BaseUrls(TypedDict):
    DSA_PLATFORM: str
    ALGO_VISUALIZER: str


BASE_URLS: BaseUrls = {
    "ALGO_VISUALIZER": "",
    "DSA_PLATFORM": "http://127.0.0.1:8000/v1",
}
