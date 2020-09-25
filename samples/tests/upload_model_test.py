# Generated code sample for google.cloud.aiplatform.ModelServiceClient.upload_model
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
from uuid import uuid4
from google.cloud import aiplatform

from samples import upload_model_sample, delete_model_sample

PROJECT_ID = "ucaip-sample-tests"
IMAGE_URI = "gcr.io/cloud-ml-service-public/cloud-ml-online-prediction-model-server-cpu:v1_15py3cmle_op_images_20200229_0210_RC00"
ARTIFACT_URI = "gs://ucaip-samples-us-central1/model/explain/"
DISPLAY_NAME = f"temp_upload_model_test_{uuid4()}"

MODEL_ID = None

@pytest.fixture(scope="function", autouse=True)
def teardown(capsys):
    yield

    assert MODEL_ID is not None

    delete_model_sample.delete_model_sample(
        project=PROJECT_ID,
        model_id=MODEL_ID
    )

    out, _ = capsys.readouterr()
    assert "delete_model_response" in out


def test_ucaip_generated_upload_model_sample(capsys):
    global MODEL_ID
    assert MODEL_ID is None

    upload_model_sample.upload_model_sample(
        display_name=DISPLAY_NAME,
        metadata_schema_uri='',
        image_uri=IMAGE_URI,
        artifact_uri=ARTIFACT_URI,
        project=PROJECT_ID
    )

    out, _ = capsys.readouterr()
    MODEL_ID = out.split("model:")[1].split("\n")[0].split("/")[-1]
