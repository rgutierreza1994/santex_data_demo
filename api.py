import fastapi
from fastapi import FastAPI
from fastapi import Depends
import dotenv
from models import common_api_responses
from connectors.db_connector import get_session, Session
from fastapi import HTTPException

dotenv.load_dotenv()

main_api = FastAPI()


@main_api.get(
    "/get-incoming-age-gender",
    response_model=common_api_responses.ListIncomingAgeGender,
)
async def get_incoming_age_gender(
    db_session: Session = Depends(get_session),
):
    try:
        result = db_session.execute(
            "select * from santex.demo_datalake.incoming_age_gender_group"
        )
        data = [common_api_responses.IncomingAgeGender(**row) for row in result]
    except Exception as ex:
        ## TODO improve the exception handling to reconnect if we loose connection to DB
        raise HTTPException(
            status_code=404,
            detail="No table found with the name incoming_age_gender_group",
        )

    return common_api_responses.ListIncomingAgeGender(data=data)
