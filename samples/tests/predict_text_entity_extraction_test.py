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

from samples import predict_tables_classification_sample

ENDPOINT_ID = "6207156555167563776" # text_entity_extraction endpoint
PROJECT_ID = "580378083368" # ucaip-sample-tests

INSTANCE = {"content": "I really love working at Google!"}

def test_ucaip_generated_predict_text_entity_extraction_sample(capsys):

    predict_tables_classification_sample.predict_tables_classification_sample(
        instance_dict=INSTANCE,
        project=PROJECT_ID,
        endpoint_id=ENDPOINT_ID
    )

    out, _ = capsys.readouterr()
    assert "confidences" in out