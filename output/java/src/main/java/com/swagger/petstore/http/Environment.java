// This file was generated by liblab | https://liblab.com/

package com.swagger.petstore.http;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

/**
 * SDK Environments
 */
@Getter
@RequiredArgsConstructor
public enum Environment {
  DEFAULT("https://api.example.com");

  private final String url;
}
