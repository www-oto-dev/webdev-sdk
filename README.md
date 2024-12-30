# WebDev SDK (Python)

WebDev SDK is a tool that generates websites using AI. It is designed so that you can create a webpage automatically with the ability to control the result if it is required.

SDK is using the [web.oto.dev](https://web.oto.dev/) service. Please note that the service has a free plan by default, which will be subject to a number of restrictions in the future. You may want to consider a paid subscription version to remove restrictions and get more advanced features.


1. First, you need to **register on the [hub.oto.dev](https://hub.oto.dev/) service and copy an `API Key`** from the Dashboard
2. **Create a project and copy project ID** which is necessary for using the SDK
3. **Install SDK by using pip `pip install web_oto_dev_sdk`**
4. We recommend to use [jupyter notebooks](https://jupyter.org/) to call SDK functions instead of a regular .py file (but it will also work with Python projects)

.
.
.


## A bit of [ ℹ️ INFO ] 🔜 turns into a [ 🌐 WEBSITE ]

### 💡 What you have as an INPUT

| Questions                             | Information               |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| What products and services do you have?                             | We provide an SDK for Python to simplify building websites by using AI               |
| Does your business offer a free first step for customers?           | You can quickly build a website by following the Quick Start guide located on github |
| What are the positive aspects of the client using the product?      | - You can build websites in minutes <br> - Use your social media, websites, and blogs as a source of information <br> - Websites have build-it speed and SEO optimization (Comming Soon) <br> - Calling one function will keep your website up-to-date |
| ... <be> *(You can add more Q&As you want)* ... | ... |

### ⬇️
### 🔥 What you get as a RESULT

![Main](examples/webdev-sdk/webdev-sdk--main.png?raw=true "Main")
![Advantages](examples/webdev-sdk/webdev-sdk--advantages.png?raw=true "Advantages")
![About](examples/webdev-sdk/webdev-sdk--about.png?raw=true "About")
![Action](examples/webdev-sdk/webdev-sdk--action.png?raw=true "Action")



## 🚀 Quick Start

Installing
```
pip install web_oto_dev_sdk
```

🔑 Configuring the SDK. Replace `<YOU_PROJECT_ID>` with project ID from the [create a website](https://hub.oto.dev/app/websites/create/) (or edit) screen and `<YOUR_API_KEY>` from the [dashboard](https://hub.oto.dev/app/dashboard/)

```
from web_oto_dev_sdk import WebOtoDevSdk
oto = WebOtoDevSdk(
    project_id=<YOU_PROJECT_ID>,
    api_key=<YOUR_API_KEY>,
    base_url='https://web.oto.dev/openapi/api/v1',
    timeout=10*60*1000
)
```

🛠 Your project basic settings
```
oto.properties.set('supported-language', 'en')
```

Information required to build your website
```
oto.meanings.set('mm-products-and-services', 'We provide an SDK for Python to simplify building websites by using AI')
oto.meanings.set('mm-free-first-step', 'You can quickly build a website by following the Quick Start guide located on https://github.com/www-oto-dev/webdev-sdk/')
oto.meanings.remove('mm-product-usage-advantages') # In case if they were set previously
oto.meanings.add('mm-product-usage-advantages', 'You can build websites in minutes')
oto.meanings.add('mm-product-usage-advantages', 'Use your social media, websites, and blogs as a source of information')
oto.meanings.add('mm-product-usage-advantages', 'Websites have build-it speed and SEO optimization (Comming Soon)')
oto.meanings.add('mm-product-usage-advantages', 'Calling one function will keep your website up-to-date')
```

🪄 Generating content & Building webpage
```
oto.project.generate()
oto.project.build()
```

✅ Done!
```
print(oto.project.view())
```
Output: https://we.oto.dev/-/<YOU_PROJECT_ID>


## 🌟 Concept

When a customer contacts a website creation agency, the process is broken down into several key stages: collecting information about the product, company, and target audience; writing marketing materials; designing the design and structure; writing code; and optimizing for search engines.

The concept of our project is to create [a website builder based on artificial intelligence](https://web.oto.dev/) without losing sight of the entire process of creating a website by professionals, but on the contrary, implementing the best solutions for each stage of the tasks automatically with the ability to intervene and make changes if necessary.


| Layer | Stage of website creation | Problems we solve |
|------|-------------------------------------------|----------------------------------------------------------------------------------------------|
| **Semantic** | ♻️ Collecting *meanings* | ☑️ Collecting information from previous website version <br> ☑️ Collecting meanings by answering questions <br> 🔜 Collecting information from social media <br> |
| **Content** | 🪄 Generating a *content* | 
☑️ Generating contents using 'formulas' (set of queries) for GTP models <br> 
☑️ Generating images using 'formulas' for graphical generative AI <br> 
🔜 Generating icons and sets of images in one style <br> 
🔜 Using provided by user graphics and materials <br> 
🔜 Text SEO optimization <br> |
| **Design** | 🎨 Creating *layouts*, a *structure* and an *UI* | [☑️] Creating a webpage layout \ |
|  |  | [🔜] Creating a website structure and the ability to manage it \ |
|  |  | [☑️] Website templates (limited right now, can not generate new) |
| **Technical** | 🧱 Building *web pages* by using HTML/JS/CSS.. | [☑️] Displaying a result as a website published on our domain \ |
|  |  | [🔜] An ability to download a result as HTML/JS/CSS code \ |
|  |  | [☑️] Adaptive web pages for all devices: desktops and mobile phones.. \ |
|  |  | [🔜] Technical optimization for Search Engines (SEO): page loading speed |



## 🌀 Full Сapabilities

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

The following code sets some properties (not required) you may need. You can find a list of all available options in PROPERTIES [definition](information/definitions.py)

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

## ➡️ Example

[Jupyter Notebook example](examples/webdev-sdk/webdev-sdk-example.ipynb?raw=true)




