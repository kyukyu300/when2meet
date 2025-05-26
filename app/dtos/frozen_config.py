from pydantic import ConfigDict

# frozen -> 생성 이후에는 변경할 수 없게 함.
FROZEN_CONFIG = ConfigDict(frozen=True)
