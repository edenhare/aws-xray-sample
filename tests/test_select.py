from functions.poc_select_pair import app
import datetime

def test_select():

    data = app.lambda_handler(event, "")

    assert "statusCode" in data

    assert data["statusCode"] == 200

