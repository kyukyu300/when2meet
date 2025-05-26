from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원래는 어떤 DB를 쓰는지 URL에 적으면 안됨


@mysql_router.post("", description="meeting을 생성합니다.")
async def api_creating_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")
