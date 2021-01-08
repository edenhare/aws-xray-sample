from functions.poc_select_pair import app
import datetime
from aws_xray_sdk.core import xray_recorder

def test_select():

    # Start a segment
    segment = xray_recorder.begin_segment('test-select-pair')
    data = app.lambda_handler({}, "")
    # End a segnent
    xray_recorder.end_segment()

    assert "statusCode" in data

    assert data["statusCode"] == 200

