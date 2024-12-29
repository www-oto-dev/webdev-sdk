# WebDev SDK (Python)

WebDev SDK is a tool that generates websites using AI. It is designed so that you can create a webpage automatically with the ability to control the result if it is required.

SDK is using the [web.oto.dev](https://web.oto.dev/) service. Please note that the service has a free plan by default, which will be subject to a number of restrictions in the future. You may want to consider a paid subscription version to remove restrictions and get more advanced features.


1. First, you need to **register on the [hub.oto.dev](https://hub.oto.dev/) service and copy an `API Key`** from the Dashboard
2. **Create a project and copy project ID** which is necessary for using the SDK
3. **Install SDK by using pip `pip install web_oto_dev_sdk`**
4. We recommend to use [jupyter notebooks](https://jupyter.org/) to call SDK functions instead of a regular .py file (but it will also work with Python projects)


## Quick Start

Replace `<YOU_PROJECT_ID>` with project ID from the [create a website](https://hub.oto.dev/app/websites/create/) (or edit) screen and `<YOUR_API_KEY>` from the [dashboard](https://hub.oto.dev/app/dashboard/)

```
# Configuring SDK
from web_oto_dev_sdk import WebOtoDevSdk
oto = WebOtoDevSdk(
    project_id=<YOU_PROJECT_ID>,
    api_key=<YOUR_API_KEY>,
    base_url='https://web.oto.dev/openapi/api/v1',
    timeout=10*60*1000
)

# Your project basic settings
oto.properties.set('supported-language', 'en')

# Information required to build your website
oto.meanings.set('mm-products-and-services', 'We provide an SDK for Python to simplify building websites by using AI')
oto.meanings.set('mm-free-first-step', 'You can quickly build a website by following the Quick Start guide located on https://github.com/www-oto-dev/webdev-sdk/')
oto.meanings.set('mm-product-usage-advantages', 'You can build websites in minutes')
oto.meanings.set('mm-product-usage-advantages', 'Use your social media, websites and blogs as a source of information')
oto.meanings.set('mm-product-usage-advantages', 'Websites have build-it speed and SEO optimization (Comming Soon)')
oto.meanings.set('mm-product-usage-advantages', 'Calling one function will keep your website up-to-date')
# ...

# Generating content & Building layout
oto.project.generate()
oto.project.build()

# Done
print(oto.project.view())
# Output: https://we.oto.dev/-/<YOU_PROJECT_ID>



## Full Сapabilities

### Full SDK imports

Replace `<YOU_PROJECT_ID>` and `<YOUR_API_KEY>` as described above.
```
from web_oto_dev_sdk import WebOtoDevSdk
from web_oto_dev_sdk.models.property import Property
from web_oto_dev_sdk.models.meaning import Meaning
from web_oto_dev_sdk.models.formula import Formula
from web_oto_dev_sdk.models.value import Value

oto = WebOtoDevSdk(
    project_id=<YOU_PROJECT_ID>,
    api_key=<YOUR_API_KEY>,
    base_url='https://web.oto.dev/openapi/api/v1',
    timeout=10*60*1000
)
```


If you use Jupyter Notebooks, we recommend installing 'tabulate' (by using `pip install tabulate` in the terminal) to display some SDK function results as tables.
```
from tabulate import tabulate

def table(data):
    return tabulate(data, tablefmt='html', showindex=False, stralign="right")
```








### Project Properties

The following code sets some properties (not required) you may need. You can find a list of all available options in PROPERTIES [definition](definitions.py)

```
oto.properties.set('supported-language', 'en')
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



