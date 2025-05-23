# WebDev SDK (Python)

WebDev SDK is a tool that generates websites using AI. It is designed so that you can create a webpage automatically with the ability to control the result if it is required.

SDK is using the [web.oto.dev](https://web.oto.dev/) service. Please note that the service has a free plan by default, which will be subject to a number of restrictions in the future. You may want to consider a paid subscription version to remove restrictions and get more advanced features.


1. First, you need to **register on the [hub.oto.dev](https://hub.oto.dev/) service and copy an `API Key`** from the Dashboard
2. **Create a project and copy project ID** which is necessary for using the SDK
3. **Install SDK by using pip `pip install --upgrade web_oto_dev_sdk`**
4. We recommend to use [jupyter notebooks](https://jupyter.org/) to call SDK functions instead of a regular .py file (but it will also work with Python projects)

<br><br><br>


## A bit of [ ℹ️ INFO ] &nbsp; 🔜 &nbsp; turns into a [ 🌐 WEBSITE ]

<br>

### 💡 What you have as an ℹ️ INPUT

| Questions                             | Information               |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| What products and services do you have?                             | We provide an SDK for Python to simplify building websites by using AI               |
| Does your business offer a free first step for customers?           | You can quickly build a website by following the Quick Start guide located on github |
| What are the positive aspects of the client using the product?      | - You can build websites in minutes <br> - Use your social media, websites, and blogs as a source of information <br> - Websites have build-it speed and SEO optimization (Comming Soon) <br> - Calling one function will keep your website up-to-date |
| ... <be> *(You can add more Q&As you want)* ... | ... |

<br>

### 🔥 What you get as a 🌐 RESULT

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
sdk = WebOtoDevSdk(
    project_id=<YOU_PROJECT_ID>,
    api_key=<YOUR_API_KEY>,
    base_url='https://site.oto.dev/openapi/api/v1',
    timeout=10*60*1000
)
```

🛠 Your project basic settings
```
sdk.properties.set('supported-language', 'en')
```

Information required to build your website
```
sdk.meanings.set('mm-products-and-services', 'We provide an SDK for Python to simplify building websites by using AI')
sdk.meanings.set('mm-free-first-step', 'You can quickly build a website by following the Quick Start guide located on https://github.com/www-oto-dev/webdev-sdk/')
sdk.meanings.remove('mm-product-usage-advantages') # In case if they were set previously
sdk.meanings.add('mm-product-usage-advantages', 'You can build websites in minutes')
sdk.meanings.add('mm-product-usage-advantages', 'Use your social media, websites, and blogs as a source of information')
sdk.meanings.add('mm-product-usage-advantages', 'Websites have build-it speed and SEO optimization (Comming Soon)')
sdk.meanings.add('mm-product-usage-advantages', 'Calling one function will keep your website up-to-date')
```

🪄 Generating content & Building webpage
```
sdk.project.generate()
sdk.project.build()
```

✅ Done!
```
print(sdk.project.view())
```
Output: https://we.oto.dev/-/your-project-id


## 🌟 Concept

When a customer contacts a website creation agency, the process is broken down into several key stages: collecting information about the product, company, and target audience; writing marketing materials; designing the design and structure; writing code; and optimizing for search engines.

The concept of our project is to create [a website builder based on artificial intelligence](https://web.oto.dev/) without losing sight of the entire process of creating a website by professionals, but on the contrary, implementing the best solutions for each stage of the tasks automatically with the ability to intervene and make changes if necessary.


| Layer | Stage of website creation | Problems we solve |
|------|-------------------------------------------|----------------------------------------------------------------------------------------------|
| **Semantic** | ♻️ Collecting *meanings* | ☑️ Collecting information from previous website version <br> ☑️ Collecting meanings by answering questions <br> 🔜 Collecting information from social media <br> |
| **Content** | 🪄 Generating a *content* | ☑️ Generating contents using 'formulas' (set of queries) for GPT AI <br> ☑️ Generating images using 'formulas' for graphical generative AI <br> 🔜 Generating icons and sets of images in one style <br> 🔜 Using provided by user graphics and materials <br> 🔜 Text SEO optimization <br> |
| **Design** | 🎨 Creating *layouts*, a *structure* and *UI* | ☑️ Creating a webpage layout <br> 🔜 Creating a website structure and the ability to manage it <br> ☑️ Website templates (limited right now, can not generate new) <br> |
| **Technical** | 🧱 Building *web pages* by using HTML/JS/CSS.. | ☑️ Displaying a result as a website published on our domain <br> 🔜 An ability to download a result as HTML/JS/CSS code <br> ☑️ Adaptive web pages for all devices: desktops and mobile phones... <br> 🔜 Technical optimization for Search Engines (SEO): speed <br> |



## 🌀 Full Сapabilities

### Full SDK imports

Replace `<YOU_PROJECT_ID>` and `<YOUR_API_KEY>` as described above.
```
from web_oto_dev_sdk import WebOtoDevSdk
from web_oto_dev_sdk.models.property import Property
from web_oto_dev_sdk.models.meaning import Meaning
from web_oto_dev_sdk.models.formula import Formula
from web_oto_dev_sdk.models.value import Value

sdk = WebOtoDevSdk(
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

### Name-Value Services

There are several services available in SDK. The following services work on the key/value principle and allow you to generate, set, delete or view specified values.

| Service | Model  |  Task | Version Support |
|---------------------|-------------------------------------------|-------------------------------------------------------------------------------------|--------------------------|
| [sdk.properties](framework/python/documentation/services/PropertiesService.md) | [Property](framework/python/documentation/models/Property.md) | Controls project properties. [more info](#project-properties) | ☑️ Supports revisions by referring to specific Build textual ID (version generated by `sdk.project.build()` command | 
| [sdk.meanings](framework/python/documentation/services/MeaningsService.md) | [Meaning](framework/python/documentation/models/Meaning.md) | Controls project semantic layer, or "meanings" by setting them with `sdk.meanings.set("My Question", "My answer")` and `sdk.meanings.add("Same Question", "Another answer")`. You can collect meanings from the URL set in `reference-website-url` property by calling `sdk.project.collect()` | ✖️ No version support, planned for later | 
| [sdk.formulas](framework/python/documentation/services/FormulasService.md) | [Formula](framework/python/documentation/models/Formula.md) | By using formulas, you control how generative AI (ChatGPT, MidJourney, ..) will generate content. Inside formulas, values in square brackets `[some-value]` will be replaced with pre-defined shortcuts. You can use just plain text in your formulas. Values in `{some-value-name}` refer to generated VALUE for a formula with the specified in brackets name. You can use the *engine* parameter to specify what content you want to generate (`gpt` for text and `mj` for images). You can also set *type* to `list` (instead of `text`) to make AI return a list of values (like several advantages of the product will be treated as several different cards on the resulted web page | ✖️ No version support, planned for later | 
| [sdk.values](framework/python/documentation/services/ValuesService.md) | [Value](framework/python/documentation/models/Value.md) | Each formula will turn into one of several values after calling `sdk.project.generate()` | ☑️ Use `dataset` parameter to refer for specified version by textual ID | 
| [sdk.layouts](framework/python/documentation/services/LayoutsService.md) | [Formula](framework/python/documentation/models/Layout.md) | Controls page layouts by setting it by calling `sdk.layouts.set` where `name` is a page textual ID (slug) function or generating `sdk.layouts.new(init="imagine")` | ✖️ No version support, planned for later | 



<br><br><br>

**⚠️ Please note that the examples below are relevant to most of the key-value services but can have slightly different parameters and can also result in different behaviors.**

<br>


#### Setting values by 'name'

Remove previously set and **set a new value** by its name:
```
sdk.properties.set('reference-website-url', 'https://web.oto.dev')
sdk.formulas.set('about.text', 'Imagine how useful this product can be for end-users and write an article with examples about that', engine='gpt')
sdk.layouts.set('', '["main", "advantages", "about", "action"]')
```

**Removing value** that was previously set (or not):
```
sdk.meanings.remove('mm-product-usage-advantages')
```

**Adding a value** for a key with a same 'name'. That will create several values (For example, engine generates several values by solving formulas with a 'list' form)
```
sdk.meanings.add('mm-product-usage-advantages', 'You can build websites in minutes')
sdk.meanings.add('mm-product-usage-advantages', 'Use your social media, websites, and blogs as a source of information')
sdk.meanings.add('mm-product-usage-advantages', 'Websites have build-it speed and SEO optimization (Comming Soon)')
sdk.meanings.add('mm-product-usage-advantages', 'Calling one function will keep your website up-to-date')
```

Adding a second value for the previously set value:
```
sdk.properties.set('branding-gradient', 'linear-gradient(90deg, #00DBDE 0%, #FC00FF 100%);')
sdk.properties.add('branding-gradient', '')
```

Removing previously set with specified 'name' value and **updating several values**
```
sdk.properties.update([Property(key='supported-language', value='en'), Property(key='website-skin', value='softcorners')])
```



#### Obtaining values by 'name'

**Get a last value** for the specified key by its 'name'
```
sdk.properties.get('supported-language')
```

**Obtaining all values** as a list of models (find in proper Model the table above) for the specified key by 'name'
```
sdk.values.all('cases.cards.text')
sdk.values.all()
```

**Displaying all values as a table** (for Jupyter Notabook with defined 'table' function)
```
table(sdk.formulas.display())
```




#### Initialize + Version Support 

Some services support version control. Please have a look at the details in the table in this section.

**To init new set of values:**

You can use a `new` function to create a new set of values. By specifying the `init` parameter (`empty`, `default`, `imagine`), you can control whether will the function return an empty list (`init="empty"`), a list filled with default (`init="default"`) values or the one that will be set random or by using an AI (`init="imagine"`).
```
sdk.formulas.new(init='default')
```

The following functions **can also result in creating a new list of values**:
```
sdk.project.collect() # Adds new values to 'meanings' from a specified source (for example, an html page)
sdk.project.generate() # Creates a new 'dataset' and generates new 'values' by solving 'formulas'
sdk.project.build() # Create new 'pages' (Pages do not have a key/value access by the moment)
```



### Building the project

To build project you need to use [Project Service](framework/python/documentation/services/ProjectService.md)

| Order | Function                             | Action               |
|---|---|---|
| 1️⃣ | `sdk.project.collect()` | Collecting 'meanings' from the URL set by 'reference-website-url' property |
| 2️⃣ | `sdk.project.generate()` | Generate new 'values' based on 'formulas' |
| 3️⃣ | `sdk.project.build()` | Build new version of the website with the latest 'values' and 'layouts' |
| 4️⃣ | `sdk.project.view()` | Return a full webpage preview URL with an access token |



### Project Properties
Service: [Properties](framework/python/documentation/services/PropertiesService.md) | Model: [Property](framework/python/documentation/models/Property.md)

The following code sets some properties (not required) you may need. You can find a list of all available options in PROPERTIES [definition](information/definitions.py)

```
sdk.properties.set('supported-language', 'en')
sdk.properties.set('reference-website-url', 'https://your-old-website-to-collect-meanings.com')
sdk.properties.set('branding-color', '#40C3E4')
sdk.properties.set('light-color-threshold', '0.65')
sdk.properties.set('website-skin', 'softcorners')
sdk.properties.set('background-decoration', 'circle')
sdk.properties.set('branding-gradient', 'linear-gradient(90deg, #00DBDE 0%, #FC00FF 100%);')
sdk.properties.add('branding-gradient', '')
sdk.properties.update([Property(key='supported-language', value='en')])
table(sdk.properties.display())
```


### Meanings
Service: [Meanings](framework/python/documentation/services/MeaningsService.md) | Model: [Meaning](framework/python/documentation/models/Meaning.md)

Controls project semantic layer, or "meanings" by setting them with `sdk.meanings.set("My Question", "My answer")` and `sdk.meanings.add("Same Question", "Another answer")`. You can collect meanings from the URL set in `reference-website-url` property by calling `sdk.project.collect()`

Adding 'meanings' for predefined questions:
```
sdk.meanings.set('mm-products-and-services', 'We provide an SDK for Python to simplify building websites by using AI')
sdk.meanings.set('mm-free-first-step', 'You can quickly build a website by following the Quick Start guide located on https://github.com/www-oto-dev/webdev-sdk/')
sdk.meanings.remove('mm-product-usage-advantages') # In case if they were set previously
sdk.meanings.add('mm-product-usage-advantages', 'You can build websites in minutes')
sdk.meanings.add('mm-product-usage-advantages', 'Use your social media, websites, and blogs as a source of information')
sdk.meanings.add('mm-product-usage-advantages', 'Websites have build-it speed and SEO optimization (Comming Soon)')
sdk.meanings.add('mm-product-usage-advantages', 'Calling one function will keep your website up-to-date')
```

Adding 'meanings' for your own question list:
```
sdk.meanings.set("My Question", "My answer")
sdk.meanings.add("Same Question", "Another answer")
```

Collecting 'meanings' from a webpage:

```
sdk.properties.set('reference-website-url', 'https://web.oto.dev')
sdk.meanings.new(init="empty")
sdk.project.collect() # Takes some time
```


### Formulas
Service: [Formulas](framework/python/documentation/services/FormulasService.md) | Model: [Formula](framework/python/documentation/models/Formula.md)

Using formulas lets you control how generative AI (ChatGPT, MidJourney, ..) generates content. Inside formulas, values in square brackets `[some-value]` will be replaced with pre-defined shortcuts. You can use just a plain text in your formulas. Values in `{some-value-name}` refer to generated VALUE for a formula with the specified in brackets name. You can use the *engine* parameter to specify what content you want to generate (`gpt` for text and `mj` for images). You can also set *type* to `list` (instead of `text`) to make AI return a list of values (like several advantages of the product will be treated as several different cards on the resulting web page

```
sdk.formulas.new(init='default')

sdk.formulas.set('about.text', 'Imagine how useful this product can be for end-users and write an article with examples about that')
sdk.formulas.set('about.title', 'Create a Title the following text: {about.text}')
sdk.formulas.set('action.button.title', 'Same in a couple of words: {main.button.title}')
sdk.formulas.set('main.image', 'A plain in a sky [white-bg] [flat-vector-illustraton] [cartoon-style]', 'id', 'mj')
```

Do not forget to generate values and build the website to apply changes:
```
sdk.project.generate() # Takes up to 10 mins
sdk.project.build()
```

![Formulas](examples/service_formulas_display.png?raw=true "Formulas")
(Reference from values)

### Values
Service: [Values](framework/python/documentation/services/ValuesService.md) | Model: [Value](framework/python/documentation/models/Value.md)

```
# Generate values
sdk.project.generate() # Takes up to 10 mins

# We would like to change something
sdk.values.set('main.title', 'WebDev SDK')
```

Do not forget to build the website to apply changes in 'layouts'.
```
sdk.project.build()
```

(Refer to the formula by its 'name')
![Values](examples/service_values_display.png?raw=true "Values")



### Layout
Service: [Layouts](framework/python/documentation/services/LayoutsService.md) | Model: [Layout](framework/python/documentation/models/Layout.md)


Setting a layout for the default page (if parameter 'name' is '') in a simplified way by using only section names (engine will go through the 'values' list and will try to build proper sections):
```
sdk.layouts.set('', '["main", "advantages", "about", "action"]') # New layout (using latest 'values')
```


Do not forget to build the website to apply changes in 'layouts':
```
sdk.project.build()
```




### Building the website

Do not forget to build the website to apply changes in 'values' and 'layout.
```
sdk.project.build()
```


<br><br>


## ➡️  Examples

You can use the following notebooks as a starting point for your product  (⚠️ Do not forget to replace `project_id` and `api_key`):

| Example | Download | Format | Result |
|---------------------|-------------------------------------------|---------------------|---------------------|
| WebDev example page | 🪐 Jupyter Notebook | [WebDev example - Notebook](examples/webdev-sdk/webdev-sdk-example.ipynb) | Preview a [Result](https://web.oto.dev/-/webdev-sdk/)






