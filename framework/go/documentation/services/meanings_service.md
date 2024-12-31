# MeaningsService

A list of all methods in the `MeaningsService` service. Click on the method name to view detailed information about that method.

| Methods             | Description                                                                                                               |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------ |
| [New](#new)         | Create new collection (default or specified settings)                                                                     |
| [Get](#get)         | Obtain the lastest value for meaning with specified 'name'                                                                |
| [Set](#set)         | Remove all previous values for specified 'name' and add a new value                                                       |
| [Add](#add)         | Add a new value for specified 'name'                                                                                      |
| [All](#all)         | Obtain a list of all meanings with specified 'name'                                                                       |
| [Update](#update)   | Remove previously set and add new meanings with specified 'name' fileds with values from 'values' fileds of provided list |
| [Remove](#remove)   | Remove all values for specified 'name'                                                                                    |
| [Display](#display) | Display a list of all meanings with specified 'name'                                                                      |

## New

Create new collection (default or specified settings)

- HTTP Method: `PUT`
- Endpoint: `/meanings/revision/new`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | NewRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/meanings"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := meanings.NewRequestParams{}


response, err := client.Meanings.New(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Get

Obtain the lastest value for meaning with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/meanings/actual/get`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | GetRequestParams | ✅       | Additional request parameters |

**Return Type**

`string`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/meanings"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := meanings.GetRequestParams{}
params.SetName("string")

response, err := client.Meanings.Get(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Set

Remove all previous values for specified 'name' and add a new value

- HTTP Method: `PUT`
- Endpoint: `/meanings/actual/set`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | SetRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/meanings"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := meanings.SetRequestParams{}
params.SetName("string")

response, err := client.Meanings.Set(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Add

Add a new value for specified 'name'

- HTTP Method: `PUT`
- Endpoint: `/meanings/actual/add`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | AddRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/meanings"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := meanings.AddRequestParams{}
params.SetName("string")

response, err := client.Meanings.Add(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## All

Obtain a list of all meanings with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/meanings/all/get`

**Parameters**

| Name   | Type             | Required | Description                   |
| :----- | :--------------- | :------- | :---------------------------- |
| ctx    | Context          | ✅       | Default go language context   |
| params | AllRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]Meaning`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/meanings"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := meanings.AllRequestParams{}


response, err := client.Meanings.All(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Update

Remove previously set and add new meanings with specified 'name' fileds with values from 'values' fileds of provided list

- HTTP Method: `PUT`
- Endpoint: `/meanings/all/update`

**Parameters**

| Name    | Type                | Required | Description                   |
| :------ | :------------------ | :------- | :---------------------------- |
| ctx     | Context             | ✅       | Default go language context   |
| meaning | []Meaning           | ✅       |                               |
| params  | UpdateRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/meanings"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := meanings.UpdateRequestParams{}


response, err := client.Meanings.Update(context.Background(), request, params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Remove

Remove all values for specified 'name'

- HTTP Method: `DELETE`
- Endpoint: `/meanings/all/remove`

**Parameters**

| Name   | Type                | Required | Description                   |
| :----- | :------------------ | :------- | :---------------------------- |
| ctx    | Context             | ✅       | Default go language context   |
| params | RemoveRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/meanings"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := meanings.RemoveRequestParams{}


response, err := client.Meanings.Remove(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

## Display

Display a list of all meanings with specified 'name'

- HTTP Method: `GET`
- Endpoint: `/meanings/all/display`

**Parameters**

| Name   | Type                 | Required | Description                   |
| :----- | :------------------- | :------- | :---------------------------- |
| ctx    | Context              | ✅       | Default go language context   |
| params | DisplayRequestParams | ✅       | Additional request parameters |

**Return Type**

`[]byte`

**Example Usage Code Snippet**

```go
import (
  "fmt"
  "encoding/json"
  "web-dev-sdk/pkg/webotodevsdkconfig"
  "web-dev-sdk/pkg/webotodevsdk"
  "web-dev-sdk/pkg/meanings"
)

config := webotodevsdkconfig.NewConfig()
client := webotodevsdk.NewWebOtoDevSdk(config)


params := meanings.DisplayRequestParams{}


response, err := client.Meanings.Display(context.Background(), params)
if err != nil {
  panic(err)
}

fmt.Println(response)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
