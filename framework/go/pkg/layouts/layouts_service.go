// This file was generated by liblab | https://liblab.com/

package layouts

import (
	"context"
	"time"
	restClient "web-dev-sdk/internal/clients/rest"
	"web-dev-sdk/internal/clients/rest/httptransport"
	"web-dev-sdk/internal/configmanager"
	"web-dev-sdk/pkg/shared"
	"web-dev-sdk/pkg/webotodevsdkconfig"
)

type LayoutsService struct {
	manager *configmanager.ConfigManager
}

func NewLayoutsService(manager *configmanager.ConfigManager) *LayoutsService {
	return &LayoutsService{
		manager: manager,
	}
}

func (api *LayoutsService) getConfig() *webotodevsdkconfig.Config {
	return api.manager.GetLayouts()
}

func (api *LayoutsService) SetBaseUrl(baseUrl string) {
	config := api.getConfig()
	config.SetBaseUrl(baseUrl)
}

func (api *LayoutsService) SetTimeout(timeout time.Duration) {
	config := api.getConfig()
	config.SetTimeout(timeout)
}

func (api *LayoutsService) SetApiKey(apiKey string) {
	config := api.getConfig()
	config.SetApiKey(apiKey)
}

func (api *LayoutsService) SetProjectId(projectId string) {
	config := api.getConfig()
	config.SetProjectId(projectId)
}

// Create new version (default or specified settings)
func (api *LayoutsService) New(ctx context.Context, params NewRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("PUT").
		WithPath("/layouts/revision/new").
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

// Obtain the lastest layout for page with specified 'name'
func (api *LayoutsService) Get(ctx context.Context, params GetRequestParams) (*shared.WebOtoDevSdkResponse[string], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("GET").
		WithPath("/layouts/actual/get").
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

// Remove all previous layouts for specified page with 'name' and add a new value
func (api *LayoutsService) Set(ctx context.Context, params SetRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("PUT").
		WithPath("/layouts/actual/set").
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

// Add a new value for specified page by 'name'
func (api *LayoutsService) Add(ctx context.Context, params AddRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("PUT").
		WithPath("/layouts/actual/add").
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

// Obtain a list of all layouts with specified 'name'
func (api *LayoutsService) All(ctx context.Context, params AllRequestParams) (*shared.WebOtoDevSdkResponse[[]shared.Value], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("GET").
		WithPath("/layouts/all/get").
		WithConfig(config).
		WithOptions(params).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[[]shared.Value](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[[]shared.Value](err)
	}

	return shared.NewWebOtoDevSdkResponse[[]shared.Value](resp), nil
}

// Remove previously set and add new layouts with specified 'name' fileds with layouts from 'layouts' fileds of provided list
func (api *LayoutsService) Update(ctx context.Context, value []shared.Value, params UpdateRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("PUT").
		WithPath("/layouts/all/update").
		WithConfig(config).
		WithBody(value).
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

// Remove all layouts for specified 'name'
func (api *LayoutsService) Remove(ctx context.Context, params RemoveRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("DELETE").
		WithPath("/layouts/all/remove").
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

// Display a list of all layouts with specified 'name'
func (api *LayoutsService) Display(ctx context.Context, params DisplayRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("GET").
		WithPath("/layouts/all/display").
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