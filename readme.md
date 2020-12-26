# ReadMe for SAM X-Ray Sample

The files in this sample are:
```

├── api
├── aws_xray_sdk
│   └── python
│       ├── aws_xray_sdk
│       ├── aws_xray_sdk-2.6.0.dist-info
│       ├── bin
│       ├── botocore
│       ├── botocore-1.19.43.dist-info
│       ├── dateutil
│       ├── future
│       ├── future-0.18.2.dist-info
│       ├── importlib_metadata
│       ├── importlib_metadata-3.3.0.dist-info
│       ├── jmespath
│       ├── jmespath-0.10.0.dist-info
│       ├── jsonpickle
│       ├── jsonpickle-1.4.2.dist-info
│       ├── libfuturize
│       ├── libpasteurize
│       ├── past
│       ├── __pycache__
│       ├── python_dateutil-2.8.1.dist-info
│       ├── six-1.15.0.dist-info
│       ├── typing_extensions-3.7.4.3.dist-info
│       ├── urllib3
│       ├── urllib3-1.26.2.dist-info
│       ├── wrapt
│       ├── wrapt-1.12.1.dist-info
│       └── zipp-3.4.0.dist-info
├── functions
│   ├── poc-notify-pair
│   ├── poc-save-db
│   ├── poc-select-pair
│   └── poc-verify-pair
|── statemachine
├── no-xray-template.yaml
├── samconfig.toml
├── statemachine
├── template.yaml
└── xray-template.yaml

```

## Buiding the Sample

To build without X-Ray, execute:

```
sam build --template-file no-x-ray-template.yaml
sam deploy
```

to build with X-Ray, execute:

```
sam build --template-file xray-template.yaml
sam deploy
```

