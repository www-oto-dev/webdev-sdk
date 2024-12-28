# WebDev SDK (Python)

WebDev SDK is a tool that generates websites using AI. It is designed so that you can create a webpage automatically with the ability to control the result if it is required.

SDK is using the [web.oto.dev](https://web.oto.dev/) service. Please note that the service has a free plan by default, which will be subject to a number of restrictions in the future. You may want to consider a paid subscription version to remove restrictions and get more advanced features.


1. First, you need to **register on the [hub.oto.dev](https://hub.oto.dev/) service and copy an `API Key`** from the Dashboard
2. **Create a project and copy project ID** which is necessary for using the SDK
3. **Install SDK by using pip `pip install web_oto_dev_sdk`**
4. We recommend to use [jupyter notebooks](https://jupyter.org/) to call SDK functions instead of a regular .py file (but it will also work with Python projects)


## Creating a website by using the SDK

### Settings and SDK initialization

Replace `YOU_PROJECT_ID` with project ID from the 'edit' project screen and `YOUR_API_KEY` from the dashboard.

```
project_id = 'YOU_PROJECT_ID'
api_key = 'YOUR_API_KEY'
```

SDK initialization
```
from web_oto_dev_sdk import WebOtoDevSdk
from web_oto_dev_sdk.models.property import Property
from web_oto_dev_sdk.models.meaning import Meaning
from web_oto_dev_sdk.models.formula import Formula
from web_oto_dev_sdk.models.value import Value

oto = WebOtoDevSdk(
    project_id=project_id,
    api_key=api_key,
    base_url='https://web.oto.dev/openapi/api/v1',
    timeout=10*60*1000
)
```

If you are using Jupyter Notebooks, we recommend installing 'tabulate' and using it to display some SDK function results as tables.
```
from tabulate import tabulate

def table(data):
    return tabulate(data, tablefmt='html', showindex=False, stralign="right")
```


### Properties
```
oto.properties.set('supported-language', 'ru')
oto.properties.set('reference-website-url', 'https://your-old-website-to-collect-meanings.com')
oto.properties.set('branding-color', '#40C3E4')
oto.properties.set('light-color-threshold', '0.65')
oto.properties.set('website-skin', 'softcorners')
oto.properties.set('background-decoration', 'circle')
oto.properties.set('branding-gradient', 'linear-gradient(90deg, #00DBDE 0%, #FC00FF 100%);')
oto.properties.add('branding-gradient', '')
oto.properties.update([Property(key='supported-language', value='en')])
table(oto.properties.display())
```



