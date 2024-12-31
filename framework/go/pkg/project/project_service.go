// This file was generated by liblab | https://liblab.com/

package project

import (
	"context"
	restClient "github.com/swagger-api/swagger-petstore/internal/clients/rest"
	"github.com/swagger-api/swagger-petstore/internal/clients/rest/httptransport"
	"github.com/swagger-api/swagger-petstore/internal/configmanager"
	"github.com/swagger-api/swagger-petstore/pkg/shared"
	"github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
	"time"
)

type ProjectService struct {
	manager *configmanager.ConfigManager
}

func NewProjectService(manager *configmanager.ConfigManager) *ProjectService {
	return &ProjectService{
		manager: manager,
	}
}

func (api *ProjectService) getConfig() *webotodevsdkconfig.Config {
	return api.manager.GetProject()
}

func (api *ProjectService) SetBaseUrl(baseUrl string) {
	config := api.getConfig()
	config.SetBaseUrl(baseUrl)
}

func (api *ProjectService) SetTimeout(timeout time.Duration) {
	config := api.getConfig()
	config.SetTimeout(timeout)
}

func (api *ProjectService) SetApiKey(apiKey string) {
	config := api.getConfig()
	config.SetApiKey(apiKey)
}

// Obtain project information
func (api *ProjectService) Info(ctx context.Context) (*shared.WebOtoDevSdkResponse[shared.Project], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("GET").
		WithPath("/project/info").
		WithConfig(config).
		WithContentType(httptransport.ContentTypeJson).
		WithResponseContentType(httptransport.ContentTypeJson).
		Build()

	client := restClient.NewRestClient[shared.Project](config)
	resp, err := client.Call(*request)
	if err != nil {
		return nil, shared.NewWebOtoDevSdkError[shared.Project](err)
	}

	return shared.NewWebOtoDevSdkResponse[shared.Project](resp), nil
}

// collect
func (api *ProjectService) Collect(ctx context.Context) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("POST").
		WithPath("/project/collect").
		WithConfig(config).
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

// generate
func (api *ProjectService) Generate(ctx context.Context) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("POST").
		WithPath("/project/generate").
		WithConfig(config).
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

// build
func (api *ProjectService) Build(ctx context.Context) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("POST").
		WithPath("/project/build").
		WithConfig(config).
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

// view
func (api *ProjectService) View(ctx context.Context) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("POST").
		WithPath("/project/view").
		WithConfig(config).
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

// imagine
func (api *ProjectService) Imagine(ctx context.Context, params ImagineRequestParams) (*shared.WebOtoDevSdkResponse[[]byte], *shared.WebOtoDevSdkError) {
	config := *api.getConfig()

	request := httptransport.NewRequestBuilder().WithContext(ctx).
		WithMethod("POST").
		WithPath("/project/imagine").
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
