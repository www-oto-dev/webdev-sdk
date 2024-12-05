// This file was generated by liblab | https://liblab.com/

package webdevsdk

import (
	"github.com/swagger-api/swagger-petstore/internal/configmanager"
	"github.com/swagger-api/swagger-petstore/pkg/v0"
	"github.com/swagger-api/swagger-petstore/pkg/webdevsdkconfig"
	"time"
)

type WebdevSdk struct {
	V0      *v0.V0Service
	manager *configmanager.ConfigManager
}

func NewWebdevSdk(config webdevsdkconfig.Config) *WebdevSdk {
	manager := configmanager.NewConfigManager(config)
	return &WebdevSdk{
		V0:      v0.NewV0Service(manager),
		manager: manager,
	}
}

func (w *WebdevSdk) SetBaseUrl(baseUrl string) {
	w.manager.SetBaseUrl(baseUrl)
}

func (w *WebdevSdk) SetTimeout(timeout time.Duration) {
	w.manager.SetTimeout(timeout)
}

func (w *WebdevSdk) SetAccessToken(accessToken string) {
	w.manager.SetAccessToken(accessToken)
}

// c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
