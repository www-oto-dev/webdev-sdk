# ProjectService

A list of all methods in the `ProjectService` service. Click on the method name to view detailed information about that method.

| Methods               | Description                |
| :-------------------- | :------------------------- |
| [Info](#info)         | Obtain project information |
| [Collect](#collect)   | collect                    |
| [Generate](#generate) | generate                   |
| [Build](#build)       | build                      |
| [View](#view)         | view                       |
| [Imagine](#imagine)   | imagine                    |

## Info

Obtain project information

- HTTP Method: `GET`
- Endpoint: `/project/info`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`shared.Project`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)

response, err := client.Project.Info(context.Background())
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Collect

collect

- HTTP Method: `POST`
- Endpoint: `/project/collect`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)

response, err := client.Project.Collect(context.Background())
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Generate

generate

- HTTP Method: `POST`
- Endpoint: `/project/generate`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)

response, err := client.Project.Generate(context.Background())
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Build

build

- HTTP Method: `POST`
- Endpoint: `/project/build`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)

response, err := client.Project.Build(context.Background())
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## View

view

- HTTP Method: `POST`
- Endpoint: `/project/view`

**Parameters**

| Name | Type    | Required | Description                 |
| :--- | :------ | :------- | :-------------------------- |
| ctx  | Context | ✅       | Default go language context |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)

response, err := client.Project.View(context.Background())
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Imagine

imagine

- HTTP Method: `POST`
- Endpoint: `/project/imagine`

**Parameters**

| Name   | Type                 | Required | Description                   |
| :----- | :------------------- | :------- | :---------------------------- |
| ctx    | Context              | ✅       | Default go language context   |
| params | ImagineRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/project"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := project.ImagineRequestParams{}


response, err := client.Project.Imagine(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
