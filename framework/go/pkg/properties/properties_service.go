// This file was generated by liblab | https://liblab.com/

package properties

import (
	"context"
	"time"
	restClient "web-dev-sdk/internal/clients/rest"
	"web-dev-sdk/internal/clients/rest/httptransport"
	"web-dev-sdk/internal/configmanager"
	"web-dev-sdk/pkg/shared"
	"web-dev-sdk/pkg/webotodevsdkconfig"
)

type PropertiesService struct {
	manager *configmanager.ConfigManager
}

func NewPropertiesService(manager *configmanager.ConfigManager) *PropertiesService {
	return &PropertiesService{
		manager: manager,
	}
}

func (api *PropertiesService) getConfig() *webotodevsdkconfig.Config {
	return api.manager.GetProperties()
}

func (api *PropertiesService) SetBaseUrl(baseUrl string) {
	config := api.getConfig()
	config.SetBaseUrl(baseUrl)
}

func (api *PropertiesService) SetTimeout(timeout time.Duration) {
	config := api.getConfig()
	config.SetTimeout(timeout)
}

func (api *PropertiesService) SetApiKey(apiKey string) {
	config := api.getConfig()
	config.SetApiKey(apiKey)
}

func (api *PropertiesService) SetProjectId(projectId string) {
	config := api.getConfig()
	config.SetProjectId(projectId)
}

// Create new build (default or specified settings)
func (api *PropertiesService) New(ctx context.Context, params NewRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("PUT").
		WithPath("/properties/revision/new").
		WithConfig(config).
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[[]byte](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[[]byte](err)
	}

	return shared.NewWebOtoDevSdkResponse[[]byte](resp), nil
}

// Obtain the lastest value for formula with specified 'name'
func (api *PropertiesService) Get(ctx context.Context, params GetRequestParams) (*shared.WebOtoDevSdkResponse[string], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("GET").
		WithPath("/properties/actual/get").
		WithConfig(config).
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[string](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[string](err)
	}

	return shared.NewWebOtoDevSdkResponse[string](resp), nil
}

// Remove all previous values for specified 'name' and add a new value
func (api *PropertiesService) Set(ctx context.Context, params SetRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("PUT").
		WithPath("/properties/actual/set").
		WithConfig(config).
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[[]byte](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[[]byte](err)
	}

	return shared.NewWebOtoDevSdkResponse[[]byte](resp), nil
}

// Add a new value for specified 'name'
func (api *PropertiesService) Add(ctx context.Context, params AddRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("PUT").
		WithPath("/properties/actual/add").
		WithConfig(config).
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[[]byte](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[[]byte](err)
	}

	return shared.NewWebOtoDevSdkResponse[[]byte](resp), nil
}

// Obtain a list of all properties with specified 'name'
func (api *PropertiesService) All(ctx context.Context, params AllRequestParams) (*shared.WebOtoDevSdkResponse[[]Property], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("GET").
		WithPath("/properties/all/get").
		WithConfig(config).
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[[]Property](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[[]Property](err)
	}

	return shared.NewWebOtoDevSdkResponse[[]Property](resp), nil
}

// Remove previously set and add new properties with specified 'name' fileds with values from 'values' fileds of provided list
func (api *PropertiesService) Update(ctx context.Context, property []Property, params UpdateRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("PUT").
		WithPath("/properties/all/update").
		WithConfig(config).
		WithBody(property).
		AddHeader("CONTENT-TYPE", "application/json").
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[[]byte](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[[]byte](err)
	}

	return shared.NewWebOtoDevSdkResponse[[]byte](resp), nil
}

// Remove all values for specified 'name'
func (api *PropertiesService) Remove(ctx context.Context, params RemoveRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("DELETE").
		WithPath("/properties/all/remove").
		WithConfig(config).
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[[]byte](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[[]byte](err)
	}

	return shared.NewWebOtoDevSdkResponse[[]byte](resp), nil
}

// Display a list of all properties with specified 'name'
func (api *PropertiesService) Display(ctx context.Context, params DisplayRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("GET").
		WithPath("/properties/all/display").
		WithConfig(config).
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[[]byte](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[[]byte](err)
	}

	return shared.NewWebOtoDevSdkResponse[[]byte](resp), nil
}