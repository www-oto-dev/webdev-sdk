// This file was generated by liblab | https://liblab.com/

package configmanager

import (
	"time"

	"github.com/swagger-api/swagger-petstore/pkg/webotodevsdkconfig"
)

type ConfigManager struct {
	Admin      webotodevsdkconfig.Config
	Project    webotodevsdkconfig.Config
	Properties webotodevsdkconfig.Config
	Meanings   webotodevsdkconfig.Config
	Formulas   webotodevsdkconfig.Config
	Values     webotodevsdkconfig.Config
	Layouts    webotodevsdkconfig.Config
}

func NewConfigManager(config webotodevsdkconfig.Config) *ConfigManager {
	return &ConfigManager{
		Admin:      config,
		Project:    config,
		Properties: config,
		Meanings:   config,
		Formulas:   config,
		Values:     config,
		Layouts:    config,
	}
}

func (c *ConfigManager) SetBaseUrl(baseUrl string) {
	c.Admin.SetBaseUrl(baseUrl)
	c.Project.SetBaseUrl(baseUrl)
	c.Properties.SetBaseUrl(baseUrl)
	c.Meanings.SetBaseUrl(baseUrl)
	c.Formulas.SetBaseUrl(baseUrl)
	c.Values.SetBaseUrl(baseUrl)
	c.Layouts.SetBaseUrl(baseUrl)
}

func (c *ConfigManager) SetTimeout(timeout time.Duration) {
	c.Admin.SetTimeout(timeout)
	c.Project.SetTimeout(timeout)
	c.Properties.SetTimeout(timeout)
	c.Meanings.SetTimeout(timeout)
	c.Formulas.SetTimeout(timeout)
	c.Values.SetTimeout(timeout)
	c.Layouts.SetTimeout(timeout)
}

func (c *ConfigManager) SetApiKey(apiKey string) {
	c.Admin.SetApiKey(apiKey)
	c.Project.SetApiKey(apiKey)
	c.Properties.SetApiKey(apiKey)
	c.Meanings.SetApiKey(apiKey)
	c.Formulas.SetApiKey(apiKey)
	c.Values.SetApiKey(apiKey)
	c.Layouts.SetApiKey(apiKey)
}

func (c *ConfigManager) GetAdmin() *webotodevsdkconfig.Config {
	return &c.Admin
}
func (c *ConfigManager) GetProject() *webotodevsdkconfig.Config {
	return &c.Project
}
func (c *ConfigManager) GetProperties() *webotodevsdkconfig.Config {
	return &c.Properties
}
func (c *ConfigManager) GetMeanings() *webotodevsdkconfig.Config {
	return &c.Meanings
}
func (c *ConfigManager) GetFormulas() *webotodevsdkconfig.Config {
	return &c.Formulas
}
func (c *ConfigManager) GetValues() *webotodevsdkconfig.Config {
	return &c.Values
}
func (c *ConfigManager) GetLayouts() *webotodevsdkconfig.Config {
	return &c.Layouts
}
