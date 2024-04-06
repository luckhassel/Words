# Words

Available on: https://python-words-api.azurewebsites.net/

Description:
Words is a Python API that has the functionalities do count vowel number on word array, and also sort words by the direction desired.
It's available under a Azure Web App service

Features:

    Vowel count: Count how many vowels are on each word.
      Enpoint: [POST] /vowel_count
      Input Example: {"words": ["batman", "robin", "coringa"]}
      Output Example: {"batman": 2, "robin": 2, "coringa": 3}

    Sort: Sort an array of words on the desired direction
      Enpoint: [POST] /sort
      Input Example: {"words": ["batman", "robin", "coringa"], "order": "asc"} | {"words": ["batman", "robin", "coringa"], "order": "desc"}
      Output Example: ["batman", "coringa", "robin"] | ["robin", "coringa", "batman"]
      
    Docker support: There's a docker file in case you want to run it using docker container. 
      Steps:
        1) docker build -t <IMAGE_NAME> .
        2) docker run -it -p 5000:5000 <IMAGE_NAME>

    Unit tests: The project has 30 unit tests, including words controller tests, words sort use case test and vowel count use case tests.
    Below, there are the steps to execute this tests:
      1) python -m unittest discover -s tests/unit_tests/ -p '*_test.py'

    CI/CD: There's a CI/CD pipeline configured to use GitHub Actions. This pipeline performs lint analysis and runs all tests for pushes and pull
    request on main and development branches. Also, when a new version is pushed to main branch, it deploys it to Azure Web App.

    Azure Web App: The application is running on an azure Web App instance. Here're the steps followed:
      1) Create service plan: az appservice plan create \
                       --resource-group MY_RESOURCE_GROUP \
                       --name MY_APP_SERVICE_PLAN \
                       --is-linux
      2) Create web app: az webapp create \
                          --name MY_WEBAPP_NAME \
                          --plan MY_APP_SERVICE_PLAN \
                          --resource-group MY_RESOURCE_GROUP \
                          --runtime "python|3.10"
      3) The last step is added on the deploy section of CI/CD yaml file.
