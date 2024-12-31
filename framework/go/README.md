# WebOtoDevSdk Go SDK 1.0.3

Welcome to the WebOtoDevSdk SDK documentation. This guide will help you get started with integrating and using the WebOtoDevSdk SDK in your project.

[![This SDK was generated by liblab](https://public-liblab-readme-assets.s3.us-east-1.amazonaws.com/built-by-liblab-icon.svg)](https://liblab.com/?utm_source=readme)

## Versions

- API version: `1.0.1`
- SDK version: `1.0.3`

## About the API

API v1 for web.oto.dev service

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [API Key Authentication](#api-key-authentication)
- [Services](#services)
  - [Response Wrappers](#response-wrappers)
- [Models](#models)
- [License](#license)

# Setup & Configuration

## Supported Language Versions

This SDK is compatible with the following versions: `Go >= 1.19.0`

## Authentication

### API Key Authentication

The web-oto-dev-sdk API uses API keys as a form of authentication. An API key is a unique identifier used to authenticate a user, developer, or a program that is calling the API.

#### Setting the API key

When you initialize the SDK, you can set the API key as follows:

```go
import (
    "web-dev-sdk/pkg/webotodevsdk"
    "web-dev-sdk/pkg/webotodevsdkconfig"
  )

config := webotodevsdkconfig.NewConfig()
config.SetApiKey("YOUR-TOKEN")

sdk := webotodevsdk.NewWebOtoDevSdk(config)
```

If you need to set or update the API key after initializing the SDK, you can use:

```go
import (
    "web-dev-sdk/pkg/webotodevsdk"
    "web-dev-sdk/pkg/webotodevsdkconfig"
  )

config := webotodevsdkconfig.NewConfig()

sdk := webotodevsdk.NewWebOtoDevSdk(config)
sdk.SetApiKey("YOUR-TOKEN")
```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                              |
| :---------------------------------------------------------------- |
| [AdminService](documentation/services/admin_service.md)           |
| [ProjectService](documentation/services/project_service.md)       |
| [PropertiesService](documentation/services/properties_service.md) |
| [MeaningsService](documentation/services/meanings_service.md)     |
| [FormulasService](documentation/services/formulas_service.md)     |
| [ValuesService](documentation/services/values_service.md)         |
| [LayoutsService](documentation/services/layouts_service.md)       |

</details>

### Response Wrappers

All services use response wrappers to provide a consistent interface to return the responses from the API.

The response wrapper itself is a generic struct that contains the response data and metadata.

<details>
<summary>Below are the response wrappers used in the SDK:</summary>

#### `WebOtoDevSdkResponse[T]`

This response wrapper is used to return the response data from the API. It contains the following fields:

| Name     | Type                           | Description                                 |
| :------- | :----------------------------- | :------------------------------------------ |
| Data     | `T`                            | The body of the API response                |
| Metadata | `WebOtoDevSdkResponseMetadata` | Status code and headers returned by the API |

#### `WebOtoDevSdkError`

This response wrapper is used to return an error. It contains the following fields:

| Name     | Type                           | Description                                 |
| :------- | :----------------------------- | :------------------------------------------ |
| Err      | `error`                        | The error that occurred                     |
| Body     | `T`                            | The body of the API response                |
| Metadata | `WebOtoDevSdkResponseMetadata` | Status code and headers returned by the API |

#### `WebOtoDevSdkResponseMetadata`

This struct is shared by both response wrappers and contains the following fields:

| Name       | Type                | Description                                      |
| :--------- | :------------------ | :----------------------------------------------- |
| Headers    | `map[string]string` | A map containing the headers returned by the API |
| StatusCode | `int`               | The status code returned by the API              |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                         | Description |
| :------------------------------------------- | :---------- |
| [Project](documentation/models/project.md)   |             |
| [Property](documentation/models/property.md) |             |
| [Meaning](documentation/models/meaning.md)   |             |
| [Formula](documentation/models/formula.md)   |             |
| [Value](documentation/models/value.md)       |             |

</details>

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->