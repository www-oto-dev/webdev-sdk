// This file was generated by liblab | https://liblab.com/

package configmanager

import (
	"time"

	"github.com/swagger-api/swagger-petstore/pkg/webdevsdkconfig"
)

type ConfigManager struct {
	V0 webdevsdkconfig.Config
}

func NewConfigManager(config webdevsdkconfig.Config) *ConfigManager {
	return &ConfigManager{
		V0: config,
	}
}

func (c *ConfigManager) SetBaseUrl(baseUrl string) {
	c.V0.SetBaseUrl(baseUrl)
}

func (c *ConfigManager) SetTimeout(timeout time.Duration) {
	c.V0.SetTimeout(timeout)
}

func (c *ConfigManager) SetAccessToken(accessToken string) {
	c.V0.SetAccessToken(accessToken)
}

func (c *ConfigManager) UpdateAccessToken(originalValue string, newValue string) {

	if c.V0.AccessToken != nil && *c.V0.AccessToken == originalValue {
		c.V0.SetAccessToken(newValue)
	}
}

func (c *ConfigManager) GetV0() *webdevsdkconfig.Config {
	return &c.V0
}
